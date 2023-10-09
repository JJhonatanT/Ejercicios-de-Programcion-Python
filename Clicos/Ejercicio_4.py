#4. Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.

suma = 0

for contador in range(1, 11):
    try:
        numero = float(input(f"Ingrese el número {contador}: "))
        suma += numero
    except ValueError:
        print("¡Entrada no válida! Por favor, ingrese un número válido.")


promedio = suma / 10

# Mostramos la suma y el promedio
print(f"La suma de los 10 números es: {suma}")
print(f"El promedio de los 10 números es: {promedio}")
