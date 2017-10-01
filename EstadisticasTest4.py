from unittest import TestCase
from Estadisticas import Estadisticas

class EstadisticasTest4(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular(""), [0, None, None, None], "Cadena Vacia Iter 4")

    def test_calcularUnNumero(self):
        self.assertEqual(Estadisticas().calcular("11"), [1, 11, 11, 11], "Un Numero Iter 4")

    def test_calcularDosNumeros(self):
        self.assertEqual(Estadisticas().calcular("11,5"), [2, 5, 11, 8], "Dos Numeros Iter 4")