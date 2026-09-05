# validacao-documentos Specification

## Purpose
Garantir que CPFs e CNPJs aceitos pelo sistema sejam documentos aritmeticamente válidos segundo o algoritmo oficial da Receita Federal, e não apenas cadeias de dígitos com o tamanho certo.

## Requirements

### Requirement: Normalização da entrada

O sistema SHALL aceitar o documento com ou sem máscara e MUST descartar todos os caracteres não numéricos antes de qualquer verificação, de modo que a validação dependa apenas dos dígitos informados.

#### Scenario: CPF válido com máscara

- **GIVEN** um CPF válido escrito com pontuação `"529.982.247-25"`
- **WHEN** a validação de CPF é executada
- **THEN** o resultado é `True`

#### Scenario: CPF válido sem máscara

- **GIVEN** o mesmo CPF escrito apenas com dígitos `"52998224725"`
- **WHEN** a validação de CPF é executada
- **THEN** o resultado é `True`, idêntico ao da forma com máscara

#### Scenario: CNPJ válido com máscara

- **GIVEN** um CNPJ válido escrito com pontuação `"11.222.333/0001-81"`
- **WHEN** a validação de CNPJ é executada
- **THEN** o resultado é `True`

### Requirement: Rejeição de documentos com todos os dígitos iguais

O sistema SHALL rejeitar documentos formados por um único dígito repetido, mesmo quando satisfaçam o cálculo dos dígitos verificadores.

#### Scenario: CPF com todos os dígitos repetidos

- **GIVEN** o CPF `"111.111.111-11"`, que passa no cálculo dos dígitos verificadores
- **WHEN** a validação de CPF é executada
- **THEN** o resultado é `False`

#### Scenario: CNPJ com todos os dígitos zerados

- **GIVEN** o CNPJ `"00.000.000/0000-00"`
- **WHEN** a validação de CNPJ é executada
- **THEN** o resultado é `False`

### Requirement: Conferência dos dígitos verificadores

O sistema SHALL calcular os dois dígitos verificadores a partir dos dígitos base do documento e MUST considerar o documento válido somente quando os dígitos calculados coincidirem com os dois últimos dígitos informados.

#### Scenario: CPF com dígito verificador adulterado

- **GIVEN** o CPF `"529.982.247-26"`, igual a um CPF válido exceto pelo último dígito
- **WHEN** a validação de CPF é executada
- **THEN** o resultado é `False`

#### Scenario: CNPJ com dígitos verificadores adulterados

- **GIVEN** o CNPJ `"12.345.678/0001-99"`
- **WHEN** a validação de CNPJ é executada
- **THEN** o resultado é `False`

### Requirement: Rejeição de documentos com quantidade de dígitos incorreta

O sistema SHALL rejeitar como inválido qualquer documento cuja quantidade de dígitos, após a normalização, seja diferente de 11 para CPF e de 14 para CNPJ.

#### Scenario: CPF incompleto

- **GIVEN** a entrada `"123.456.789"`, com 9 dígitos
- **WHEN** a validação de CPF é executada
- **THEN** o resultado é `False`

#### Scenario: String vazia

- **GIVEN** a entrada `""`
- **WHEN** a validação de CPF ou de CNPJ é executada
- **THEN** o resultado é `False`, sem levantar exceção

### Requirement: Contrato de tipo da entrada

O sistema SHALL retornar estritamente um booleano para entradas do tipo `str` e MUST levantar `TypeError` com mensagem descritiva quando a entrada não for `str`, em vez de retornar `False` silenciosamente.

#### Scenario: Documento informado como número inteiro

- **GIVEN** a entrada `52998224725` como inteiro, e não como texto
- **WHEN** a validação de CPF é executada
- **THEN** um `TypeError` é levantado informando o tipo recebido

#### Scenario: Documento ausente

- **GIVEN** a entrada `None`
- **WHEN** a validação de CPF ou de CNPJ é executada
- **THEN** um `TypeError` é levantado

#### Scenario: Retorno estritamente booleano

- **GIVEN** qualquer entrada do tipo `str`
- **WHEN** a validação é executada e não levanta exceção
- **THEN** o valor retornado é uma instância de `bool`, e não um valor apenas truthy ou falsy
