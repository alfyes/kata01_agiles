from unittest import TestCase
from Estadisticas import Estadisticas

class EstadisticasTest4(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular(""), [0, None, None, None], "Cadena Vacia Iter 4")
