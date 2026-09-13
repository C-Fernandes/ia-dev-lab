"""Validação de número de cartão de crédito pelo algoritmo de Luhn."""


def validar_cartao_credito(numero: str) -> bool:
    """Retorna True se `numero` passar no algoritmo de Luhn.

    Aceita string com ou sem espaços. Não valida bandeira/emissor, apenas o
    dígito verificador de Luhn.
    """
    if not isinstance(numero, str):
        return False

    digitos = numero.replace(" ", "")

    if not digitos.isdigit() or len(digitos) < 2:
        return False

    soma = 0
    dobrar = False
    for digito in reversed(digitos):
        valor = int(digito)
        if dobrar:
            valor *= 2
            if valor > 9:
                valor -= 9
        soma += valor
        dobrar = not dobrar

    return soma % 10 == 0


if __name__ == "__main__":
    exemplos = [
        "4532015112830366",
        "4532 0151 1283 0366",
        "4532015112830367",
        "abcd efgh ijkl mnop",
    ]
    for n in exemplos:
        print(f"{n!r}: {validar_cartao_credito(n)}")
