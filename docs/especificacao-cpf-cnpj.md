# Especificação: Validador Avançado de CPF/CNPJ

## 1. User Story (Prompt Inicial)

Como desenvolvedor backend do sistema, eu quero uma função robusta em Python para validar números de CPF e CNPJ, de modo que o sistema consiga verificar o formato textual, rejeitar sequências de dígitos repetidos e calcular corretamente os dígitos verificadores oficiais, garantindo a integridade dos dados cadastrais.

## 2. Requisitos Funcionais (PRD)

- **RF01:** A função deve aceitar strings contendo números de CPF ou CNPJ com ou sem formatação (pontos, traços e barras).
- **RF02:** A função deve remover todos os caracteres não numéricos antes de realizar a validação.
- **RF03:** A função deve rejeitar CPFs/CNPJs que possuam todos os dígitos iguais (ex: `111.111.111-11` ou `00.000.000/0000-00`).
- **RF04:** A função deve calcular e validar o primeiro e o segundo dígitos verificadores de acordo com o algoritmo oficial da Receita Federal.
- **RF05:** A função deve retornar um valor booleano (`True` se válido, `False` se inválido) ou lançar exceções descritivas caso o tipo de dado passado seja inválido.

## 3. Critérios de Aceite (Given/When/Then)

### Cenário 1: Validação de CPF com formato válido

- **Given** que o usuário informa um CPF válido formatado (`"123.456.789-09"` - _exemplo ilustrativo_),
- **When** a função de validação de CPF é executada,
- **Then** o retorno deve ser `True`.

### Cenário 2: Rejeição de CPF com dígitos repetidos (Caso de Borda)

- **Given** que o usuário informa um CPF com todos os dígitos repetidos (`"111.111.111-11"`),
- **When** a função de validação de CPF é executada,
- **Then** o retorno deve ser `False`.

### Cenário 3: Validação de CNPJ com dígitos verificadores incorretos

- **Given** que o usuário informa um CNPJ com os dígitos verificadores adulterados (`"12.345.678/0001-99"`),
- **When** a função de validação de CNPJ é executada,
- **Then** o retorno deve ser `False`.

## 4. Plano de Tarefas (TO-DO)

1. Criar o arquivo de testes unitários `tests/test_validador_documentos.py` contemplando os cenários de aceite e casos de borda.
2. Criar o módulo `src/validador_documentos.py` contendo a função de limpeza de máscara (remediação de caracteres especiais).
3. Implementar a lógica de cálculo dos dígitos verificadores para CPF.
4. Implementar a lógica de cálculo dos dígitos verificadores para CNPJ.
5. Executar os testes via `pytest` para validar a implementação inicial e ajustar eventuais falhas.
