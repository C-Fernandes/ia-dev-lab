"""Testes isolados para `validar_cartao_credito` (algoritmo de Luhn)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validador_cartao_credito import validar_cartao_credito


class TestValidarCartaoCredito(unittest.TestCase):
    def test_numero_valido_luhn(self):
        self.assertIs(validar_cartao_credito("4532015112830366"), True)

    def test_numero_valido_com_espacos(self):
        self.assertIs(validar_cartao_credito("4532 0151 1283 0366"), True)

    def test_numero_invalido_luhn(self):
        self.assertIs(validar_cartao_credito("4532015112830367"), False)

    def test_nao_numerico(self):
        self.assertIs(validar_cartao_credito("abcd efgh ijkl mnop"), False)

    def test_string_vazia(self):
        self.assertIs(validar_cartao_credito(""), False)

    def test_entrada_nao_string(self):
        self.assertIs(validar_cartao_credito(None), False)
        self.assertIs(validar_cartao_credito(4532015112830366), False)

    def test_retorno_estritamente_booleano(self):
        for entrada in ["4532015112830366", "0", "", None, 0]:
            self.assertIsInstance(validar_cartao_credito(entrada), bool)


if __name__ == "__main__":
    unittest.main()
