import unittest
from modules.guia1 import CalculadoraIMC, Persona
from prueba import Cuadrado

class Test_Cuadrado(unittest.TestCase):
    def test_lado(self):
        cuadrado=Cuadrado(4)
        self.assertEqual(cuadrado.lado,4)
    def test_area(self):
        cuadrado=Cuadrado(2)
        self.assertEqual(cuadrado.obtener_area,4)
    def test_perimetro(self):
        cuadrado=Cuadrado(1)
        self.assertEqual(cuadrado.obtener_perimetro,4)

class Test_Persona(unittest.TestCase):
    def test_nombre_apellido_validos(self):
        persona=Persona("amanda","epson")
        self.assertEqual((persona.nombre,persona.apellido),("Amanda","Epson"))
    def test_nombre_invalido(self):
        with self.assertRaises(TypeError):
            persona = Persona(1,"epson")

    def test_apellido_invalido(self):
        with self.assertRaises(TypeError):
            persona = Persona("amanda",2)

if __name__ == "__main__":
    unittest.main()

class Test_CalculadoraIMC(unittest.TestCase):
    def test_peso_invalido(self):
        with self.assertRaises(TypeError):
            calculado = CalculadoraIMC("75", 1.80) #cuando a peso le pongo algo que no es un numero debe dar TypeError

if __name__ == "__main__":
    unittest.main()