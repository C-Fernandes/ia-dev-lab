"""Validação de endereços de e-mail usando apenas a biblioteca padrão."""

import re

# Padrão prático baseado na especificação HTML5 para o atributo type="email".
# Aceita a maioria dos endereços válidos do mundo real sem tentar cobrir
# todos os casos exóticos da RFC 5322.
_PADRAO_EMAIL = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)

TAMANHO_MAXIMO = 254


def validar_email(email: str) -> bool:
    """Retorna True se `email` for um endereço de e-mail válido.

    A validação verifica:
    - que a entrada é uma string não vazia;
    - que o comprimento total não excede 254 caracteres (limite prático de SMTP);
    - que o formato corresponde a `parte-local@dominio.tld`.

    Não verifica se o domínio existe ou se a caixa de correio recebe mensagens.
    """
    if not isinstance(email, str):
        return False

    email = email.strip()

    if not email or len(email) > TAMANHO_MAXIMO:
        return False

    parte_local, _, dominio = email.partition("@")

    # A parte local não pode passar de 64 caracteres (RFC 5321).
    if len(parte_local) > 64 or not dominio:
        return False

    # Pontos consecutivos ou no início/fim da parte local são inválidos.
    if parte_local.startswith(".") or parte_local.endswith(".") or ".." in parte_local:
        return False

    return _PADRAO_EMAIL.match(email) is not None


if __name__ == "__main__":
    exemplos = [
        "usuario@exemplo.com",
        "nome.sobrenome+tag@sub.dominio.com.br",
        "invalido@",
        "@sem-local.com",
        "espaco no meio@exemplo.com",
        "ponto..duplo@exemplo.com",
    ]
    for e in exemplos:
        print(f"{e!r}: {validar_email(e)}")
