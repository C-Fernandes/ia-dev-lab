# Registro de revisão de diff - Funcionalidade 1 (CPF/CNPJ)

Referente à tarefa 12 da Etapa 3.

## Diff revisado

Commit `feat: adiciona validador de CPF e CNPJ com dígitos verificadores`, arquivo `src/validador_documentos.py`.

## Problema encontrado

O bloco de demonstração escolhia a validação pelo comprimento da string:

```python
metodo = ValidadorDocumentos.validar_cpf if len(e) <= 14 else ValidadorDocumentos.validar_cnpj
```

Um CNPJ sem máscara tem exatamente 14 caracteres (`"11222333000181"`). Como `14 <= 14`, ele seria enviado para `validar_cpf`, que rejeita por tamanho e retorna `False` para um CNPJ válido.

O limiar funcionava por acaso nos exemplos da lista, todos com máscara: `"11.222.333/0001-81"` tem 18 caracteres.

## Por que os testes não pegariam

Os 27 testes passam, antes e depois de encontrado o problema. Eles chamam `validar_cpf` e `validar_cnpj` diretamente, que é o contrato descrito no spec. O bloco `if __name__ == "__main__"` não é importado por nenhum teste e não faz parte desse contrato.

## Observação

O mesmo padrão já tinha sido criticado neste projeto. Em [`prompts-comparacao.md`](prompts-comparacao.md), a resposta ao prompt fraco foi criticada por "inserir exemplos de validação soltos no final do próprio arquivo". O módulo novo repetiu isso, mesmo tendo sido gerado a partir de uma spec completa.

## Encaminhamento

Levado ao checkpoint humano ([`checkpoint-humano.md`](checkpoint-humano.md)). Decisão: editar antes de aprovar.
