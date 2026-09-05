## Contexto

Ver `proposal.md`. Restrições do projeto: código de regra de negócio em `src/`, testes em `tests/`, e o README proíbe bibliotecas externas não documentadas. O projeto já tem dois validadores de e-mail. Um deles, `validador_email.py`, é o exemplo de código gerado por prompt fraco, com testes soltos em `if __name__ == "__main__"`, e não serve de referência.

## Objetivos / Nao-objetivos

**Objetivos:**

- Uma única rotina de cálculo dos dígitos verificadores, compartilhada por CPF e CNPJ.
- Comportamento igual ao descrito em `specs/validacao-documentos/spec.md`, testável sem I/O.

**Nao-objetivos:**

- Consultar a Receita Federal para saber se o documento existe. A validação é só aritmética.
- Detectar automaticamente se a entrada é CPF ou CNPJ. Quem chama escolhe a função.
- Formatar ou aplicar máscara na saída.

## Decisoes

**1. Uma função de cálculo parametrizada por lista de pesos, em vez de duas implementações.**
CPF e CNPJ usam o mesmo algoritmo (soma ponderada, módulo 11, resto menor que 2 vira dígito 0) e diferem só nas matrizes de pesos. Extrair `_calcular_digito_verificador(digitos, pesos)` evita repetir a mesma aritmética em quatro lugares. Alternativa descartada: quatro funções explícitas, mais literal, mas com quatro cópias da mesma regra e quatro chances de erro de índice.

**2. Pesos como constantes nomeadas de classe.**
As quatro matrizes ficam lado a lado no topo do módulo, o que permite conferir o diff contra a tabela oficial. Alternativa descartada: gerar os pesos por `range`, mais curto, mas a sequência do CNPJ (`5,4,3,2,9,8,7,6,5,4,3,2`) não é progressão simples e a geração ficaria mais difícil de conferir do que a lista.

**3. `TypeError` para entrada não-`str`, `False` para `str` inválida.**
String malformada é dado de usuário inválido, então retorna `False`. Inteiro passado no lugar de texto é erro de quem chamou, então falha alto. Alternativa descartada: aceitar `int` e converter, porque `int` não preserva zeros à esquerda e a conversão transformaria documento válido em inválido.

**4. `unittest` da biblioteca padrão, executável também por `pytest`.**
Segue a convenção de `tests/test_validador_email_simples.py` e respeita a restrição do README.

**5. Classe com métodos de classe, sem estado de instância.**
Agrupa as constantes e os helpers privados num namespace e deixa claro que `_limpar` e `_calcular_digito_verificador` são internos. Alternativa descartada: funções soltas no módulo, equivalentes em comportamento, mas espalhariam quatro constantes no escopo do módulo.

## Riscos / Compromissos

- **Trocar as matrizes de pesos entre o primeiro e o segundo dígito, ou entre CPF e CNPJ.** O código continua rodando e retorna `False` para documentos válidos, sem erro visível. Mitigação: cada validação tem teste com documento válido conhecido (`529.982.247-25` e `11.222.333/0001-81`), que falha se os pesos estiverem trocados. É o ponto que exige revisão humana do diff.
- **Documentos que passam na aritmética mas não existem na Receita Federal.** Sem mitigação, está declarado como não-objetivo. Quem precisar de existência real deve consultar o serviço oficial.
- **Exigir `str` transfere para quem chama a responsabilidade de converter a entrada.** Aceito, conforme a Decisão 3.
