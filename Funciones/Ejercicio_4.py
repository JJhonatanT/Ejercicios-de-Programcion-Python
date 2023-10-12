#4. Escriba una función de Python para multiplicar todos los números de una lista. Lista de muestra: 
#(8, 2, 3, -1, 7)Resultado esperado: -336

def multi (lista):
    multi = 1
    for numero in lista:
        multi *= numero
    return multi

lista = [8, 2, 3, -1, 7]

resultado = multi(lista)
print(resultado)
