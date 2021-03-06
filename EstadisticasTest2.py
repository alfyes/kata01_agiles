from unittest import TestCase
from Estadisticas import Estadisticas

class EstadisticasTest2(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular(""), [0, None], "Cadena Vacia Iter 2")

    def test_calcularUnNumero(self):
        self.assertEqual(Estadisticas().calcular("11"), [1, 11], "Un Numero Iter 2")

    def test_calcularDosNumeros(self):
        self.assertEqual(Estadisticas().calcular("11,5"), [2, 5], "Dos Numero Iter 2")

    def test_calcularMultiplesNumeros(self):
        self.assertEqual(Estadisticas().calcular("11,5,8,2"), [4, 2], "Multiples Numeros Iter 2")
