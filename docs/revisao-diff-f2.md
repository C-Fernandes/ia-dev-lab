# Registro de revisão de diff - Funcionalidade 2 (Senha Forte)

Referente à tarefa 12 da Etapa 3, repetida na Etapa 5.

## Diff revisado

Commit `feat: adiciona validador de senha forte com política configurável`, arquivo `src/validador_senha.py`.

## Problemas encontrados

Os dois são do mesmo tipo: o código atende ao comportamento especificado, mas diverge do que o `plan.md` determinou por escrito.

**1. Anotação de tipo contradiz o valor padrão.**

```python
def __init__(self, politica: PoliticaSenha = None):
```

A anotação diz `PoliticaSenha`, mas o padrão é `None`. São incompatíveis. O correto é `PoliticaSenha | None`. Como Python não verifica anotação em tempo de execução, o código funciona e os 17 testes passam.

**2. O tipo de `pendencias` perdeu a precisão definida no plano.**

O `plan.md` especifica `pendencias: tuple[str, ...]`. O código entregou:

```python
pendencias: tuple = field(default=())
```

A anotação `tuple` não diz o que a tupla contém, e o `field(default=())` é desnecessário, já que `pendencias: tuple = ()` faz o mesmo com tupla, que é imutável.

## Por que os testes não pegariam

Os 17 testes verificam comportamento: quantas pendências, quais mensagens, quais exceções. Anotação de tipo não altera nenhuma dessas coisas em tempo de execução. O projeto ainda não usa verificador estático, então nada além da leitura do diff acusaria a divergência.

## Comparação com a Funcionalidade 1

- Na F1, o problema estava **fora da spec**: o bloco de demonstração não era coberto por nenhum requisito.
- Na F2, o problema está **dentro do plano, mas fora dos testes**: o `plan.md` definiu a assinatura, e a implementação não seguiu.

Nos dois casos a suíte ficou verde. São formas diferentes de o mesmo ponto cego aparecer.

## Encaminhamento

Levado ao checkpoint humano ([`checkpoint-humano.md`](checkpoint-humano.md)). Decisão: editar antes de aprovar.
