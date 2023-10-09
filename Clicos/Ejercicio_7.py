#7. Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número. El patrón como:


'''
1
12
123
1234
12345
'''


tamaño_triangulo = 5


for fila in range(1, tamaño_triangulo + 1):
    for contador in range(1, fila + 1):
        print(contador, end='')
    print()
