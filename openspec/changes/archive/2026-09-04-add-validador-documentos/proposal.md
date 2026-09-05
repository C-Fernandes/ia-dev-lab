## Por que

O projeto valida e-mails, mas não valida documentos brasileiros. Cadastros que aceitam CPF ou CNPJ sem conferir o dígito verificador deixam entrar dados inválidos que parecem válidos, como `111.111.111-11` ou documentos com um dígito digitado errado. A regra é padronizada pela Receita Federal e tem vários casos de borda, o que a torna um bom caso para especificar antes de implementar.

## O que muda

- Validação de CPF com cálculo dos dois dígitos verificadores oficiais.
- Validação de CNPJ com cálculo dos dois dígitos verificadores oficiais, com matrizes de pesos diferentes das de CPF.
- Normalização da entrada: aceitar documento com ou sem máscara, removendo caracteres não numéricos antes de validar.
- Rejeição de sequências com todos os dígitos iguais, que passam no cálculo mas são inválidas por convenção.
- Entrada que não seja `str` levanta `TypeError` descritivo, em vez de retornar `False`.
- Nenhuma mudança em código existente e nenhuma quebra de compatibilidade.

## Capacidades

### Novas capacidades

- `validacao-documentos`: validação de CPF e CNPJ brasileiros, incluindo normalização de máscara, rejeição de dígitos repetidos, conferência dos dígitos verificadores e contrato de tipo da entrada.

### Capacidades modificadas

Nenhuma.

## Impacto

- Código novo: `src/validador_documentos.py`.
- Testes novos: `tests/test_validador_documentos.py`.
- Dependências: nenhuma. Só biblioteca padrão do Python, conforme a convenção do README.
- Sem impacto em `src/validador_email.py`, `src/validador_email_simples.py` ou `src/hello.py`.
