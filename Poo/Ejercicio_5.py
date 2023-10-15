#5. Escriba un clase padre llamada Ave que herede a clases hijas con tipos de aves

class Ave:
    def __init__(self, nombre, color, habitat):
        self.nombre = nombre
        self.color = color
        self.habitat = habitat

    def volar(self):
        print(f"{self.nombre} está volando.")

class Pajaro(Ave):
    def __init__(self, nombre, color, habitat, tipo_pico):
        super().__init__(nombre, color, habitat)
        self.tipo_pico = tipo_pico

    def cantar(self):
        print(f"{self.nombre} está cantando.")

class Aguila(Ave):
    def __init__(self, nombre, color, habitat, envergadura):
        super().__init__(nombre, color, habitat)
        self.envergadura = envergadura

    def cazar(self):
        print(f"{self.nombre} está cazando presas.")

# Ejemplo de uso
pajaro = Pajaro("Canario", "Amarillo", "Bosque", "Cónico")
aguila = Aguila("Águila Real", "Marrón", "Montañas", "Amplia")

print(f"{pajaro.nombre} es un pájaro de color {pajaro.color} que vive en {pajaro.habitat}.")
pajaro.volar()
pajaro.cantar()

print(f"{aguila.nombre} es un águila de color {aguila.color} que vive en {aguila.habitat}.")
aguila.volar()
aguila.cazar()
