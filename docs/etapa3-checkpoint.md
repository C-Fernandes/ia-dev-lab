# Etapa 3 — Checkpoint humano obrigatório

## Checkpoint definido

**Antes de instalar ou alterar qualquer configuração global do Claude Code**
(plugin marketplace, hooks fora deste repositório, config em `~/.claude/`),
a execução para e espera aprovação humana explícita antes de rodar qualquer
comando.

**Por quê esse e não outro:** o guardrail da Etapa 1 (`check_pip_install.py`)
só protege o que está *dentro* deste repositório — `git revert` desfaz
qualquer coisa commitada aqui. Uma mudança de config global do Claude Code
(ex.: instalar um plugin de um marketplace de terceiro) não é versionada,
afeta outras sessões e projetos além deste, e não tem "desfazer" via git.
É exatamente o tipo de ação que passa despercebida se ninguém parar para
confirmar.

## Simulação (aconteceu de verdade durante a Etapa 2, não é encenação)

Ao investigar a ferramenta de enforcement de TDD (item 6 da Etapa 2), a
opção mais completa era instalar o plugin real `tdd-guard` via
`claude plugin marketplace add nizos/tdd-guard` + `claude plugin install`.
Antes de rodar qualquer um desses comandos, a execução parou e apresentou
ao usuário, em texto explícito:

> "Instala tdd-guard de verdade (plugin marketplace externo, muda config
> global do Claude Code) ou só documenta o comportamento sem instalar?"

com as opções: instalar de verdade, ou só documentar sem instalar — e o
motivo de cada uma (a instalação de verdade mexe na config global do
usuário, fora do escopo deste repositório).

## Decisão tomada

**Aprovar** — o usuário escolheu "Instalar de verdade (Recomendado)".
Só depois dessa aprovação explícita os comandos
`claude plugin marketplace add nizos/tdd-guard` e
`claude plugin install tdd-guard@tdd-guard` foram executados (ver
`docs/etapa2-tdd.md` e `docs/sessao-log.md` para o registro completo).

## Papel humano assumido

**Aprovador final de mudanças com efeito fora do repositório versionado.**
Justificativa: dentro do repositório, hooks e testes já dão rede de
segurança reversível (Etapa 1 e 2). Fora dele — configuração global,
credenciais, marketplaces externos — não existe essa rede, então a decisão
de prosseguir não pode ser automática; precisa de alguém que entenda o
efeito colateral (afeta todas as sessões futuras do usuário, não só este
projeto) e assuma a responsabilidade por ele.
