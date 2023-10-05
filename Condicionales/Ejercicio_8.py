#8. Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente. 

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print("Números en orden ascendente:", numero1, numero2, numero3)
print("Números en orden descendente:", numero3, numero2, numero1)
