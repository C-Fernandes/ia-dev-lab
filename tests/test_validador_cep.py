"""Testes isolados para `validar_cep`, usando unittest nativo."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validador_cep import validar_cep


class TestValidarCep(unittest.TestCase):
    def test_cep_valido_com_hifen(self):
        self.assertIs(validar_cep("59078-970"), True)

    def test_cep_valido_sem_hifen(self):
        self.assertIs(validar_cep("59078970"), True)

    def test_digitos_repetidos(self):
        self.assertIs(validar_cep("00000000"), False)

    def test_tamanho_errado(self):
        self.assertIs(validar_cep("1234-567"), False)

    def test_nao_numerico(self):
        self.assertIs(validar_cep("abcdefgh"), False)

    def test_string_vazia(self):
        self.assertIs(validar_cep(""), False)

    def test_entrada_nao_string(self):
        self.assertIs(validar_cep(None), False)
        self.assertIs(validar_cep(59078970), False)

    def test_retorno_estritamente_booleano(self):
        for entrada in ["59078-970", "00000000", "x", "", None, 0]:
            self.assertIsInstance(validar_cep(entrada), bool)


if __name__ == "__main__":
    unittest.main()
