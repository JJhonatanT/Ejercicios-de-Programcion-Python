#12. Un local vende sus productos con la siguiente promoción. Si compra hasta 5 artículos, no hay descuento. 
#Si compra más de 5 artículos, pero menos de 10, el precio unitario se reduce en 5%. Si compra 10 o más 
#artículos, el precio unitario se reduce en 8%. Ingrese un dato de cantidad y el valor del precio unitario original. 
#Calcule y muestre el valor total a pagar. 

cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
precio_unitario_original = float(input("Ingrese el precio unitario original: "))

precio_total = cantidad_articulos * precio_unitario_original

if cantidad_articulos > 5 and cantidad_articulos < 10:
    descuento = 0.05  
elif cantidad_articulos >= 10:
    descuento = 0.08  
else:
    descuento = 0.00  

precio_total_con_descuento = precio_total - (precio_total * descuento)

print(f"El valor total a pagar es: ${precio_total_con_descuento}")
