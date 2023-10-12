#7. Escriba una función de Python para comprobar si un número cae en un rango determinado.

def rango(numero, rango_minimo, rango_maximo):
    return rango_minimo <= numero <= rango_maximo

numero = float(input("Ingresa un número: "))
rango_minimo = 1
rango_maximo = 10

if rango(numero, rango_minimo, rango_maximo):
    print(f"{numero} está en el rango [{rango_minimo}, {rango_maximo}]")
else:
    print(f"{numero} no está en el rango [{rango_minimo}, {rango_maximo}]")
