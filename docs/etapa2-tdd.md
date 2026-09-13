# Etapa 2 — TDD como Guard-Rail

## 1. Ciclo Red-Green-Refactor (tarefa: `validar_cartao_credito`, algoritmo de Luhn)

Três commits, um por fase, na branch `feature/etapa1-harness`:

| Fase | Commit | O que prova |
|---|---|---|
| RED | `3a730a1` | `tests/test_validador_cartao_credito.py` criado antes de qualquer implementação; rodar pytest dava `ModuleNotFoundError: No module named 'validador_cartao_credito'` |
| GREEN | `0a7126a` | `src/validador_cartao_credito.py` implementado; suíte passou 7/7 |
| REFACTOR | `7cc8163` | loop reescrito com `enumerate` em vez de flag booleana alternante; 7/7 continuou verde, comportamento idêntico |

## 2. Investigação da ferramenta de enforcement: tdd-guard

**Instalado de verdade** (não apenas documentado), via marketplace oficial de
plugins do Claude Code:

```
claude plugin marketplace add nizos/tdd-guard
claude plugin install tdd-guard@tdd-guard
```

Isso registra 3 hooks globais (escopo *user*, fora deste repositório):
`PreToolUse` (matcher `Write|Edit|MultiEdit|TodoWrite`), `UserPromptSubmit` e
`SessionStart`, todos rodando `npx tdd-guard@latest`. Para o projeto, foi
instalado o reporter `tdd-guard-pytest` (documentado antes em
`docs/dependencias-aprovadas.md`, respeitando o hook da Etapa 1) e configurado
`tdd_guard_project_root` em `pytest.ini`. Rodar `pytest` de fato grava
resultados reais em `.claude/tdd-guard/data/test.json` (confirmado, 30/30
testes registrados corretamente) — essa parte funciona.

### Achado: a validação por IA falha aberta (fail-open) sem API key

O objetivo do hook `PreToolUse` é bloquear uma edição de `src/` quando não
existe teste falho correspondente (i.e., pular a fase RED). Na prática, ao
escrever `src/validador_hora.py` **sem nenhum teste antes** (de propósito,
para a tarefa 7 desta etapa), o hook **não bloqueou** a escrita.

Investigando o código-fonte do pacote (`~/.npm/_npx/.../tdd-guard/dist/`):

- `Config.js`: `DEFAULT_CLIENT = 'sdk'` — por padrão a validação usa
  `@anthropic-ai/claude-agent-sdk`, que precisa de credencial própria (API
  key), não reaproveita a sessão logada do Claude Code CLI.
- `cli/tdd-guard.js`: todo o `run()` roda dentro de um `try/catch` que, em
  caso de erro (ex.: SDK sem API key configurada), só faz
  `console.error(...)` e **sempre `process.exit(0)`** — ou seja, qualquer
  falha na validação vira "permitir", nunca "bloquear".
- Reproduzido manualmente: `npx tdd-guard@latest` recebendo via stdin um
  payload `PreToolUse`/`Write` real (arquivo `.json` de teste) retornou
  `exit=0` sem nenhuma saída — nem bloqueio, nem erro visível para quem
  chamou o hook.

**Conclusão da investigação:** tdd-guard é uma ferramenta real e bem
projetada (o reporter pytest funciona, a decisão de design de bloquear só
quando há teste RED existente é correta), mas seu enforcement por IA depende
de uma credencial de modelo configurada à parte (`ANTHROPIC_API_KEY` ou
`useSystemClaude`/cliente `cli` apontando para um binário local do Claude).
Sem isso, ela **não** impede a ação — apenas registra dados de teste
silenciosamente. Isso é um risco de segurança-por-obscuridade: o
desenvolvedor pode achar que está protegido e não está. Em um uso real, o
próximo passo seria configurar `TDD_GUARD_VALIDATION_CLIENT=cli` com
`useSystemClaude` apontando para o binário já autenticado
(`/Users/mariaclara_fo/.local/bin/claude`), o que não foi testado aqui por
estar fora do escopo desta atividade.

## 3. Comparação: tarefa com TDD vs. tarefa sem TDD

| | Com TDD (`validar_cartao_credito`) | Sem TDD (`validar_hora`) |
|---|---|---|
| Ordem | Teste → Red → implementação → Green → Refactor | Implementação direta, teste só depois |
| Testes que passam | 7/7 desde o commit GREEN | 6/9 (3 falhas descobertas só depois) |
| Casos de borda cobertos desde o início | Sim: espaços, não-numérico, string vazia, tipo errado, dígito verificador errado | Não: formato de 2 dígitos obrigatório e dígitos unicode nunca foram considerados na hora de escrever o código |
| Bugs reais encontrados | Nenhum após GREEN | 3: aceita `"1:5"`, aceita `"09:9"`, aceita dígitos unicode (`"٢٣:٠٠"`) |

**Conclusão:** escrever o teste antes obrigou a decidir o contrato exato
(o que conta como entrada válida) antes de escrever a lógica — os casos de
borda saíram naturalmente da própria lista de testes. Sem esse passo, a
implementação de `validador_hora` cobriu o "caminho feliz" e o óbvio
(intervalo 0-23/0-59), mas deixou passar despercebido o requisito implícito
de formato de 2 dígitos e a possibilidade de dígitos unicode — só apareceram
ao escrever teste de propósito depois, quando já era tarde para influenciar
o design da função.
