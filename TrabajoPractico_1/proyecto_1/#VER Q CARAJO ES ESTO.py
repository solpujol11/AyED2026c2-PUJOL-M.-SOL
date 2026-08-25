#VER Q CARAJO ES ESTO
property
def nombre (self):
    return self.__nombre

@property
def apellido (self):
    return self.__apellido



class CalculadoraIMC:
    def __init__(self, peso, altura):
        self.establecer_altura(altura)
        self.establecer_peso(peso)

    def establecer_altura(self, altura):
        if isinstance(altura,(int,float)):
            if altura > 0:
                self.altura = float(altura)
            else:
                raise ValueError ("Altura debe ser mayor que 0")
        else:
            raise TypeError ("Altura no es un float")

    def establecer_peso(self, peso):
        if isinstance(peso,(int,float)):
            if peso > 0:
                self.peso = float(peso)
            else:
                raise ValueError ("Peso debe ser mayor que 0")
        else:
            raise TypeError ("Peso no es un float")

    @property
    def imc (self):
        return self.peso / (self.altura ** 2)
    @property
    def info(self):
        imc = self.imc
        if imc < 18.5:
            return f"Tu IMC {imc:.2f} está debajo de lo normal"
        elif imc < 25:
            return f"Tu IMC {imc:.2f} está en el rango normal"
        elif imc < 30:
            return f"Tu IMC {imc:.2f} indica Sobrepeso"
        else:
            return f"Tu IMC {imc:.2f} indica Obesidad"