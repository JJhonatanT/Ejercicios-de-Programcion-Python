#9. Programa que permita a un usuario tomar una decisión del tipo de pago a usar. Si la cuenta
#es menor a $150000 pago en efectivo. Si no, si es de $150000 hasta $300000 pago con el celular
#(dinero electrónico). Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito. 
#Caso contrario, pago con#la tarjeta de crédito.

monto_cuenta = float(input("Ingrese el monto de la cuenta: "))

if monto_cuenta < 150000:
    metodo_pago = "Efectivo"
elif 150000 <= monto_cuenta <= 300000:
    metodo_pago = "Celular (dinero electrónico)"
elif 300000 < monto_cuenta <= 600000:
    metodo_pago = "Tarjeta de débito"
else:
    metodo_pago = "Tarjeta de crédito"

print(f"El método de pago es: {metodo_pago}")
