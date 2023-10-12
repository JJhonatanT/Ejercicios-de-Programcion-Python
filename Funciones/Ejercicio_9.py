#9. Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista. 


def elementos(lista):
    lista_unica = list(set(lista))
    return lista_unica


lista = [1, 2, 2, 3, 4, 4, 5]
nueva_lista = elementos(lista)
print(nueva_lista)
