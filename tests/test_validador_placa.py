"""Testes isolados para `validar_placa`, usando unittest nativo."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validador_placa import validar_placa


class TestValidarPlaca(unittest.TestCase):
    def test_placa_antiga_valida(self):
        self.assertIs(validar_placa("ABC1234"), True)

    def test_placa_antiga_valida_com_hifen(self):
        self.assertIs(validar_placa("ABC-1234"), True)

    def test_placa_antiga_minuscula(self):
        self.assertIs(validar_placa("abc1234"), True)

    def test_placa_mercosul_valida(self):
        self.assertIs(validar_placa("ABC1D23"), True)

    def test_tamanho_errado_curto(self):
        self.assertIs(validar_placa("AB1234"), False)

    def test_tamanho_errado_longo(self):
        self.assertIs(validar_placa("ABCD1234"), False)

    def test_letras_no_lugar_de_digitos(self):
        self.assertIs(validar_placa("ABCDEFG"), False)

    def test_digitos_no_lugar_de_letras(self):
        self.assertIs(validar_placa("1234ABC"), False)

    def test_mercosul_posicao_letra_errada(self):
        self.assertIs(validar_placa("ABC12D3"), False)

    def test_string_vazia(self):
        self.assertIs(validar_placa(""), False)

    def test_entrada_nao_string(self):
        self.assertIs(validar_placa(None), False)
        self.assertIs(validar_placa(1234567), False)

    def test_retorno_estritamente_booleano(self):
        for entrada in ["ABC1234", "ABC1D23", "invalida", "", None, 0]:
            self.assertIsInstance(validar_placa(entrada), bool)


if __name__ == "__main__":
    unittest.main()
