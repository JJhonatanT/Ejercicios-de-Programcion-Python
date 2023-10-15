#3. Escriba una clase de Python llamada Circle construida por un radio y dos métodos que calcularán
# el área y el perímetro de un círculo.

import math

class Circle:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio**2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

radio = 5
circulo = Circle(radio)  
area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()

print(f"Radio del círculo: {radio}")
print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")
