#6. Crear un programa con un menú de opciones, que permita calcular las áreas de figuras geométricas
#(cuadrado, rectángulo, triángulo, círculo, rombo y trapecio). 

while True:
    print("Seleccione la figura geométrica a calcular el area:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Rombo")
    print("6. Trapecio")

    opcion = input("Ingrese el número de la figura: ")

    if opcion == "1":
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")
    elif opcion == "2":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        print(f"El área del rectángulo es: {area}")
    elif opcion == "3":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    elif opcion == "4":
        radio = float(input("Ingrese el radio del círculo: "))
        area = 3.14159 * (radio ** 2)
        print(f"El área del círculo es: {area}")
    elif opcion == "5":
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        area = (diagonal_mayor * diagonal_menor) / 2
        print(f"El área del rombo es: {area}")
    elif opcion == "6":
        base_mayor = float(input("Ingrese la base mayor del trapecio: "))
        base_menor = float(input("Ingrese la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        area = ((base_mayor + base_menor) * altura) / 2
        print(f"El área del trapecio es: {area}")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
