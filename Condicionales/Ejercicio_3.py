#1. Solicitar número al usuario y determinar si es negativo, positivo o cero.

numero1 = float(input("Ingrese un número: "))

if numero1 < 0:
    resultado = "El número es negativo."
elif numero1 > 0:
    resultado = "El número es positivo."
else:
    resultado = "El número es cero."

print(resultado)
