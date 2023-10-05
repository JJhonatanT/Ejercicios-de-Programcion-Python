#12. Calcular la hipotenusa con el Teorema de Pitágoras.

cateto_a = float(input("Ingrese la longitud del primer cateto A: "))
cateto_b = float(input("Ingrese la longitud del segundo cateto B: "))

hipotenusa = (cateto_a**2 + cateto_b**2)**0.5

print(f"La longitud de la hipotenusa es de: {hipotenusa}")
