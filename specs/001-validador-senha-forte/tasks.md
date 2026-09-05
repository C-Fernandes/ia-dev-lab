---
description: "Plano de tarefas do validador de senha forte"
---

# Tarefas: Validador de Senha Forte com Políticas Configuráveis

**Entrada**: Documentos de desenho em `/specs/001-validador-senha-forte/`

**Pré-requisitos**: [plan.md](./plan.md) e [spec.md](./spec.md)

**Testes**: incluídos. O princípio II da constituição do projeto torna os testes obrigatórios e anteriores à implementação.

**Organização**: agrupadas por história de usuário, na ordem de prioridade da spec, de modo que cada história possa ser implementada e verificada de forma independente.

## Formato: `[ID] [P?] [História] Descrição`

- **[P]**: pode rodar em paralelo (arquivos diferentes, sem dependência entre si)
- **[História]**: US1, US2 ou US3, conforme a spec

## Fase 1: Testes (obrigatoriamente antes da implementação)

**Objetivo**: fixar o comportamento esperado antes de existir código que o justifique.

- [x] T001 [US1] Criar `tests/test_validador_senha.py` com os três cenários de aceite da História 1 (senha `"abc"` com quatro pendências, `"Abc@1234"` válida, `"abcdefgh"` sem pendência de comprimento) e verificar que a suíte falha por `ImportError`
- [x] T002 [US2] Acrescentar os três cenários de aceite da História 2 (comprimento mínimo 12, política sem caractere especial, política sem critérios) e verificar que continuam falhando pelo mesmo motivo
- [x] T003 [US3] Acrescentar os três cenários de aceite da História 3 (`TypeError` para `int` e `None`, `ValueError` para comprimento mínimo negativo) e verificar que continuam falhando pelo mesmo motivo
- [x] T004 Acrescentar os seis casos de borda da spec (senha vazia, só espaços, exatamente no mínimo, com acento, muito longa, critério satisfeito duas vezes) e verificar que o total de testes coletados cobre todos os cenários e casos de borda especificados

## Fase 2: Implementação

**Objetivo**: fazer a suíte passar, sem antecipar nada que a spec não peça.

- [x] T005 Criar `src/validador_senha.py` com a dataclass congelada `PoliticaSenha` (comprimento mínimo e quatro sinalizadores de composição) e o `__post_init__` que levanta `ValueError` para comprimento negativo, verificando pelos testes de T003
- [x] T006 [P] Implementar a dataclass `ResultadoValidacao` com `pendencias` imutável e `valida` derivada de a lista estar vazia, verificando que nenhum caminho consegue produzir resultado válido com pendências
- [x] T007 Implementar a checagem de comprimento mínimo, com a mensagem interpolando o valor exigido pela política, verificando pelos cenários de T001 e do comprimento 12 em T002
- [x] T008 Implementar as checagens de maiúscula, minúscula e dígito, verificando pelos cenários da História 1
- [x] T009 Implementar a checagem de caractere especial por exclusão (não é `isalnum()` nem `isspace()`), verificando pelos casos de borda do acento e da senha só de espaços em T004
- [x] T010 Implementar a função pública de validação, que levanta `TypeError` para entrada não-`str` e avalia todos os critérios sem interromper na primeira falha, verificando que os cenários de T003 passam e que uma senha com três violações devolve três pendências
- [x] T011 [P] Adicionar a política padrão de 8 caracteres com os quatro critérios ativos, verificando que a validação funciona sem configuração explícita

## Fase 3: Verificação

- [x] T012 Rodar `python3 -m pytest -q` e verificar que a suíte inteira do repositório passa, incluindo os testes de e-mail e de CPF/CNPJ

## Fase 4: Revisão

- [x] T013 Revisar o `git diff` da implementação antes de aceitar e registrar o achado
- [x] T014 Passar pelo checkpoint humano de `docs/checkpoint-humano.md` antes de abrir o Pull Request

## Dependências

- Fase 1 inteira antes da Fase 2: a suíte precisa estar vermelha antes de existir implementação.
- T005 antes de T007 a T011: todas dependem de a política existir.
- T006 pode ser feita em paralelo a T005, arquivo mesmo mas classes independentes.
- T012 depois de toda a Fase 2.
