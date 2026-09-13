"""Validação estrutural de horário no formato HH:MM (24h)."""


def validar_hora(hora: str) -> bool:
    """Retorna True se `hora` estiver no formato HH:MM, 00:00 a 23:59."""
    if not isinstance(hora, str):
        return False

    partes = hora.split(":")
    if len(partes) != 2:
        return False

    h, m = partes
    if not (h.isdigit() and m.isdigit()):
        return False

    return 0 <= int(h) <= 23 and 0 <= int(m) <= 59
