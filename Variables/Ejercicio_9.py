#9. Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.

producto = int(input("Ingrese el precio de Platanos a llevar : "))
cantidad = int(input("Ingrese el numero de Platanos a llevar : "))

resultado = producto * cantidad

iva = producto * 0.16
total = resultado + iva




print(f"El precio unitario de cada platano es de: 2000$\n La cantidad de platanos a llevar es de: {cantidad}\n La suma de los platanos a llevar es de: {resultado}\n Mas el 16% del Iva es de: {total}")