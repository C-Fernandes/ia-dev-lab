"""Validação estrutural de CEP brasileiro."""


def validar_cep(cep: str) -> bool:
    """Retorna True se `cep` tiver o formato de um CEP brasileiro válido.

    Aceita string com ou sem hífen. Regras:
    - precisa ter exatamente 8 dígitos após remover hífen;
    - rejeita sequências com todos os dígitos iguais (ex.: '00000000').
    Validação puramente estrutural, não verifica existência do CEP.
    """
    if not isinstance(cep, str):
        return False

    digitos = cep.replace("-", "")

    if len(digitos) != 8 or not digitos.isdigit():
        return False

    if digitos == digitos[0] * 8:
        return False

    return True


if __name__ == "__main__":
    exemplos = [
        "59078-970",
        "59078970",
        "00000000",
        "1234-567",
        "abcdefgh",
        "",
    ]
    for c in exemplos:
        print(f"{c!r}: {validar_cep(c)}")
