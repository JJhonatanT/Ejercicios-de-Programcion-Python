#2. Preguntar al usuario el nombre y la edad, si es mayor o igual a 18 años 
#mostrar el mensaje "Usted es mayor de edad", de lo contrario 
#"Usted es menor de edad". Si el número ingresado es negativo o la edad ingresada 
#es mayor a 100 años, mostrar al usuario un mensaje de ingresar una edad válida.

nombre = input("Ingrese su nombre por favor: ")
edad = int(input("Ingrese su edad por favor: "))

if edad < 0:
    mensaje = "Por favor, ingrese una edad válida."
else:
    if edad <= 100:
        if edad >= 18:
            mensaje = "Usted es mayor de edad."
        else:
            mensaje = "Usted es menor de edad."
    else:
        mensaje = "Por favor, ingrese una edad válida."

print(f"Hola, {nombre}. {mensaje}")
