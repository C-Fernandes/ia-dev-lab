# Checkpoint humano obrigatório

Referente às tarefas 13 e 14 da Etapa 4.

## Checkpoint definido

Nenhum código gerado por agente entra na branch `main` sem revisão humana do diff completo. O ponto de parada é antes do merge do Pull Request.

O agente pode especificar, escrever os testes, implementar, rodar a suíte e abrir o PR. Não pode fechar o PR.

## Justificativa da escolha do ponto

- É o último ponto em que desfazer é barato. Antes do merge, basta `git reset` numa branch de uso individual. Depois, o código já é base do que vem em seguida.
- É o ponto em que o diff está completo. Revisar commit a commit fragmenta a análise, e cada pedaço isolado parece razoável.

## Papel humano assumido

Revisora responsável pela regra de negócio.

Não é revisão de estilo nem de convenção, que ficam por conta dos testes. A pergunta respondida é: o comportamento implementado é o que a especificação pediu, e o que ficou fora da especificação também está correto?

A funcionalidade implementa regra externa ao projeto (algoritmo da Receita Federal). O agente não consegue conferir as matrizes de pesos contra a fonte oficial, só reproduz o que aprendeu. Um erro ali é silencioso: não quebra nada, apenas rejeita documentos válidos.

## Simulação do checkpoint

**Momento:** depois da implementação completa, com 27 testes passando e `openspec validate --strict` limpo, antes de abrir o Pull Request.

**Itens revisados:**

1. As quatro matrizes de pesos, conferidas contra a tabela oficial: 9 pesos para o primeiro dígito do CPF, 10 para o segundo, 12 e 13 para o CNPJ. Corretas.
2. A regra do módulo 11 (`resto < 2` resulta em dígito `0`). Correta.
3. O contrato de tipo: `TypeError` para entrada não-`str`, `False` para `str` inválida. Conforme o spec.
4. O bloco `if __name__ == "__main__"`, que não tem cobertura de teste.

**Decisão: editar antes de aprovar.**

Os itens 1 a 3 passaram. O item 4 não: o bloco escolhia a validação por `len(e) <= 14`, enviando um CNPJ sem máscara para `validar_cpf`. Detalhes em [`revisao-diff-f1.md`](revisao-diff-f1.md).

A correção foi feita antes do merge, em commit próprio e não em amend, para que o histórico mostre que o checkpoint pegou o problema. Aprovação concedida depois disso.

## Segunda simulação (Funcionalidade 2)

**Momento:** depois da implementação do validador de senha, com 44 testes passando no repositório inteiro, antes do Pull Request.

**Itens revisados:**

1. Os cinco critérios de composição, conferidos contra os requisitos FR-001 a FR-010 do spec. Corretos.
2. A definição de caractere especial por exclusão (`isalnum()` e `isspace()`), conferida contra os casos de borda do acento e dos espaços. Correta.
3. As assinaturas de tipo, conferidas contra o `plan.md`.

**Decisão: editar antes de aprovar.**

Os itens 1 e 2 passaram. O item 3 não: a anotação `politica: PoliticaSenha = None` contradiz o próprio valor padrão, e `pendencias: tuple` perdeu a precisão `tuple[str, ...]` que o plano definia. Detalhes em [`revisao-diff-f2.md`](revisao-diff-f2.md). Correção em commit próprio, antes do merge.

## Conclusão

O erro estava fora da spec, não dentro dela. Os testes cobriam tudo o que a especificação descrevia e continuaram passando durante o problema. Especificar antes reduz o espaço de erro, mas o código que ninguém especificou também é o código que ninguém testa. Por isso o checkpoint permanece obrigatório.
