"""Testes isolados para `validar_email_simples`, usando unittest nativo."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validador_email_simples import validar_email_simples


class TestValidarEmailSimples(unittest.TestCase):
    def test_email_valido_simples(self):
        self.assertIs(validar_email_simples("usuario@exemplo.com"), True)

    def test_email_valido_com_subdominio(self):
        self.assertIs(
            validar_email_simples("nome.sobrenome+tag@sub.dominio.com.br"), True
        )

    def test_dominio_vazio(self):
        self.assertIs(validar_email_simples("invalido@"), False)

    def test_parte_local_vazia(self):
        self.assertIs(validar_email_simples("@sem-local.com"), False)

    def test_sem_arroba(self):
        self.assertIs(validar_email_simples("sem-arroba.com"), False)

    def test_multiplos_arrobas(self):
        self.assertIs(validar_email_simples("dois@arrobas@aqui.com"), False)

    def test_string_vazia(self):
        self.assertIs(validar_email_simples(""), False)

    def test_apenas_arroba(self):
        self.assertIs(validar_email_simples("@"), False)

    def test_entrada_nao_string(self):
        self.assertIs(validar_email_simples(None), False)
        self.assertIs(validar_email_simples(123), False)

    def test_retorno_estritamente_booleano(self):
        for entrada in ["a@b", "@", "x", "", None, 0]:
            self.assertIsInstance(validar_email_simples(entrada), bool)


if __name__ == "__main__":
    unittest.main()
