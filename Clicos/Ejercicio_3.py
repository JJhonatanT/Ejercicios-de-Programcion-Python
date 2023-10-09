#3. Escriba un programa para mostrar n términos de número natural y su suma (Fibonacci).

numero = int(input("Ingrese la cantidad de términos de Fibonacci a mostrar: "))

fibonacci = [0, 1]  
suma = 1      

print(f"Los primeros {numero} términos de la serie de Fibonacci son:")
print("Fibonacci(1) = 0")
if numero > 1:
    print("Fibonacci(2) = 1")

for i in range(2, numero):
    siguiente = fibonacci[-1] + fibonacci[-2]  
    fibonacci.append(siguiente)          
    suma += siguiente       

    print(f"Fibonacci({i + 1}) = {siguiente}")

print(f"Suma de los primeros {numero} términos: {suma}")
