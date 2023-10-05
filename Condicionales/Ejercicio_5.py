#5. Calcular el promedio de notas y determinar si aprobó

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 6.0:
    resultado = "Aprobó"
else:
    resultado = "No aprobó"

print(f"El promedio de notas es: {promedio}")
print(resultado)
