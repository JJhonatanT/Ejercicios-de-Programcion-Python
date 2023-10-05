#7. Conversión de temperaturas. Crear un menú de opciones. 

def convertir_temperatura():
    print("1. Fahrenheit a Celsius")
    print("2. Fahrenheit a Kelvin")
    print("3. Fahrenheit a Rankine")
    print("4. Fahrenheit a Réaumur")
    print("5. Celsius a Fahrenheit")
    print("6. Celsius a Kelvin")
    print("7. Celsius a Rankine")
    print("8. Celsius a Réaumur")
    print("9. Kelvin a Celsius")
    print("10. Kelvin a Fahrenheit")
    print("11. Kelvin a Rankine")
    print("12. Kelvin a Réaumur")
    print("13. Rankine a Celsius")
    print("14. Rankine a Fahrenheit")
    print("15. Rankine a Kelvin")
    print("16. Rankine a Réaumur")
    print("17. Réaumur a Celsius")
    print("18. Réaumur a Fahrenheit")
    print("19. Réaumur a Kelvin")
    print("20. Réaumur a Rankine")
    print("0. Salir")

opciones_validas = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

while True:
    convertir_temperatura()
    opcion = input("Ingrese una opción: ")

    if opcion not in opciones_validas:
        print("Opción inválida. Por favor, ingrese una opción válida.\n")
        continue

    if opcion == "0":
        print("¡Hasta luego!")
        break

    temperatura = float(input("Ingrese el valor de la temperatura: "))

    if opcion == "1":
        celsius = (temperatura - 32) / 1.8
        print("El resultado es", celsius, "grados Celsius.")
    elif opcion == "2":
        kelvin = (temperatura + 459.67) / 1.8
        print("El resultado es", kelvin, "grados Kelvin.")
    elif opcion == "3":
        rankine = temperatura + 459.67
        print("El resultado es", rankine, "grados Rankine.")
    elif opcion == "4":
        reaumur = (temperatura - 32) / 2.25
        print("El resultado es", reaumur, "grados Réaumur.")
    elif opcion == "5":
        fahrenheit = temperatura * 1.8 + 32
        print("El resultado es", fahrenheit, "grados Fahrenheit.")
    elif opcion == "6":
        kelvin = temperatura + 273.15
        print("El resultado es", kelvin, "grados Kelvin.")
    elif opcion == "7":
        rankine = temperatura * 1.8 + 32 + 459.67
        print("El resultado es", rankine, "grados Rankine.")
    elif opcion == "8":
        reaumur = temperatura * 0.8
        print("El resultado es", reaumur, "grados Réaumur.")
    elif opcion == "9":
        celsius = temperatura - 273.15
        print("El resultado es", celsius, "grados Celsius.")
    elif opcion == "10":
        fahrenheit = temperatura * 1.8 - 459.67
        print("El resultado es", fahrenheit, "grados Fahrenheit.")
    elif opcion == "11":
        rankine = temperatura * 1.8
        print("El resultado es", rankine, "grados Rankine.")
    elif opcion == "12":
        reaumur = (temperatura - 273.15) * 0.8
        print("El resultado es", reaumur, "grados Réaumur.")
    elif opcion == "13":
        celsius = (temperatura - 32 - 459.67) / 1.8
        print("El resultado es", celsius, "grados Celsius.")
    elif opcion == "14":
        fahrenheit = temperatura - 459.67
        print("El resultado es", fahrenheit, "grados Fahrenheit.")
    elif opcion == "15":
        kelvin = temperatura / 1.8
        print("El resultado es", kelvin, "grados Kelvin.")
    elif opcion == "16":
        reaumur = (temperatura - 32 - 459.67) / 2.25
        print("El resultado es", reaumur, "grados Réaumur.")
    elif opcion == "17":
        celsius = temperatura * 1.25
        print("El resultado es", celsius, "grados Celsius.")
    elif opcion == "18":
        fahrenheit = temperatura * 2.25 + 32
        print("El resultado es", fahrenheit, "grados Fahrenheit.")
    elif opcion == "19":
        kelvin = temperatura * 1.25 + 273.15
        print("El resultado es", kelvin, "grados Kelvin.")
    elif opcion == "20":
        rankine = temperatura * 2.25 + 32 + 459.67
        print("El resultado es", rankine, "grados Rankine.")
    
    print() 