"""Testes isolados para `validar_ipv4`, usando unittest nativo."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validador_ipv4 import validar_ipv4


class TestValidarIpv4(unittest.TestCase):
    def test_ip_valido_comum(self):
        self.assertIs(validar_ipv4("192.168.0.1"), True)

    def test_octeto_maior_que_255(self):
        self.assertIs(validar_ipv4("192.168.0.256"), False)

    def test_menos_de_quatro_octetos(self):
        self.assertIs(validar_ipv4("192.168.0"), False)

    def test_zero_a_esquerda(self):
        self.assertIs(validar_ipv4("192.168.01.1"), False)

    def test_entrada_nao_string(self):
        self.assertIs(validar_ipv4(None), False)
        self.assertIs(validar_ipv4(19216801), False)

    def test_string_vazia(self):
        self.assertIs(validar_ipv4(""), False)

    def test_retorno_estritamente_booleano(self):
        for entrada in ["192.168.0.1", "192.168.0.256", "x", "", None, 0]:
            self.assertIsInstance(validar_ipv4(entrada), bool)


if __name__ == "__main__":
    unittest.main()
