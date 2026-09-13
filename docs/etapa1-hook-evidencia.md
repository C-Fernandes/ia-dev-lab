# Etapa 1 — Hook de guardrail e evidência do bloqueio

## Risco escolhido

O `CLAUDE.md` do projeto define: "Não utilize bibliotecas externas sem que
estejam documentadas." Esse é um risco real e recorrente em sessões com
agente de IA: pedir para "resolver X" pode levar o agente a rodar
`pip install <pacote>` sem que ninguém tenha decidido, documentado ou
revisado essa dependência nova. Risco diferente do exemplo de aula
("bloquear merge na main").

## Controle implementado

- `docs/dependencias-aprovadas.md`: lista de pacotes PyPI aprovados/documentados
  (hoje só `pytest`, já em uso no projeto).
- `.claude/hooks/check_pip_install.py`: hook `PreToolUse` no tool `Bash`. Extrai
  o(s) pacote(s) de qualquer comando `pip install` / `pip3 install` (exceto uso
  com `-r`/`--requirement`) e compara com a lista aprovada. Se algum pacote não
  estiver na lista, imprime o motivo em stderr e sai com código 2 — código que
  o Claude Code interpreta como "bloquear a execução da ferramenta".
- `.claude/settings.json`: registra o hook no evento `PreToolUse` para o
  matcher `Bash`.

## Teste 1 — bloqueio ao vivo (disparado sem querer, já prova o funcionamento)

Ao tentar rodar um comando Bash cujo texto continha literalmente
`pip install requests` (durante a escrita dos testes do próprio hook), o
harness bloqueou a chamada de ferramenta antes de executar:

```
PreToolUse:Bash hook error: [python3 .claude/hooks/check_pip_install.py]:
BLOQUEADO: pacote(s) externo(s) nao documentado(s): requests. Adicione em
docs/dependencias-aprovadas.md antes de instalar (regra do CLAUDE.md: nao
usar libs externas sem documentar).
```

## Teste 2 — disparo deliberado

Comando executado de propósito para confirmar o bloqueio:

```
$ pip install requests
```

Resultado:

```
PreToolUse:Bash hook error: [python3 .claude/hooks/check_pip_install.py]:
BLOQUEADO: pacote(s) externo(s) nao documentado(s): requests. Adicione em
docs/dependencias-aprovadas.md antes de instalar (regra do CLAUDE.md: nao
usar libs externas sem documentar).
```

A instalação **não** aconteceu — a ferramenta Bash foi impedida de rodar.

## Teste 3 — casos de controle (script chamado diretamente com payloads de teste)

| Payload (`tool_input.command`) | Resultado esperado | Resultado obtido |
|---|---|---|
| `pip install requests` | bloquear | `exit=2`, mensagem de bloqueio |
| `pip install pytest` (documentado) | permitir | `exit=0`, sem saída |
| `ls -la` (não relacionado) | permitir | `exit=0`, sem saída |

## Bug encontrado e corrigido durante o teste

A primeira versão do regex de extração de argumentos (`(?P<args>.*)`) capturava
texto além do comando `pip install`, incluindo qualquer coisa depois de `||`
ou `;` na mesma linha de shell — um teste com
`pip install pytest --dry-run 2>&1 || pip3 --version` acabou sendo
interpretado como tentativa de instalar o pacote inválido `"2"`. Corrigido
limitando a captura a `[^;&|\n]*`, parando nos separadores de shell.
