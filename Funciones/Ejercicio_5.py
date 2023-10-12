#5. Escriba un programa Python para invertir una cadena. Cadena de ejemplo: "1234abcd" Resultado esperado: "dcba4321"

def invertir(cadena):
    return cadena[::-1]

cadena_muestra = "1234abcd"

resultado = invertir(cadena_muestra)
print(resultado)
