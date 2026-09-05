## 1. Testes primeiro

- [x] 1.1 Criar `tests/test_validador_documentos.py` com os cenários de CPF do spec (máscara, sem máscara, dígitos repetidos, dígito adulterado, tamanho inválido, string vazia) e verificar que a suíte falha por `ImportError`, provando que os testes exercitam o módulo ainda inexistente
- [x] 1.2 Acrescentar ao mesmo arquivo os cenários de CNPJ do spec (máscara, sem máscara, todos zerados, dígitos adulterados, tamanho inválido, string vazia) e verificar que continuam falhando pelo mesmo motivo
- [x] 1.3 Acrescentar os cenários do contrato de tipo (`TypeError` para `int` e `None`, retorno `isinstance(..., bool)`) e verificar que a contagem de testes coletados cobre todos os `#### Scenario` do spec

## 2. Núcleo compartilhado

- [x] 2.1 Criar `src/validador_documentos.py` com as quatro constantes de pesos e verificar contra a tabela oficial que `_PESOS_CPF_1` tem 9 pesos, `_PESOS_CPF_2` tem 10, `_PESOS_CNPJ_1` tem 12 e `_PESOS_CNPJ_2` tem 13
- [x] 2.2 Implementar `_limpar` (descarta não dígitos, levanta `TypeError` para entrada não-`str`) e verificar pelos testes de contrato de tipo, que devem passar a partir daqui
- [x] 2.3 Implementar `_todos_digitos_iguais` e `_calcular_digito_verificador` (soma ponderada, módulo 11, resto menor que 2 vira 0) e verificar isoladamente que os dígitos de `529.982.247-25` calculam `2` e `5`

## 3. Validações públicas

- [x] 3.1 Implementar `validar_cpf` (tamanho 11, rejeita repetidos, confere os dois dígitos) e verificar que todos os testes da classe `TestValidarCpf` passam
- [x] 3.2 Implementar `validar_cnpj` (tamanho 14, rejeita repetidos, confere os dois dígitos) e verificar que todos os testes da classe `TestValidarCnpj` passam

## 4. Fechamento

- [x] 4.1 Rodar `python3 -m pytest -q` e verificar que a suíte inteira do repositório passa, incluindo os testes de e-mail preexistentes
- [x] 4.2 Revisar o `git diff` da implementação linha a linha contra as matrizes de pesos oficiais antes de aceitar, e registrar o resultado da revisão em `docs/revisao-diff-f1.md`
- [x] 4.3 Passar pelo checkpoint humano definido em `docs/checkpoint-humano.md` e registrar a decisão antes de abrir o Pull Request
