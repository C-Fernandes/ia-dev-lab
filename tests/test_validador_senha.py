"""Testes para o validador de senha forte (specs/001-validador-senha-forte)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validador_senha import POLITICA_PADRAO, PoliticaSenha, ValidadorSenha


def _pendencias(senha, politica=None):
    validador = ValidadorSenha(politica) if politica else ValidadorSenha()
    return validador.validar(senha).pendencias


def _texto(pendencias):
    return " | ".join(pendencias).lower()


class TestHistoria1FeedbackAcionavel(unittest.TestCase):
    """US1: a pessoa precisa saber tudo que falta de uma vez."""

    def test_senha_curta_reporta_todas_as_pendencias_juntas(self):
        pendencias = _pendencias("abc")
        texto = _texto(pendencias)

        self.assertEqual(len(pendencias), 4)
        self.assertIn("caracteres", texto)
        self.assertIn("maiúscula", texto)
        self.assertIn("dígito", texto)
        self.assertIn("especial", texto)

    def test_senha_valida_nao_tem_pendencias(self):
        resultado = ValidadorSenha().validar("Abc@1234")

        self.assertTrue(resultado.valida)
        self.assertEqual(resultado.pendencias, ())

    def test_comprimento_atendido_nao_vira_pendencia(self):
        pendencias = _pendencias("abcdefgh")
        texto = _texto(pendencias)

        self.assertEqual(len(pendencias), 3)
        self.assertNotIn("caracteres", texto)
        self.assertIn("maiúscula", texto)
        self.assertIn("dígito", texto)
        self.assertIn("especial", texto)


class TestHistoria2PoliticaConfiguravel(unittest.TestCase):
    """US2: mudar a régua sem mudar o código."""

    def test_comprimento_minimo_maior_reprova_senha_antes_valida(self):
        politica = PoliticaSenha(comprimento_minimo=12)
        pendencias = _pendencias("Abc@1234", politica)

        self.assertEqual(len(pendencias), 1)
        self.assertIn("12", pendencias[0])

    def test_politica_sem_caractere_especial_aprova_senha_alfanumerica(self):
        politica = PoliticaSenha(exigir_especial=False)
        resultado = ValidadorSenha(politica).validar("Abcd1234")

        self.assertTrue(resultado.valida)
        self.assertFalse(ValidadorSenha().validar("Abcd1234").valida)

    def test_politica_sem_criterios_aprova_qualquer_senha_nao_vazia(self):
        politica = PoliticaSenha(
            comprimento_minimo=1,
            exigir_maiuscula=False,
            exigir_minuscula=False,
            exigir_digito=False,
            exigir_especial=False,
        )

        self.assertTrue(ValidadorSenha(politica).validar("a").valida)
        self.assertFalse(ValidadorSenha(politica).validar("").valida)


class TestHistoria3ContratoDeUso(unittest.TestCase):
    """US3: uso incorreto falha alto, em vez de virar senha inválida."""

    def test_senha_nao_textual_levanta_typeerror(self):
        with self.assertRaises(TypeError):
            ValidadorSenha().validar(12345678)

    def test_senha_ausente_levanta_typeerror(self):
        with self.assertRaises(TypeError):
            ValidadorSenha().validar(None)

    def test_comprimento_minimo_negativo_levanta_valueerror(self):
        with self.assertRaises(ValueError):
            PoliticaSenha(comprimento_minimo=-1)


class TestCasosDeBorda(unittest.TestCase):
    def test_senha_vazia_e_invalida_sem_excecao(self):
        resultado = ValidadorSenha().validar("")

        self.assertFalse(resultado.valida)
        self.assertIn("caracteres", _texto(resultado.pendencias))

    def test_espacos_nao_contam_como_caractere_especial(self):
        pendencias = _pendencias(" " * 8)
        texto = _texto(pendencias)

        self.assertNotIn("caracteres", texto)
        self.assertIn("especial", texto)
        self.assertEqual(len(pendencias), 4)

    def test_comprimento_exatamente_no_minimo_e_valido(self):
        politica = PoliticaSenha(comprimento_minimo=8)
        resultado = ValidadorSenha(politica).validar("Abc@1234")

        self.assertEqual(len("Abc@1234"), 8)
        self.assertTrue(resultado.valida)

    def test_letra_acentuada_conta_como_minuscula_e_nao_como_especial(self):
        self.assertTrue(ValidadorSenha().validar("Senhá@123").valida)

        politica = PoliticaSenha(
            comprimento_minimo=1,
            exigir_maiuscula=False,
            exigir_minuscula=False,
            exigir_digito=False,
        )
        self.assertIn("especial", _texto(_pendencias("senhá", politica)))

    def test_senha_muito_longa_e_valida(self):
        senha = "Abc@1234" + ("x" * 250)

        self.assertTrue(ValidadorSenha().validar(senha).valida)

    def test_criterio_satisfeito_varias_vezes_nao_duplica_pendencia(self):
        resultado = ValidadorSenha().validar("AB@@12ab")
        self.assertTrue(resultado.valida)

        pendencias = _pendencias("aaa")
        self.assertEqual(len(pendencias), len(set(pendencias)))


class TestContratoDoResultado(unittest.TestCase):
    def test_valida_e_verdadeira_apenas_quando_nao_ha_pendencias(self):
        for senha in ["abc", "", "Abc@1234", "abcdefgh"]:
            resultado = ValidadorSenha().validar(senha)
            self.assertEqual(resultado.valida, resultado.pendencias == ())

    def test_politica_padrao_exige_oito_caracteres_e_os_quatro_criterios(self):
        self.assertEqual(POLITICA_PADRAO.comprimento_minimo, 8)
        self.assertTrue(POLITICA_PADRAO.exigir_maiuscula)
        self.assertTrue(POLITICA_PADRAO.exigir_minuscula)
        self.assertTrue(POLITICA_PADRAO.exigir_digito)
        self.assertTrue(POLITICA_PADRAO.exigir_especial)


if __name__ == "__main__":
    unittest.main()
