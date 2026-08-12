import unittest
from guia1 import Cuadrado, Persona

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