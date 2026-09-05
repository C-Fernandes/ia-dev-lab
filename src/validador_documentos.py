"""Validação oficial de CPF e CNPJ (RF01-RF05 em docs/especificacao-cpf-cnpj.md)."""


class ValidadorDocumentos:
    """Valida CPF e CNPJ segundo o algoritmo oficial da Receita Federal."""

    _PESOS_CPF_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    _PESOS_CPF_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    _PESOS_CNPJ_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    _PESOS_CNPJ_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    @staticmethod
    def _limpar(documento: str) -> str:
        if not isinstance(documento, str):
            raise TypeError(
                f"Documento deve ser uma string, recebido: {type(documento).__name__}"
            )
        return "".join(c for c in documento if c.isdigit())

    @staticmethod
    def _todos_digitos_iguais(digitos: str) -> bool:
        return len(set(digitos)) == 1

    @staticmethod
    def _calcular_digito_verificador(digitos: str, pesos: list) -> int:
        soma = sum(int(d) * p for d, p in zip(digitos, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    @classmethod
    def validar_cpf(cls, documento: str) -> bool:
        digitos = cls._limpar(documento)

        if len(digitos) != 11 or cls._todos_digitos_iguais(digitos):
            return False

        digito1 = cls._calcular_digito_verificador(digitos[:9], cls._PESOS_CPF_1)
        digito2 = cls._calcular_digito_verificador(digitos[:9] + str(digito1), cls._PESOS_CPF_2)

        return digitos[-2:] == f"{digito1}{digito2}"

    @classmethod
    def validar_cnpj(cls, documento: str) -> bool:
        digitos = cls._limpar(documento)

        if len(digitos) != 14 or cls._todos_digitos_iguais(digitos):
            return False

        digito1 = cls._calcular_digito_verificador(digitos[:12], cls._PESOS_CNPJ_1)
        digito2 = cls._calcular_digito_verificador(digitos[:12] + str(digito1), cls._PESOS_CNPJ_2)

        return digitos[-2:] == f"{digito1}{digito2}"


if __name__ == "__main__":
    # O tipo de documento e escolhido explicitamente: inferir pelo tamanho da
    # string roteia um CNPJ sem mascara (14 caracteres) para validar_cpf.
    exemplos_cpf = ["529.982.247-25", "52998224725", "111.111.111-11"]
    exemplos_cnpj = ["11.222.333/0001-81", "11222333000181", "12.345.678/0001-99"]

    for documento in exemplos_cpf:
        print(f"CPF  {documento!r}: {ValidadorDocumentos.validar_cpf(documento)}")

    for documento in exemplos_cnpj:
        print(f"CNPJ {documento!r}: {ValidadorDocumentos.validar_cnpj(documento)}")
