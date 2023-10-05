#1. Solicitar número al usuario y determinar si es par, impar o es cero. 


numero1 = int(input("Ingrese un número a determinar: "))


if numero1 == 0:
    resultado = "cero"
elif numero1 % 2 == 0:
    resultado = "par"
else:
    resultado = "impar"

1
print(f"El número ingresado es: {numero1} y numero es: {resultado}.")
