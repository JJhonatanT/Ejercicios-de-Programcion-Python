#4. Determinar el número mayor y menor entre dos números

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
