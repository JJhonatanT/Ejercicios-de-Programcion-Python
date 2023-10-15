#4. Escriba una clase de Python para implementar pow(x, n).

class Pow:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result

calcular = Pow()
x = 2.0
n = 10
resultado = calcular.myPow(x, n)
print(f"{x} elevado a la potencia {n} es igual a {resultado}")
