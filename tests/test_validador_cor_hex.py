"""Testes isolados para `validar_cor_hex`, usando unittest nativo."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validador_cor_hex import validar_cor_hex


class TestValidarCorHex(unittest.TestCase):
    def test_seis_digitos_valido(self):
        self.assertIs(validar_cor_hex("#a1b2c3"), True)

    def test_tres_digitos_valido(self):
        self.assertIs(validar_cor_hex("#abc"), True)

    def test_minusculo(self):
        self.assertIs(validar_cor_hex("#ffffff"), True)

    def test_maiusculo(self):
        self.assertIs(validar_cor_hex("#FFFFFF"), True)

    def test_sem_hash(self):
        self.assertIs(validar_cor_hex("ffffff"), False)

    def test_digito_invalido(self):
        self.assertIs(validar_cor_hex("#gggggg"), False)

    def test_tamanho_errado(self):
        self.assertIs(validar_cor_hex("#ff00"), False)

    def test_entrada_nao_string(self):
        self.assertIs(validar_cor_hex(None), False)
        self.assertIs(validar_cor_hex(16777215), False)

    def test_string_vazia(self):
        self.assertIs(validar_cor_hex(""), False)

    def test_retorno_estritamente_booleano(self):
        for entrada in ["#fff", "#ffffff", "x", "", None, 0]:
            self.assertIsInstance(validar_cor_hex(entrada), bool)


if __name__ == "__main__":
    unittest.main()
