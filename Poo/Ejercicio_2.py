#2. Escriba una clase de Python llamada Rectangle construida por una longitud y anchura y un método 
#que calculará el área de un rectángulo.

class Rectangle:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho


rectangulo = Rectangle(5, 10)  
area = rectangulo.calcular_area()
print(f"El área del rectángulo es: {area}")
