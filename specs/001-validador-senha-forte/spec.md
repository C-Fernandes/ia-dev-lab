# Especificação da Funcionalidade: Validador de Senha Forte com Políticas Configuráveis

**Branch da funcionalidade**: `001-validador-senha-forte`

**Criada em**: 2026-09-04

**Situação**: Rascunho

**Entrada**: Descrição do usuário: "Validador de senha forte com politicas configuraveis"

## Cenários de Uso e Testes *(obrigatório)*

### História de usuário 1 - Saber por que a senha foi recusada (Prioridade: P1)

Como pessoa criando uma conta, quero receber a lista completa do que falta na minha senha, e não apenas "senha fraca". Sem isso, cada tentativa revela um problema por vez e o cadastro exige várias rodadas.

**Por que esta prioridade**: É o motivo de a funcionalidade existir. Um validador que só devolve `True`/`False` não resolve o problema; o valor está na lista de pendências.

**Teste independente**: Submeter uma senha que viola três critérios ao mesmo tempo e verificar que as três pendências vêm juntas, em uma única resposta.

**Cenários de aceite**:

1. **Given** a política padrão e a senha `"abc"`, **When** a validação é executada, **Then** o resultado é inválido e as pendências listam comprimento mínimo, letra maiúscula, dígito e caractere especial — todas de uma vez.
2. **Given** a política padrão e a senha `"Abc@1234"`, **When** a validação é executada, **Then** o resultado é válido e a lista de pendências está vazia.
3. **Given** a política padrão e a senha `"abcdefgh"`, **When** a validação é executada, **Then** o resultado é inválido e as pendências citam letra maiúscula, dígito e caractere especial, mas **não** citam comprimento, que já foi atendido.

---

### História de usuário 2 - Ajustar a política sem reescrever o validador (Prioridade: P2)

Como pessoa responsável pela segurança do sistema, quero configurar quais critérios valem e qual o comprimento mínimo. A política muda por ambiente e por exigência de auditoria: o ambiente de testes não precisa do mesmo rigor do cadastro público.

**Por que esta prioridade**: Sem isto, cada mudança de política vira alteração de código. O escopo pede um validador configurável.

**Teste independente**: Validar a mesma senha sob duas políticas diferentes e verificar que os resultados divergem conforme a configuração, sem nenhuma alteração de código.

**Cenários de aceite**:

1. **Given** uma política que exige 12 caracteres e a senha `"Abc@1234"`, com 8, **When** a validação é executada, **Then** o resultado é inválido e a pendência de comprimento cita o mínimo exigido de 12.
2. **Given** uma política que dispensa caractere especial e a senha `"Abcd1234"`, **When** a validação é executada, **Then** o resultado é válido, ainda que a mesma senha fosse inválida na política padrão.
3. **Given** uma política sem nenhum critério ativo e comprimento mínimo 1, **When** qualquer senha não vazia é validada, **Then** o resultado é válido.

---

### História de usuário 3 - Falhar alto quando o uso está errado (Prioridade: P3)

Como pessoa desenvolvendo a integração, quero que o validador recuse entradas do tipo errado com erro explícito, em vez de devolver "senha inválida" e esconder um erro que está no código de quem chamou.

**Por que esta prioridade**: Não afeta o usuário final, mas evita bug que se disfarça de comportamento normal. Mesma decisão já tomada na validação de CPF/CNPJ.

**Teste independente**: Passar um valor não textual e verificar que a exceção é levantada em vez de um resultado inválido.

**Cenários de aceite**:

1. **Given** a entrada `12345678` como número inteiro, **When** a validação é executada, **Then** um `TypeError` é levantado informando o tipo recebido.
2. **Given** a entrada `None`, **When** a validação é executada, **Then** um `TypeError` é levantado.
3. **Given** uma política configurada com comprimento mínimo negativo, **When** a política é criada, **Then** um `ValueError` é levantado, porque nenhuma senha poderia violá-la e a configuração é claramente um engano.

---

### Casos de borda

- **Senha vazia (`""`)**: inválida, com a pendência de comprimento reportada. Não levanta exceção, porque string vazia é entrada de usuário válida.
- **Senha só de espaços (`"        "`)**: atende ao comprimento, mas a nenhum critério de composição. O espaço não conta como caractere especial.
- **Senha exatamente no comprimento mínimo**: válida. O critério é "pelo menos N", não "mais que N".
- **Caracteres acentuados (`"Senhá@123"`)**: `á` conta como letra minúscula, não como caractere especial.
- **Senha muito longa (acima de 200 caracteres)**: válida, se atender aos critérios. O validador não impõe limite superior.
- **Critério satisfeito mais de uma vez**: uma senha com três dígitos satisfaz o critério de dígito uma vez só. As pendências não se repetem.

## Requisitos *(obrigatório)*

### Requisitos funcionais

- **FR-001**: O sistema MUST avaliar uma senha contra uma política e retornar, em uma única operação, se ela é válida e a lista de todos os critérios não atendidos.
- **FR-002**: O sistema MUST avaliar todos os critérios da política antes de responder, sem interromper na primeira falha encontrada.
- **FR-003**: O sistema MUST suportar os critérios de comprimento mínimo, presença de letra maiúscula, presença de letra minúscula, presença de dígito e presença de caractere especial.
- **FR-004**: O sistema MUST permitir ativar ou desativar individualmente cada critério de composição e definir o comprimento mínimo, sem alteração de código.
- **FR-005**: O sistema MUST considerar caractere especial qualquer caractere que não seja letra, dígito ou espaço em branco.
- **FR-006**: O sistema MUST retornar cada pendência com uma mensagem que descreva o que falta, incluindo o valor exigido quando houver um (por exemplo, o comprimento mínimo).
- **FR-007**: O sistema MUST retornar uma lista de pendências vazia quando, e somente quando, a senha for válida.
- **FR-008**: O sistema MUST levantar `TypeError` quando a senha informada não for do tipo texto.
- **FR-009**: O sistema MUST levantar `ValueError` quando a política for construída com comprimento mínimo negativo.
- **FR-010**: O sistema MUST oferecer uma política padrão utilizável sem configuração: 8 caracteres, exigindo maiúscula, minúscula, dígito e caractere especial.

### Entidades principais

- **Política de senha**: conjunto de critérios em vigor — comprimento mínimo e quais categorias de caractere são exigidas. É dado de configuração, não de usuário.
- **Resultado da validação**: resposta da avaliação — se a senha é válida e a lista de pendências. Uma pendência descreve um critério não atendido, em linguagem apresentável ao usuário final.

## Critérios de Sucesso *(obrigatório)*

### Resultados mensuráveis

- **SC-001**: Uma senha que viola N critérios produz exatamente N pendências, em uma única chamada — o usuário nunca precisa de duas tentativas para descobrir dois problemas.
- **SC-002**: Todos os cenários de aceite e todos os casos de borda desta especificação têm teste automatizado correspondente.
- **SC-003**: Mudar a política de segurança do sistema não exige alterar nenhuma linha do validador, apenas a configuração passada a ele.
- **SC-004**: Uso incorreto da interface (tipo errado, política impossível) falha com exceção, nunca com um resultado de validação silenciosamente errado.

## Premissas

- A validação é local e síncrona. Não consulta listas de senhas vazadas nem serviços externos, o que seria outra funcionalidade.
- Não há medição de entropia nem pontuação de força em escala. O resultado é booleano mais a lista de pendências.
- O validador não armazena, registra em log nem transmite a senha avaliada.
- As mensagens de pendência são escritas em português, como o restante da documentação do projeto.
- Mantém-se a convenção do projeto de usar apenas a biblioteca padrão do Python e `unittest` para os testes.
