# Prompts de comparação

Registro dos prompts usados para comparar assistentes de IA no desenvolvimento
de software. Cada entrada descreve a tarefa, o prompt exato enviado e
observações sobre o resultado de cada ferramenta.

## Modelo de entrada

### Tarefa: <nome curto da tarefa>

- **Objetivo:** <o que se espera do assistente>
- **Prompt:**

  ```
  <texto do prompt enviado>
  ```

- **Resultado — Claude Code:** <resumo do que foi produzido>
- **Observações:** <qualidade, autonomia, erros, número de iterações>

## Entradas

### Tarefa 1: Validação de e-mail (Prompt Fraco)

- **Objetivo:** Criar uma função de validação de e-mail básica.
- **Prompt:**
  ```text
  Crie uma função para validar e-mail em Python.
  ```
- **Resultado — Claude Code:** A IA gerou um script extenso utilizando expressões regulares complexas (re) baseadas em especificações HTML5/RFC 5322. Não separou os testes, optando por inserir exemplos de validação soltos no final do próprio arquivo usando um bloco if **name** == "**main**":

- **Observações:** O assistente tentou adivinhar o contexto ausente e gerou uma solução desnecessariamente complexa, acoplada e sem seguir uma organização de pastas.

### Tarefa 2: Validação de e-mail (Prompt Eficaz)

- **Objetivo:** Criar a mesma função aplicando as diretrizes de contexto, restrições claras e validação.
- **Prompt:**

  ```text
  Atue como um desenvolvedor Python sênior. Crie uma nova função de validação de e-mail na pasta src/. O retorno deve ser estritamente booleano. Restrições: não utilize a biblioteca re ou qualquer expressão regular; faça apenas uma validação estrutural simples usando .split('@') para garantir que existe texto de ambos os lados. Validação: gere um arquivo de testes isolado utilizando a biblioteca nativa unittest e salve-o na pasta tests/.
  ```

- **Resultado — Claude Code:** A ferramenta atendeu perfeitamente às restrições. Criou o script de validação (src/validador_email_simples.py) utilizando a lógica de split, sem regex, e gerou autonomamente um arquivo de testes robusto e isolado (tests/test_validador_email_simples.py) que passou em todas as 10 checagens.

- **Observações:** A diferença de produtividade é nítida. O prompt fraco exigiria refatoração manual para extrair os testes e ajustar o uso de bibliotecas. O prompt eficaz garantiu previsibilidade, forçando a IA a entregar a funcionalidade já testada, modularizada e perfeitamente alinhada à arquitetura do projeto na primeira tentativa.
