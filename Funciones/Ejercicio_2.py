#2. Escriba un programa para calcular las áreas de las figuras geométricas utilizando una función para cada área. 
import math

def area_cuadrado(lado):
    return lado * lado

def area_rectángulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_rombo(diagonal_mayor, diagonal_menor):
    return  (diagonal_mayor * diagonal_menor)/2

def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor * base_menor)/2) * altura

while True:
    print("Seleccione una figura geométrica:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Rombo")
    print("6. Trapecio")
    print("7. Salir")
    
    opcion = input("Ingrese el número de la figura a calcular: ")

 
    if opcion == "1":
        lado = float(input("Ingrese el lado del cuadrado: "))
        print("El área del cuadrado es:", area_cuadrado(lado))
    
    elif opcion == "2":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print("El área del rectángulo es:", area_rectángulo(base, altura))
    
    elif opcion == "3":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es:", area_triangulo(base, altura))
    
    elif opcion == "4":
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es:", area_circulo(radio))
     
    elif opcion == "5":
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        print("El área del rombo es:", area_rombo(diagonal_mayor, diagonal_menor))
     
    elif opcion == "6":
        base_mayor = float(input("Ingrese la base mayor del trapecio: "))
        base_menor = float(input("Ingrese la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        print("El área del trapecio es:", area_trapecio(base_mayor, base_menor, altura))

        
    elif opcion == "7":
        break