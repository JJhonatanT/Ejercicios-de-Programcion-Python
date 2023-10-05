#14. 14. El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico 
#se calcula con la fórmula:
    #Género femenino (1): número de pulsaciones = (220 - edad en años)/10
    #Género masculino (2): número de pulsaciones = (210 - edad en años)/10
    #Lea la edad y el género y muestre el número de pulsaciones.

edad = int(input("Ingrese su edad en años: "))
genero = int(input("Ingrese su género (1 para femenino, 2 para masculino): "))

if genero == 1:
    pulsaciones = (220 - edad) / 10
elif genero == 2:
    pulsaciones = (210 - edad) / 10
else:
    print("Género no válido. Ingrese 1 para femenino o 2 para masculino.")
    pulsaciones = None

if pulsaciones is not None:
    print(f"El número de pulsaciones por cada 10 segundos de ejercicio es: {pulsaciones}")
