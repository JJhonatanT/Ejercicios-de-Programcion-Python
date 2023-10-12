#10. Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no. 
#Un número primo (o primo) es un número natural mayor que 1 y que no tiene divisores positivos aparte de 1 y sí mismo.

def numero_primo (numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

numero = int(input("Ingresa un número para verificar si es primo: "))

if numero_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
