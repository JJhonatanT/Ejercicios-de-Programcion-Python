#11. Escriba un programa Python para imprimir los números pares de una lista determinada.

def numeros_pares(lista):
    for numero in lista:
        if numero % 2 == 0:
            print(numero)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Números pares en la lista:")
numeros_pares(lista)
