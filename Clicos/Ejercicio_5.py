#5. Escriba un programa para mostrar la tabla de multiplicar de un entero dado.

numero1 = int(input("Ingrese un entero para mostrar su tabla de multiplicar: "))


print(f"Tabla de multiplicar del {numero1}:")
for multi in range(1, 11):
    producto = numero1 * multi
    print(f"{numero1} x {multi} = {producto}")
