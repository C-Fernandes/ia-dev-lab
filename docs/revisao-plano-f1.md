# Revisão do plano de tarefas - Funcionalidade 1 (CPF/CNPJ)

Referente à tarefa 8 da Etapa 2: revisar o plano proposto pelo agente, com justificativa.

## Plano original

O primeiro plano, em [`especificacao-cpf-cnpj.md`](especificacao-cpf-cnpj.md), tinha 5 itens:

1. Criar o arquivo de testes unitários.
2. Criar o módulo `src/validador_documentos.py` com a função de limpeza de máscara.
3. Implementar o cálculo dos dígitos verificadores para CPF.
4. Implementar o cálculo dos dígitos verificadores para CNPJ.
5. Executar os testes via `pytest` e ajustar falhas.

## Plano revisado

O plano aplicado é o de [`../openspec/changes/archive/2026-09-04-add-validador-documentos/tasks.md`](../openspec/changes/archive/2026-09-04-add-validador-documentos/tasks.md): 4 grupos, 10 tarefas.

## Alterações e justificativas

**1. Cada tarefa passou a declarar como verificar que terminou.**
No plano original, "implementar o cálculo dos dígitos verificadores para CPF" não dizia o que significa estar pronto. Cada tarefa revisada carrega a verificação junto, por exemplo "verificar que todos os testes da classe `TestValidarCpf` passam". Exigência do próprio schema do OpenSpec.

**2. A tarefa 1 foi dividida em três (1.1, 1.2, 1.3).**
São 13 cenários no total. Dividir por CPF, CNPJ e contrato de tipo deixa visível se algum grupo foi esquecido.

**3. As tarefas 2, 3 e 4 foram reorganizadas em dois grupos.**
O plano original separava CPF e CNPJ, o que levaria a duplicar a aritmética do módulo 11. O plano revisado separa o núcleo compartilhado (grupo 2: pesos, `_limpar`, `_calcular_digito_verificador`) das validações públicas (grupo 3: `validar_cpf`, `validar_cnpj`), conforme a Decisão 1 do `design.md`.

**4. Acrescentada a conferência do tamanho das matrizes de pesos (tarefa 2.1).**
Pesos errados não quebram nada: só fazem documentos válidos retornarem `False`. É o risco listado no `design.md` e a conferência custa pouco.

**5. Acrescentadas as tarefas 4.2 e 4.3 (revisão de diff e checkpoint humano).**
O plano original terminava em "executar os testes". Os testes só cobrem o que foi especificado, então a revisão humana precisa estar no plano.

## Mantido

Escrever os testes antes do código (tarefa 1 do plano original). Fixa o comportamento esperado antes de existir implementação.
