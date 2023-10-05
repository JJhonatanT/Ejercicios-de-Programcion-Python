#11. El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado, como se muestra a continuación:
    
    
    #| Tamaño | Precio |
    #| --- | --- |
    #| 1 | $15.000 |
    #| 2 | $24.000 |
    #| 3 | $36.000 |
    
#Si cada ingrediente adicional cuesta $4.000. Escribir un programa que solicite al empleado encargado de registrar las ventas, 
#el tamaño de la pizza y el número de ingredientes adicionales y muestre al cliente el precio que debe pagar.

print("Tamaño de pizza:")
print("1. Pequeña - $15,000")
print("2. Mediana - $24,000")
print("3. Grande - $36,000")

tamaño = int(input("Seleccione el tamaño de la pizza (1, 2 o 3): "))

if tamaño not in [1, 2, 3]:
    print("Tamaño de pizza no válido.")
else:
    ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))

    if tamaño == 1:
        precio_base = 15000
    elif tamaño == 2:
        precio_base = 24000
    elif tamaño == 3:
        precio_base = 36000

    costo_ingredientes = ingredientes_adicionales * 4000

    precio_total = precio_base + costo_ingredientes

    print(f"El precio total de la pizza con {ingredientes_adicionales} ingredientes adicionales es: ${precio_total}")
