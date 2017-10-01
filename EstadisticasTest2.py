from unittest import TestCase
from Estadisticas import Estadisticas

class EstadisticasTest2(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular(""), [0, None], "Cadena Vacia Iter 2")
