"""Validação estrutural simples de e-mail, sem uso de `re`."""


def validar_email_simples(email: str) -> bool:
    """Retorna True se `email` tiver texto de ambos os lados de um único '@'.

    Validação puramente estrutural:
    - a entrada precisa ser uma string;
    - precisa existir exatamente um caractere '@';
    - a parte local e o domínio não podem ser vazios.

    Não usa expressões regulares nem verifica formato de domínio, TLD ou
    existência da caixa de correio.
    """
    if not isinstance(email, str):
        return False

    partes = email.split("@")

    if len(partes) != 2:
        return False

    parte_local, dominio = partes

    return bool(parte_local) and bool(dominio)


if __name__ == "__main__":
    exemplos = [
        "usuario@exemplo.com",
        "nome.sobrenome+tag@sub.dominio.com.br",
        "invalido@",
        "@sem-local.com",
        "sem-arroba.com",
        "dois@arrobas@aqui.com",
    ]
    for e in exemplos:
        print(f"{e!r}: {validar_email_simples(e)}")
