# Escopo da Funcionalidade - SDD (Spec-Driven Development)

## 1. Visão Geral

Este documento define o escopo de duas novas funcionalidades para o projeto `ia-dev-lab`, aplicando os princípios de Spec-Driven Development (SDD). O objetivo é estender os validadores existentes com regras de negócio mais complexas e estruturadas.

## 2. Funcionalidades Escolhidas

### Funcionalidade 1: Validador Avançado de CPF/CNPJ com Dígitos Verificadores

- **Descrição:** Implementação de uma rotina robusta para validação de documentos (CPF e CNPJ), que verifica o formato, rejeita sequências inválidas conhecidas e calcula os dígitos verificadores oficiais.
- **Justificativa (por que é uma boa candidata para SDD):**
  1. A regra é externa ao projeto e fechada: o algoritmo de dígito verificador da Receita Federal não admite interpretação, então a especificação pode ser conferida contra uma fonte oficial em vez de contra a opinião de quem implementa.
  2. O comportamento se decide nos casos de borda, não no caminho feliz: documento com e sem máscara, string vazia, quantidade errada de dígitos, sequência de dígitos repetidos que passa na aritmética mas é inválida por convenção, e entrada que nem sequer é texto.
  3. O erro típico dessa regra é silencioso. Uma matriz de pesos trocada entre o primeiro e o segundo dígito não levanta exceção nenhuma: apenas faz documentos válidos retornarem `False`. Sem cenários de aceite escritos antes, com CPF e CNPJ válidos conhecidos, o defeito atravessa uma suíte verde.
  4. A funcionalidade mexe em mais de um arquivo (`src/validador_documentos.py` e `tests/test_validador_documentos.py`) e precisa respeitar convenções já declaradas no README, como não usar biblioteca externa.

### Funcionalidade 2: Validador de Senha Forte com Políticas Configuráveis

- **Descrição:** Um módulo de validação de senhas que avalia requisitos complexos de segurança (comprimento mínimo, presença de caracteres especiais, números, letras maiúsculas e minúsculas) e retorna um feedback detalhado dos critérios pendentes.
- **Justificativa (por que é uma boa candidata para SDD):**
  1. A regra é definida pelo próprio projeto, e não copiada de uma norma. Isso obriga a decidir por escrito perguntas que o código esconde: o que conta como caractere especial, se letra acentuada é minúscula ou símbolo, se oito espaços formam uma senha de oito caracteres. Nenhuma dessas perguntas aparece ao escrever `if len(senha) < 8`.
  2. A política é configurável, então a mesma senha precisa produzir resultados diferentes sob configurações diferentes. O comportamento tem de ser descrito em termos de política, e não de constante fixa no código, sob pena de cada mudança de exigência virar alteração de implementação.
  3. O valor da funcionalidade está na forma da resposta, não no veredito. Um retorno booleano informa que a senha foi recusada, mas não o que falta nela; especificar antes força a decidir que o resultado carrega a lista completa de pendências, avaliadas todas de uma vez, em vez de uma por tentativa.
