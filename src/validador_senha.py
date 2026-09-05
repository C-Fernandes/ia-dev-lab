"""Validação de senha forte com política configurável.

Comportamento especificado em specs/001-validador-senha-forte/spec.md.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PoliticaSenha:
    """Critérios em vigor. É configuração do sistema, não dado de usuário."""

    comprimento_minimo: int = 8
    exigir_maiuscula: bool = True
    exigir_minuscula: bool = True
    exigir_digito: bool = True
    exigir_especial: bool = True

    def __post_init__(self):
        if self.comprimento_minimo < 0:
            raise ValueError(
                "comprimento_minimo não pode ser negativo, recebido: "
                f"{self.comprimento_minimo}"
            )


@dataclass(frozen=True)
class ResultadoValidacao:
    """Resposta da avaliação: o que falta, se é que falta algo."""

    pendencias: tuple = field(default=())

    @property
    def valida(self) -> bool:
        return not self.pendencias


POLITICA_PADRAO = PoliticaSenha()


class ValidadorSenha:
    """Avalia senhas contra uma política, sem armazenar nem registrar nada."""

    def __init__(self, politica: PoliticaSenha = None):
        self.politica = politica if politica is not None else POLITICA_PADRAO

    @staticmethod
    def _e_especial(caractere: str) -> bool:
        # Definido por exclusão: pega qualquer símbolo Unicode sem manter uma
        # lista de permissão, e mantém acento como letra e espaço fora da conta.
        return not caractere.isalnum() and not caractere.isspace()

    def validar(self, senha: str) -> ResultadoValidacao:
        if not isinstance(senha, str):
            raise TypeError(
                f"Senha deve ser uma string, recebido: {type(senha).__name__}"
            )

        politica = self.politica
        pendencias = []

        # Todos os critérios são avaliados, sem parar na primeira falha: o
        # objetivo é devolver a lista completa em uma única chamada.
        if len(senha) < politica.comprimento_minimo:
            pendencias.append(
                f"A senha deve ter no mínimo {politica.comprimento_minimo} caracteres."
            )

        if politica.exigir_maiuscula and not any(c.isupper() for c in senha):
            pendencias.append("A senha deve conter pelo menos uma letra maiúscula.")

        if politica.exigir_minuscula and not any(c.islower() for c in senha):
            pendencias.append("A senha deve conter pelo menos uma letra minúscula.")

        if politica.exigir_digito and not any(c.isdigit() for c in senha):
            pendencias.append("A senha deve conter pelo menos um dígito.")

        if politica.exigir_especial and not any(self._e_especial(c) for c in senha):
            pendencias.append(
                "A senha deve conter pelo menos um caractere especial "
                "(símbolo que não seja letra, dígito ou espaço)."
            )

        return ResultadoValidacao(tuple(pendencias))


if __name__ == "__main__":
    exemplos = ["abc", "abcdefgh", "Abc@1234", "Senhá@123"]

    for exemplo in exemplos:
        resultado = ValidadorSenha().validar(exemplo)
        print(f"{exemplo!r}: valida={resultado.valida}")
        for pendencia in resultado.pendencias:
            print(f"  - {pendencia}")
