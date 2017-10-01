from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTestCadenaVacia(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular(""), [0], "Cadena Vacia")

    def test_calcularUnNumero(self):
        self.assertEqual(Estadisticas().calcular("1"), [1], "Un Numero")

    def test_calcularDosNumero(self):
        self.assertEqual(Estadisticas().calcular("1,2"), [2], "Dos Numeros")