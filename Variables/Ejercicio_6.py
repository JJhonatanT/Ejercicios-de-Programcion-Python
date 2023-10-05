#6. Programa que permita calcular el 30%, el 60% y el 90% de cualquier número.

numero = int(input("Ingrese el numero a calcular el 30%, 60% y 90%: "))

resultado1 = 30 * numero / 100
resultado2 = 60 * numero / 100
resultado3 = 90 * numero / 100

print(f"El porcentaje del 30% es de: {resultado1}% El de el 60% es de: {resultado2}% Y el 90% es de: {resultado3}%")