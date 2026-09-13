# Etapa 5 — Comparação entre as duas versões do diagrama

| | v1 (prompt curto) | v2 (prompt com contexto) |
|---|---|---|
| Elementos mostrados | `dev`, scripts, testes | `dev`, Claude Code, tdd-guard, validadores, testes, hooks, docs |
| Acoplamento real (zero entre validadores) | Não aparece — "Scripts de validação" é tratado como um bloco só | Também simplifica em 1 contêiner, mas a descrição do contêiner (`zero import entre si`) deixa a decisão da Etapa 4 explícita |
| O harness em si (hooks, tdd-guard, checkpoint) | Ausente | Presente — é literalmente o assunto central desta atividade |
| Poderia ser o diagrama de qualquer projeto Python com testes | Sim | Não — é específico deste repositório e desta atividade |

## Qual comunica melhor

**v2.** v1 não está errado, mas é genérico: mostra a mesma coisa que
qualquer "projeto Python com pytest" mostraria, e por isso não ajuda quem
olha o diagrama a entender as decisões que essa atividade tomou (por que
existe `.claude/hooks`, por que `tdd-guard` aparece como sistema externo em
vez de dependência normal, por que "testes" e "validadores" nunca se
misturam).

v2 comunica melhor porque:

1. Mostra o harness como parte da arquitetura, não como detalhe
   escondido — que é exatamente o ponto da Etapa 1/2 desta atividade.
2. Marca `tdd-guard` como sistema *externo* (`System_Ext`), deixando visível
   que é uma dependência de config global, não algo versionado — reforça o
   checkpoint humano da Etapa 3.
3. A relação `hooks -> Claude Code` (interceptação antes de executar) é a
   única linha do diagrama que representa controle/guardrail, e é a coisa
   mais importante que este projeto tem além dos próprios validadores.

**Custo da v2:** mais elementos, exige mais contexto de quem lê pra não se
perder. Para alguém querendo só entender "o que o código faz" (não "como o
agente foi controlado"), a v1 ainda seria suficiente. A escolha do diagrama
certo depende de para quem ele é: v1 serve para descrever o produto, v2
serve para descrever o processo — e o objetivo desta atividade era o
processo.
