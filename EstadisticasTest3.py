from unittest import TestCase
from Estadisticas import Estadisticas


class EstadisticasTest3(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular(""), [0, None, None], "Cadena Vacia Iter 3")

    def test_calcularUnNumero(self):
        self.assertEqual(Estadisticas().calcular("11"), [1, 11, 11], "Un Numero Iter 3")

    def test_calcularDosNumeros(self):
        self.assertEqual(Estadisticas().calcular("11,5"), [2, 5, 11], "Dos Numeros Iter 3")

    def test_calcularMultiplesNumeros(self):
        self.assertEqual(Estadisticas().calcular("11,5,27,2"), [4, 2, 27], "Multiples Numeros Iter 2")