import unittest
from gerenciador_notas import calcular_media, verificar_aprovacao


class TestGerenciadorNotas(unittest.TestCase):

    def test_calcular_media_normal(self):
        """
        Testa o cálculo normal da média.
        """

        resultado = calcular_media([8.0, 7.0, 9.0])

        self.assertEqual(resultado, 8.0)

    def test_verificar_aprovacao_aprovado(self):
        """
        Testa situação de aprovação.
        """

        resultado = verificar_aprovacao(8.0)

        self.assertEqual(resultado, "Aprovado")

    def test_verificar_aprovacao_reprovado(self):
        """
        Testa situação de reprovação.
        """

        resultado = verificar_aprovacao(5.0)

        self.assertEqual(resultado, "Reprovado")

    def test_lista_notas_vazia(self):
        """
        Testa comportamento com lista vazia.
        """

        with self.assertRaises(ZeroDivisionError):
            calcular_media([])

    def test_media_minima_zero(self):
        """
        Testa aprovação utilizando média mínima igual a zero.
        """

        resultado = verificar_aprovacao(0, media_minima=0)

        self.assertEqual(resultado, "Aprovado")


if __name__ == "__main__":
    unittest.main()