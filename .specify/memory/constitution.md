# ia-dev-lab Constitution

## Princípios Fundamentais

### I. Especificação antes do código

Nenhuma funcionalidade nova começa pela implementação. O comportamento esperado é escrito primeiro, como user story, requisitos e cenários de aceite. Especificação escrita depois do código é documentação, não especificação.

### II. Test-First (NÃO NEGOCIÁVEL)

Os testes derivam dos cenários de aceite e são escritos antes da implementação. A suíte deve falhar antes de existir o módulo. Cada cenário da spec corresponde a pelo menos um teste.

### III. Sem dependências externas não documentadas

O projeto usa a biblioteca padrão do Python. Qualquer dependência nova exige justificativa registrada antes de ser adicionada, conforme a convenção já declarada no README. Testes usam `unittest`.

### IV. Checkpoint humano antes da `main`

Código gerado por agente de IA não entra na branch `main` sem revisão humana do diff completo. Testes verdes não substituem a revisão, porque cobrem apenas o que foi especificado.

### V. Histórico de commits como registro do processo

Commits são pequenos e seguem a ordem do processo: spec, testes, implementação, correção. Um commit único apaga o registro de como a decisão foi tomada. Correções feitas em revisão vão em commit próprio, nunca em amend.

## Restrições Técnicas

- Código de regra de negócio em `src/`, testes em `tests/`.
- Retornos de validação são estritamente booleanos; erro de tipo do chamador levanta exceção em vez de retornar `False` silenciosamente.
- Regras vindas de fonte externa (Receita Federal, políticas de segurança) exigem conferência humana contra a fonte oficial. O agente reproduz o que aprendeu, não consulta a norma.

## Fluxo de Desenvolvimento

1. Especificar a funcionalidade com uma ferramenta de SDD (OpenSpec ou SpecKit).
2. Revisar o plano de tarefas proposto pelo agente antes de executá-lo, registrando as edições.
3. Escrever os testes; verificar que falham.
4. Implementar; verificar que a suíte passa.
5. Revisar o diff e registrar o achado.
6. Passar pelo checkpoint humano; só então abrir e integrar o Pull Request.

## Governança

Esta constituição prevalece sobre preferências pontuais de implementação. Toda revisão de Pull Request verifica a conformidade com os princípios acima. Emendas exigem registro em commit próprio com a justificativa da mudança.

**Versão**: 1.0.0 | **Ratificada em**: 2026-09-04 | **Última emenda**: 2026-09-04
