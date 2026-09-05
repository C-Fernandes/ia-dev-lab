# Plano de Implementação: Validador de Senha Forte com Políticas Configuráveis

**Branch**: `001-validador-senha-forte` | **Data**: 2026-09-04 | **Spec**: [spec.md](./spec.md)

**Entrada**: Especificação da funcionalidade em `/specs/001-validador-senha-forte/spec.md`

## Resumo

Avaliar uma senha contra uma política configurável e devolver, numa única chamada, se ela é válida e a lista dos critérios não atendidos. A abordagem usa uma política imutável e um resultado de validação imutável, ambos sem estado, com biblioteca padrão apenas.

## Contexto Técnico

**Linguagem/Versão**: Python 3 (biblioteca padrão apenas)

**Dependências principais**: Nenhuma. `dataclasses` e `typing` são da biblioteca padrão

**Armazenamento**: Não se aplica. A validação é em memória e não persiste nada

**Testes**: `unittest` da biblioteca padrão, executável por `python3 -m pytest -q`

**Plataforma alvo**: Qualquer ambiente com Python 3, sem dependência de sistema operacional

**Tipo de projeto**: Biblioteca (módulo importável em `src/`)

**Metas de desempenho**: Não se aplica. A avaliação é sobre uma string curta e não é caminho crítico

**Restrições**: Não registrar em log, não armazenar e não transmitir a senha avaliada (Premissas da spec)

**Escala/Escopo**: Um módulo, duas entidades, cinco critérios de composição

## Verificação da Constituição

*GATE: precisa passar antes da implementação. Reavaliado depois do desenho.*

| Princípio | Situação | Como este plano atende |
|-----------|----------|------------------------|
| I. Especificação antes do código | ✅ Passa | `spec.md` escrita e revisada antes deste plano; nenhuma linha de `src/` escrita ainda |
| II. Test-First | ✅ Passa | Fase 1 do plano escreve os testes derivados dos cenários e verifica que falham antes da Fase 2 |
| III. Sem dependências externas | ✅ Passa | Só biblioteca padrão; `unittest` para testes, como no validador de e-mail |
| IV. Checkpoint humano antes da `main` | ✅ Passa | Fase 4 para no checkpoint já definido em `docs/checkpoint-humano.md` |
| V. Histórico como registro do processo | ✅ Passa | Um commit por fase: spec, plano, testes, implementação |

Nenhuma violação. A tabela de Complexity Tracking fica vazia.

## Estrutura do Projeto

### Documentação desta funcionalidade

```text
specs/001-validador-senha-forte/
├── spec.md              # Especificação (o quê e por quê)
├── plan.md              # Este arquivo (como)
└── tasks.md             # Plano de tarefas executável
```

Não há `research.md`, `data-model.md`, `contracts/` nem `quickstart.md`. Não existe incógnita técnica a pesquisar, o modelo de dados são duas dataclasses descritas aqui, não há contrato de API e o módulo é importável direto. Criar esses arquivos vazios só para seguir o template não agrega.

### Código-fonte (raiz do repositório)

```text
src/
├── hello.py
├── validador_email.py
├── validador_email_simples.py
├── validador_documentos.py      # Funcionalidade 1, já entregue
└── validador_senha.py           # NOVO - esta funcionalidade

tests/
├── test_validador_email_simples.py
├── test_validador_documentos.py
└── test_validador_senha.py      # NOVO - esta funcionalidade
```

**Decisão de estrutura**: projeto único, layout plano já em uso. O repositório não tem `models/`, `services/` nem `lib/`, e criar essa hierarquia para um módulo pequeno não se justifica. Mantém-se a convenção do README: regra de negócio em `src/`, teste espelhado em `tests/`.

## Decisões de Desenho

**Política como dataclass imutável (`frozen=True`), com validação no `__post_init__`.**
A política é configuração, não estado mutável. Congelá-la impede que uma parte do sistema altere os critérios que outra está usando. O `__post_init__` levanta `ValueError` para `comprimento_minimo` negativo (FR-009) no momento da construção, e não no da validação, porque política impossível é erro de configuração.

**Resultado como dataclass com `valida: bool` e `pendencias: tuple[str, ...]`.**
Retornar só `False` obrigaria uma segunda chamada para descobrir o motivo, que é o problema da História 1. A tupla é imutável para que quem chama não altere a lista por engano. `valida` é derivado de `pendencias` estar vazia, o que garante FR-007 por construção.

**Cada critério é uma checagem independente, todas executadas sempre.**
Sem `return` antecipado na primeira falha (FR-002). O custo é irrelevante para uma string curta e o resultado é o feedback completo.

**Caractere especial definido por exclusão: não é letra, não é dígito, não é espaço em branco.**
Definir por lista de permissão (`!@#$%...`) rejeitaria símbolos válidos como `£` e exigiria manutenção manual. Usar `str.isalnum()` e `str.isspace()` cobre Unicode e resolve dois casos de borda da spec: o acento conta como letra minúscula e o espaço não conta como caractere especial.

**Mensagens de pendência montadas com o valor exigido interpolado.**
FR-006 pede que a mensagem diga o que falta. Para o comprimento, "mínimo de 12 caracteres" só funciona se o 12 vier da política, e não de texto fixo que desatualiza na primeira mudança de configuração.

## Fases

- **Fase 1 — Testes**: escrever `tests/test_validador_senha.py` cobrindo os nove cenários de aceite e os seis casos de borda. Verificar que falha por `ImportError`.
- **Fase 2 — Implementação**: escrever `src/validador_senha.py` até a suíte inteira passar.
- **Fase 3 — Verificação**: rodar a suíte completa do repositório e conferir que os testes anteriores continuam passando.
- **Fase 4 — Revisão**: revisar o diff e passar pelo checkpoint humano antes do Pull Request.

## Complexity Tracking

Sem violações da constituição. Nada a justificar.
