# Relatório Final - De Spec a Código (Aula 4)

**Repositório:** [C-Fernandes/ia-dev-lab](https://github.com/C-Fernandes/ia-dev-lab)

## 1. Funcionalidades escolhidas e por que são bom caso para SDD

Foram implementadas duas funcionalidades novas: um **validador de CPF/CNPJ** com os dígitos verificadores oficiais, e um **validador de senha forte** com política configurável, que retorna a lista de critérios pendentes.

As duas são boas candidatas por motivos opostos. O validador de documentos tem regra fechada e externa ao projeto: o algoritmo da Receita Federal não admite interpretação, mas tem muitos casos de borda (máscara, sequências repetidas, tamanho errado, tipo errado) que se perdem quando se começa pelo código. O validador de senha tem a regra definida pelo próprio projeto, e quase todo o valor está no comportamento de fronteira: o que conta como caractere especial, se acento é letra, se oito espaços formam uma senha de oito caracteres. Essas perguntas não aparecem escrevendo `if len(senha) < 8`; aparecem escrevendo os cenários de aceite antes.

## 2. Abordagens de especificação e comportamento na prática

A funcionalidade 1 foi especificada com **OpenSpec** e a 2 com **SpecKit**, para comparação. Registro completo em [`docs/etapa5-comparacao.md`](docs/etapa5-comparacao.md).

O OpenSpec valida o que se escreve: `openspec validate --strict` recusa change sem delta e requisito sem cenário. Pegou um erro real durante a atividade — ao traduzir os cabeçalhos dos artefatos para o português, o comando falhou com `No delta sections found`, mostrando que parte dos títulos é estrutura consumida por parser, e não texto livre. O SpecKit não tem validação equivalente, e nada impede entregar a spec com os marcadores `[NEEDS CLARIFICATION]` intactos. Em compensação, trouxe a constituição do projeto, com uma tabela no plano que obriga a confrontar cada princípio antes de implementar.

A priorização por história do SpecKit mudou o código gerado. Com a história P1 escrita como "saber por que a senha foi recusada", em vez de "validar a senha", o retorno booleano ficou insuficiente antes de existir código. O objeto de resultado com a lista de pendências virou consequência da spec, não escolha de implementação.

## 3. Dificuldade enfrentada

A dificuldade foi entender onde termina a especificação, e ela só ficou clara porque a atividade obriga a revisar o diff.

A implementação do validador de documentos passou nos 17 testes, atendeu a todos os requisitos e passou no `openspec validate --strict`. Mesmo assim tinha um defeito: o bloco de demonstração escolhia entre CPF e CNPJ por `len(e) <= 14`, e um CNPJ sem máscara tem exatamente 14 caracteres, então seria enviado para a validação de CPF e recusado. Nenhum teste falhou, porque aquele bloco não faz parte do contrato descrito no spec.

O erro estava fora da especificação, não dentro dela. Especificar antes reduz o espaço de erro, mas o código que ninguém especificou continua sem teste. Foi isso que justificou manter o checkpoint humano antes da `main` ([`docs/checkpoint-humano.md`](docs/checkpoint-humano.md)) em vez de confiar só na suíte verde.
