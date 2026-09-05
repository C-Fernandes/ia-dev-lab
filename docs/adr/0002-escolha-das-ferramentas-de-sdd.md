# 2. Escolha das ferramentas de Spec-Driven Development

- Status: Aceito
- Data: 2026-09-04

## Contexto

O projeto passou a especificar funcionalidades antes de implementá-las. Era preciso decidir com que ferramenta escrever essas especificações, entre OpenSpec, SpecKit, Traycer.ai ou Markdown manual.

A ferramenta define quais artefatos existem, em que ordem podem ser escritos e se há verificação do que foi escrito.

## Decisão

Foram adotadas duas ferramentas, uma por funcionalidade, para compará-las em uso real.

**OpenSpec 1.12.0** para o validador de CPF/CNPJ:

- É a única opção com validação automática. `openspec validate --strict` recusa change sem delta, requisito sem cenário e cenário com o número errado de `#`.
- O modelo de delta acumula a especificação do sistema em `openspec/specs/`.
- Roda por CLI, sem conta em serviço externo.

**SpecKit (github/spec-kit)** para o validador de senha forte:

- Obriga a priorizar as histórias de usuário e a dizer como cada uma é testável isoladamente.
- Traz a constituição do projeto, que nenhuma das outras opções tem.
- Também roda localmente, por scripts e templates.

Descartados:

- **Traycer.ai:** exige conta em serviço externo.
- **Markdown manual:** a tarefa 15 pede outra ferramenta, e duas abordagens manuais não seriam comparáveis entre si.

## Consequências

- Os artefatos ficam em dois lugares: `openspec/changes/` para a funcionalidade 1 e `specs/001-*/` para a funcionalidade 2.
- Os marcadores estruturais do OpenSpec (`## ADDED Requirements`, `### Requirement:`, `#### Scenario:`, `SHALL`/`MUST`) permanecem em inglês, porque o parser os consome. A spec fica bilíngue mesmo com `language: pt-BR` no `config.yaml`.
- A constituição vinda do SpecKit vale para o repositório inteiro, inclusive para a funcionalidade especificada com OpenSpec.
- Comparação completa em [`../etapa5-comparacao.md`](../etapa5-comparacao.md).
- Troca de ferramenta exige nova ADR que substitua esta, como definido na [ADR 0001](0001-escolha-da-ferramenta-de-ia.md).
