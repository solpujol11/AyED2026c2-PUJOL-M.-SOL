import unittest
from modules.guia2 import calcular_potencia_dos_iterativo

class Test_CalculadorPotenciaDosIterativo(unittest.TestCase):
    def test_calculo(self):
        n = 9
        self.assertEqual(calcular_potencia_dos_iterativo(n), 512)
if __name__ == "__main__":
    unittest.main()