"""Validação estrutural de placa de veículo brasileira (formato antigo e Mercosul)."""


def validar_placa(placa: str) -> bool:
    """Retorna True se `placa` for uma placa brasileira válida.

    Aceita string com ou sem hífen/espaços, case-insensitive. Formatos aceitos:
    - antigo: 3 letras + 4 dígitos (ex.: 'ABC1234', 'ABC-1234');
    - Mercosul: 3 letras + 1 dígito + 1 letra + 2 dígitos (ex.: 'ABC1D23').
    Qualquer outro formato ou tamanho é rejeitado.
    """
    if not isinstance(placa, str):
        return False

    normalizada = placa.replace("-", "").replace(" ", "").upper()

    if len(normalizada) != 7:
        return False

    letras = normalizada[:3]
    resto = normalizada[3:]

    if not letras.isalpha():
        return False

    formato_antigo = resto.isdigit()
    formato_mercosul = (
        resto[0].isdigit() and resto[1].isalpha() and resto[2:].isdigit()
    )

    return formato_antigo or formato_mercosul


if __name__ == "__main__":
    exemplos = [
        "ABC1234",
        "ABC-1234",
        "abc1234",
        "ABC1D23",
        "ABC12D3",
        "AB1234",
        "1234ABC",
        "",
    ]
    for p in exemplos:
        print(f"{p!r}: {validar_placa(p)}")
