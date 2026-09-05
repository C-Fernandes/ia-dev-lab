# Revisão do plano de tarefas - Funcionalidade 2 (Senha Forte)

Referente à tarefa 8 da Etapa 2, repetida na Etapa 5.

## O que o SpecKit propôs

O SpecKit entrega um template de tarefas já preenchido (`.specify/templates/tasks-template.md`), com tarefas de exemplo que o próprio template manda descartar. A estrutura em volta delas é a proposta da ferramenta:

- Fase 1 de Setup, com inicialização do projeto e estrutura básica.
- Fases seguintes agrupadas por história de usuário, com testes e implementação juntos em cada história.
- Marcadores `[P]` para tarefas paralelizáveis.
- Testes declarados como opcionais: "Tests are OPTIONAL - only include them if explicitly requested in the feature specification".

## Plano revisado

O plano aplicado é o de [`../specs/001-validador-senha-forte/tasks.md`](../specs/001-validador-senha-forte/tasks.md).

## Alterações e justificativas

**1. Testes deixaram de ser opcionais e viraram a Fase 1 inteira.**
O template trata teste como item negociável. O princípio II da [constituição do projeto](../.specify/memory/constitution.md) o trata como obrigatório e anterior à implementação. Onde a ferramenta e a constituição discordam, prevalece a constituição, que é um artefato do próprio SpecKit.

**2. A Fase 1 de Setup foi removida.**
Não há o que inicializar. O repositório existe, `src/` e `tests/` existem, e a funcionalidade usa só a biblioteca padrão. Manter a fase geraria tarefas para trabalho já feito.

**3. O agrupamento por história foi mantido só nos testes.**
O template sugere fatiar por história de ponta a ponta, com testes e implementação de cada uma. Isso quebraria o princípio II: a implementação da US1 começaria com os testes da US2 e US3 ainda não escritos. A solução foi manter a etiqueta `[US1]`, `[US2]` ou `[US3]` em cada tarefa de teste, sem fatiar a execução.

**4. Acrescentadas as Fases 3 e 4.**
Verificação da suíte completa (T012) e revisão de diff mais checkpoint humano (T013, T014). O template termina na implementação. As duas fases correspondem às Etapas 3 e 4 da atividade e ao princípio IV da constituição.

**5. Os marcadores `[P]` foram reduzidos a dois.**
Quase todas as tarefas tocam o mesmo arquivo e dependem da política existir. Sobraram `[P]` em T006 e T011, que de fato não dependem uma da outra.

## Comparação com a revisão da Funcionalidade 1

- **F1 (OpenSpec):** a revisão foi de acréscimo. A ferramenta pedia tarefas, mas não pedia critério de verificação.
- **F2 (SpecKit):** a revisão foi de remoção. O template já exige caminho de arquivo e descrição precisa, mas oferece mais fases do que o caso precisa.

Nos dois casos, o plano cru não estava pronto para executar.
