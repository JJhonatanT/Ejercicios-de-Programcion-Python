#10. Escriba un programa para mostrar un patrón como Z con asteriscos. 

'''
*******
     *
    *
   *
  *
 *
*******
'''

altura = 5

for i in range(altura):
    for j in range(altura):
        if i == 0 or i == altura - 1:
            print('*', end=' ')
        elif i + j == altura - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


