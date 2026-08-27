# 1. Escolha da ferramenta de IA

- Status: Aceito
- Data: 2026-08-27

## Contexto

O projeto tem como objetivo avaliar a eficácia de assistentes de IA no
desenvolvimento de software. Para conduzir os experimentos de forma consistente,
é necessário definir qual ferramenta de assistência por IA será usada como base
das análises.

## Decisão

A ferramenta escolhida foi o Claude Code.

A escolha atende aos critérios definidos:

- **Integração com o fluxo de linha de comando e com o editor:** o Claude Code
  roda de forma fluida no terminal integrado do VS Code.
- **Capacidade de ler e editar múltiplos arquivos do repositório:** opera de
  forma autônoma, lendo e editando o contexto do repositório sem intervenção
  manual arquivo a arquivo.
- **Qualidade das respostas em tarefas de refatoração, testes e documentação.**
- **Custo e limites de uso.**
- **Transparência sobre o que foi alterado.**

## Consequências

- Os experimentos seguintes devem usar a ferramenta escolhida aqui.
- Mudança de ferramenta exige uma nova ADR que substitua esta.
