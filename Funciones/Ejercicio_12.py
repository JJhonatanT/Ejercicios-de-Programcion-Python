#12. Escriba una función de Python que compruebe si una cadena pasada es palíndromo o no. 
#Una palabra o frase que es palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. 
#Por ejemplo: Ana, Anita lava la tina. 

'''
reconocer
oso
salas
la ruta natural
anilina
reconocer
'''


def palindromo(cadena):
    return cadena == cadena[::-1]


cadena = input("Ingresa una palabra o frase para verificar si es un palíndromo: ")

if palindromo(cadena):
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')
