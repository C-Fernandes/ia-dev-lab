"""Testes para `ValidadorDocumentos` (CPF/CNPJ), usando unittest nativo."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validador_documentos import ValidadorDocumentos


class TestValidarCpf(unittest.TestCase):
    def test_cpf_valido_formatado(self):
        self.assertIs(ValidadorDocumentos.validar_cpf("529.982.247-25"), True)

    def test_cpf_valido_sem_formatacao(self):
        self.assertIs(ValidadorDocumentos.validar_cpf("52998224725"), True)

    def test_cpf_digitos_repetidos(self):
        self.assertIs(ValidadorDocumentos.validar_cpf("111.111.111-11"), False)

    def test_cpf_todos_zeros(self):
        self.assertIs(ValidadorDocumentos.validar_cpf("000.000.000-00"), False)

    def test_cpf_digito_verificador_incorreto(self):
        self.assertIs(ValidadorDocumentos.validar_cpf("529.982.247-26"), False)

    def test_cpf_tamanho_invalido(self):
        self.assertIs(ValidadorDocumentos.validar_cpf("123.456.789"), False)

    def test_cpf_string_vazia(self):
        self.assertIs(ValidadorDocumentos.validar_cpf(""), False)

    def test_cpf_entrada_nao_string_lanca_typeerror(self):
        with self.assertRaises(TypeError):
            ValidadorDocumentos.validar_cpf(52998224725)

        with self.assertRaises(TypeError):
            ValidadorDocumentos.validar_cpf(None)

    def test_cpf_retorno_estritamente_booleano(self):
        for entrada in ["529.982.247-25", "111.111.111-11", ""]:
            self.assertIsInstance(ValidadorDocumentos.validar_cpf(entrada), bool)


class TestValidarCnpj(unittest.TestCase):
    def test_cnpj_valido_formatado(self):
        self.assertIs(ValidadorDocumentos.validar_cnpj("11.222.333/0001-81"), True)

    def test_cnpj_valido_sem_formatacao(self):
        self.assertIs(ValidadorDocumentos.validar_cnpj("11222333000181"), True)

    def test_cnpj_digitos_repetidos(self):
        self.assertIs(ValidadorDocumentos.validar_cnpj("00.000.000/0000-00"), False)

    def test_cnpj_digitos_verificadores_incorretos(self):
        self.assertIs(ValidadorDocumentos.validar_cnpj("12.345.678/0001-99"), False)

    def test_cnpj_tamanho_invalido(self):
        self.assertIs(ValidadorDocumentos.validar_cnpj("11.222.333/0001-8"), False)

    def test_cnpj_string_vazia(self):
        self.assertIs(ValidadorDocumentos.validar_cnpj(""), False)

    def test_cnpj_entrada_nao_string_lanca_typeerror(self):
        with self.assertRaises(TypeError):
            ValidadorDocumentos.validar_cnpj(11222333000181)

        with self.assertRaises(TypeError):
            ValidadorDocumentos.validar_cnpj(None)

    def test_cnpj_retorno_estritamente_booleano(self):
        for entrada in ["11.222.333/0001-81", "00.000.000/0000-00", ""]:
            self.assertIsInstance(ValidadorDocumentos.validar_cnpj(entrada), bool)


if __name__ == "__main__":
    unittest.main()
