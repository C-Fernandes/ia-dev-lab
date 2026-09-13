# Etapa 1 — Comparação entre modos de autonomia

## Tarefas comparadas

Duas tarefas de mesmo porte (validador estrutural + testes unittest, seguindo o
padrão de `src/validador_email_simples.py`), uma em cada modo:

- **Tarefa A — plan mode**: `src/validador_placa.py` (placa de veículo, formato
  antigo e Mercosul) + `tests/test_validador_placa.py`.
- **Tarefa B — execução direta (auto-accept)**: `src/validador_cep.py` (CEP) +
  `tests/test_validador_cep.py`.

## Registro

| Critério | Tarefa A (plan mode) | Tarefa B (direto) |
|---|---|---|
| Tempo até plano/1º código | Exploração do padrão existente + escrita do plano + espera de aprovação antes de qualquer edição | Nenhuma etapa intermediária — implementação já começa na primeira resposta |
| Tempo de implementação em si | ~20s (código+teste+rodar pytest) | ~17s (código+teste+rodar pytest) |
| Overhead do modo | Sim: 1 rodada de leitura de arquivos existentes, 1 arquivo de plano escrito, 1 aprovação explícita antes de codar | Nenhum |
| Sensação de controle | Alta — decisão de formato (antigo vs. Mercosul), estrutura dos testes e escopo ficaram visíveis e aprováveis *antes* de qualquer arquivo ser tocado | Média — só é possível avaliar depois que o código já existe; correção vira "pedir para editar de novo" em vez de "recusar antes de começar" |
| Risco percebido | Baixo — qualquer engano de escopo (ex.: tentar reusar CPF já implementado em outra branch) é pego na fase de plano, sem nenhum arquivo criado | Médio — o mesmo tipo de engano só apareceria depois de arquivos já escritos e commitados, exigindo reverter |

## Conclusão

Para tarefas pequenas e bem conhecidas (um validador seguindo um padrão já
existente no repo), o custo de tempo do plan mode foi baixo e não dominou o
tempo total. O ganho real não foi velocidade, foi **controle antes do fato**:
na Etapa 1 o CPF quase foi duplicado (já existia em `feature/sdd-validadores`)
e isso só foi percebido porque o processo permitiu checar branches antes de
comitar código novo — no fluxo direto, esse tipo de checagem tende a ser
pulado justamente pela falta de uma pausa estrutural para revisão.

Uso recomendado: plan mode quando há mais de uma decisão de escopo possível
ou risco de retrabalho (duplicar algo que já existe, mexer em contrato
usado por outro módulo); execução direta para tarefas mecânicas e isoladas
onde o escopo já está 100% claro.
