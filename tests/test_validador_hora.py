"""Testes escritos DEPOIS de `validador_hora.py` (tarefa sem TDD, Etapa 2).

Objetivo: escrever a suíte de teste que normalmente teria vindo antes, para
medir a cobertura real de casos de borda de uma implementação feita sem
TDD. As falhas abaixo são deixadas propositalmente (não corrigidas) como
evidência da comparação com/sem TDD — ver docs/etapa2-tdd.md.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validador_hora import validar_hora


class TestValidarHora(unittest.TestCase):
    def test_hora_valida(self):
        self.assertIs(validar_hora("12:30"), True)

    def test_hora_limite_superior(self):
        self.assertIs(validar_hora("23:59"), True)

    def test_hora_limite_inferior(self):
        self.assertIs(validar_hora("00:00"), True)

    def test_hora_fora_do_intervalo(self):
        self.assertIs(validar_hora("24:00"), False)

    def test_string_vazia(self):
        self.assertIs(validar_hora(""), False)

    def test_entrada_nao_string(self):
        self.assertIs(validar_hora(None), False)

    def test_exige_dois_digitos_na_hora(self):
        # GAP: implementado sem TDD aceita "1:5" como se fosse "01:05".
        self.assertIs(validar_hora("1:5"), False)

    def test_exige_dois_digitos_no_minuto(self):
        # GAP: mesmo problema isolado no minuto.
        self.assertIs(validar_hora("09:9"), False)

    def test_rejeita_digitos_nao_ascii(self):
        # GAP: str.isdigit()/int() aceitam dígitos unicode (ex.: arábicos-indicos),
        # entao "٢٣:٠٠" (23:00) passa como valido.
        self.assertIs(validar_hora("٢٣:٠٠"), False)


if __name__ == "__main__":
    unittest.main()
