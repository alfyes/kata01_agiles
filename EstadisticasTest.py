from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTestCadenaVacia(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular(""), [0], "Cadena Vacia")
