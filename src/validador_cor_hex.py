"""Validação de cor hexadecimal CSS."""

import re

_PADRAO_COR_HEX = re.compile(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def validar_cor_hex(cor: str) -> bool:
    """Retorna True se `cor` for uma cor hexadecimal CSS válida.

    Aceita os formatos `#RGB` (3 dígitos) e `#RRGGBB` (6 dígitos), com o `#`
    obrigatório e dígitos hexadecimais (case-insensitive).
    """
    if not isinstance(cor, str):
        return False

    return bool(_PADRAO_COR_HEX.match(cor))


if __name__ == "__main__":
    exemplos = [
        "#fff",
        "#FFFFFF",
        "#a1B2c3",
        "fff",
        "#ggg",
        "#ff",
        "",
    ]
    for c in exemplos:
        print(f"{c!r}: {validar_cor_hex(c)}")
