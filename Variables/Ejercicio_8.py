#8. Programa que permita ingresar 5 números y calcular el promedio.

num1 = float(input("Ingrese el numero 1: "))
num2 = float(input("Ingrese el numero 2: "))
num3 = float(input("Ingrese el numero 3: "))
num4 = float(input("Ingrese el numero 4: "))
num5 = float(input("Ingrese el numero 5: "))
num_n = 5


resultado = num1 + num2 + num3 + num4 + num5 
resultado2 = resultado / num_n

print(f"El promedio de sus numeros es de: {resultado2}")