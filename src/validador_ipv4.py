"""Validador de endereços IPv4."""


def validar_ipv4(ip: str) -> bool:
    """Valida se a string representa um endereço IPv4 válido.

    Um IPv4 válido tem 4 octetos separados por ponto, cada um representando
    um número inteiro entre 0 e 255, sem zeros à esquerda (exceto o próprio
    "0") e sem espaços.
    """
    if not isinstance(ip, str):
        return False

    octetos = ip.split(".")
    if len(octetos) != 4:
        return False

    for octeto in octetos:
        if not octeto.isdigit():
            return False
        if octeto != "0" and octeto.startswith("0"):
            return False
        if not 0 <= int(octeto) <= 255:
            return False

    return True
