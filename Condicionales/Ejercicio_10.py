#10. Leer el número de llantas de una compra y mostrar el valor que debe pagarse. 
#El almacén las vende con la siguiente política: Si se compran menos de 6 llantas, el 
#precio unitario es $240000. Si se compran 6 o 7, el precio unitario es $221000, y si se 
#compran más de 7 llantas, el precio unitario es $180000.

numero_llantas = int(input("Ingrese el número de llantas que desea comprar: "))

precio_unitario = 0

if numero_llantas < 6:
    precio_unitario = 240000
elif 6 <= numero_llantas <= 7:
    precio_unitario = 221000
else:
    precio_unitario = 180000

valor_total = numero_llantas * precio_unitario

print(f"El valor total a pagar por {numero_llantas} llantas es: ${valor_total}")
