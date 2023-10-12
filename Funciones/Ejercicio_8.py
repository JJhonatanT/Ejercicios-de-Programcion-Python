#8. Escriba una función de Python que acepte una cadena y calcule el número de letras mayúsculas y minúsculas. 

def contar_m_n(cadena):
    mayusculas = 0
    minusculas = 0

    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1

    return mayusculas, minusculas


cadena = input("Ingresa un texto que incluya masyusculas y minusculas: ")
mayusculas, minusculas = contar_m_n(cadena)
print(f"Número de letras mayúsculas: {mayusculas}")
print(f"Número de letras minúsculas: {minusculas}")

