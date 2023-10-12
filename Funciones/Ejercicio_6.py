#6. Escriba una función de Python para calcular el factorial de un número (un entero no negativo). 
#La función acepta el número como argumento.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input("Ingresa un número: "))

resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
