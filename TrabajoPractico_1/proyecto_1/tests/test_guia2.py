import unittest
from modules.guia2 import calcular_fibonacci_recursiva, calcular_potencia_dos_iterativo, calcular_potencia_dos_recursivo 

class Test_CalculadorPotenciaDosIterativo(unittest.TestCase):
    def test_calculo(self):
        n = 9
        self.assertEqual(calcular_potencia_dos_iterativo(n), 512)

class Test_CalculadorPotenciaDosRecursivo(unittest.TestCase):
    def test_calculo(self):
        n = 9
        self.assertEqual(calcular_potencia_dos_recursivo(n), 512)

if __name__ == "__main__":
    unittest.main()

class Test_CalculadorPotenciaDosRecursivo(unittest.TestCase):
    def test_calculo(self):
        n = 10
        self.assertEqual(calcular_fibonacci_recursiva(n), 55)