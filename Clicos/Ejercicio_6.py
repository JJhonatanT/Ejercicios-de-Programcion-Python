#6. Escriba un programa para mostrar el patrón como triángulo con un asterisco. El patrón como:

'''
*
**
***
****
*****
****
***
**
*
'''

tamaño_triangulo = 5


for sup_trianguilo in range(1, tamaño_triangulo + 1):
    for contador in range(sup_trianguilo):
        print('*', end='')
    print()


for infe_triangulo in range(tamaño_triangulo - 1, 0, -1):
    for contador in range(infe_triangulo):
        print('*', end='')
    print()
