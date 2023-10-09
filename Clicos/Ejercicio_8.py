#8. Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1.

'''
   1
  2 3
 4 5 6
7 8 9 10
'''

n_filas = 4
numero = 1

for i in range(1, n_filas + 1):
    for contador in range(n_filas - i):
        print(" ", end=" ")
    
    for contador in range(i):
        print(numero, end=" ")
        numero += 1
    
    print()
