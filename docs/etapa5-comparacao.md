# Etapa 5: Comparação entre OpenSpec e SpecKit

Referente às tarefas 15 e 16.

| | Funcionalidade 1 | Funcionalidade 2 |
|---|---|---|
| Funcionalidade | Validador de CPF/CNPJ | Validador de senha forte |
| Ferramenta | OpenSpec 1.12.0 | SpecKit (github/spec-kit) |
| Artefatos | `openspec/changes/archive/2026-09-04-add-validador-documentos/` e `openspec/specs/validacao-documentos/` | `specs/001-validador-senha-forte/` e `.specify/memory/` |
| Código | `src/validador_documentos.py` | `src/validador_senha.py` |
| Testes | 17 | 17 |

## 1. Artefatos gerados

**OpenSpec:** `proposal.md` (por que e quais capacidades), `specs/validacao-documentos/spec.md` (contrato de comportamento), `design.md` (decisões técnicas) e `tasks.md` (plano).

A ordem é obrigatória. `openspec status` mostra `specs` como `blocked` enquanto `proposal` não existir, e `tasks` bloqueado por `specs` e `design`.

**SpecKit:** `.specify/memory/constitution.md` (princípios do projeto), `spec.md`, `plan.md` e `tasks.md`.

Também oferece `research.md`, `data-model.md`, `contracts/` e `quickstart.md`. Nenhum foi criado: não havia incógnita a pesquisar nem contrato de API. A decisão de não criá-los precisou ser justificada dentro do `plan.md`.

## 2. Diferenças de abordagem

**Escopo do que se escreve.** No OpenSpec, o artefato é um delta (`## ADDED Requirements`) sobre o conjunto de specs existente. Ao rodar `openspec archive`, o delta é promovido para `openspec/specs/` e vira a especificação do projeto. Foi o que se fez ao fim da atividade: a change saiu de `openspec/changes/` para `openspec/changes/archive/2026-09-04-add-validador-documentos/` e os cinco requisitos passaram a viver em `openspec/specs/validacao-documentos/spec.md`, agora independentes da change que os originou. No SpecKit, cada funcionalidade tem uma pasta numerada independente, sem acúmulo entre elas.

**Validação.** `openspec validate --strict` recusa change sem delta, requisito sem cenário e cenário escrito com 3 `#` em vez de 4. Ao traduzir os cabeçalhos para o português, o comando falhou com `No delta sections found`, o que mostrou quais títulos são estruturais. O SpecKit não tem comando equivalente: os templates vêm com marcadores `[NEEDS CLARIFICATION]` e nada impede entregá-los preenchidos pela metade.

**Constituição.** Só o SpecKit tem. É um documento de princípios válido para todas as funcionalidades, e o `plan.md` traz uma tabela onde cada princípio é confrontado com o plano antes da implementação. Foi o que obrigou a justificar por escrito quais artefatos do template não seriam criados.

**Priorização.** A spec do SpecKit exige ordenar as histórias em P1, P2, P3 e dizer como testar cada uma isoladamente. A spec do OpenSpec lista requisitos e cenários sem hierarquia.

## 3. Pontos positivos e negativos

**OpenSpec - positivo:**

- Validação automática, que pegou um erro real durante a atividade.
- Modelo de delta acumula a especificação do sistema em vez de pastas soltas.
- `openspec instructions <artefato> --json` entrega a orientação de cada artefato sob demanda.

**OpenSpec - negativo:**

- Marcadores estruturais precisam ficar em inglês, mesmo com `language: pt-BR` configurado.
- Vocabulário próprio (capability, delta, archive) tem curva de aprendizado.
- A estrutura de quatro artefatos é a mesma para uma função pequena e para um sistema inteiro.

**SpecKit - positivo:**

- A constituição, único mecanismo dos dois que registra princípio de projeto com força de gate.
- Priorização por história, que empurra o desenho para fatias entregáveis.
- Templates ricos, que sugerem seções em que não se pensaria sozinho.

**SpecKit - negativo:**

- Sem validação. A disciplina fica toda por conta de quem escreve.
- Instala 10 skills e uma árvore `.specify/` inteira para uma funcionalidade pequena.
- Os templates assumem um projeto grande, então parte do trabalho é decidir o que apagar.
- Cria uma branch por funcionalidade por padrão, o que atrapalha quem já tem um fluxo de branch próprio.

## 4. Comparação do código gerado

**Arquitetura.** As duas ferramentas levaram a desenhos diferentes:

- CPF/CNPJ: classe com métodos de classe, retorno `bool`. A spec do OpenSpec descrevia contrato de entrada e saída.
- Senha: duas dataclasses imutáveis (`PoliticaSenha`, `ResultadoValidacao`) mais uma classe de serviço, retorno com a lista de pendências.

A diferença veio da priorização do SpecKit. A história P1 foi escrita como "saber por que a senha foi recusada", não como "validar a senha". Com o valor declarado assim, o retorno booleano fica insuficiente antes de existir código. Uma spec que dissesse apenas "validar senhas segundo critérios configuráveis" provavelmente teria gerado outro `-> bool`.

**Atendimento aos requisitos.** As duas implementações atendem ao especificado: 44 testes no total, todos passando. Nos dois casos os testes foram commitados antes do código e falharam por `ImportError` naquele ponto do histórico.

**O que nenhuma das duas pegou.** O defeito real da atividade (o bloco de demonstração do validador de documentos escolhendo a validação por `len(e) <= 14`) não foi pego por ferramenta nenhuma. Estava fora da spec, logo fora dos testes, e a suíte permaneceu verde. Quem pegou foi a revisão humana do diff, em [`revisao-diff-f1.md`](revisao-diff-f1.md).

## 5. O que foi feito e o que se aprendeu

O processo da Etapa 2 foi repetido inteiro na segunda funcionalidade, com outra ferramenta: constituição, especificação, plano, revisão do plano, testes antes do código, implementação, revisão de diff e checkpoint. Os artefatos ficaram em `specs/001-validador-senha-forte/` e em `.specify/memory/`, e o código em `src/validador_senha.py`, com 17 testes.

Três aprendizados saíram da comparação:

1. **A forma da spec determina a forma do código.** A mesma pessoa, no mesmo dia, produziu um validador que devolve `bool` e outro que devolve um objeto com lista de pendências. A diferença não foi de gosto: a spec do SpecKit obriga a escrever a história em ordem de prioridade, e escrever "saber por que a senha foi recusada" como P1 torna o retorno booleano insuficiente antes de existir código.

2. **Validação automática pega o que a leitura deixa passar.** O `openspec validate --strict` acusou um erro que passou despercebido na revisão manual, quando os cabeçalhos foram traduzidos. O SpecKit aceitaria o mesmo arquivo quebrado sem reclamar. Ferramenta que só oferece template transfere toda a disciplina para quem escreve.

3. **Nenhuma das duas substitui a revisão humana.** Os dois defeitos encontrados na atividade passaram por ferramenta, por spec e por suíte verde. Um estava fora da especificação (o bloco de demonstração do CPF/CNPJ), o outro estava dentro do plano mas fora dos testes (as anotações de tipo do validador de senha). Especificar antes reduz o espaço de erro; não elimina o ponto cego.

## 6. Conclusão

Para este projeto, OpenSpec no dia a dia: a validação automática vale mais que os templates, e a especificação acumulada em `openspec/specs/` é um resultado que a pasta por funcionalidade do SpecKit não produz.

Do SpecKit vale manter a constituição, que ficou em `.specify/memory/constitution.md` e passou a valer para o repositório inteiro, inclusive para a funcionalidade especificada com a outra ferramenta.
