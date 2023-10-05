#13. Un reporte de salud muestra una tabla diferente del índice de masa corporal IMC de una persona 
#que se calcula con la fórmula IMC=P/(E*E) en donde P es el peso en Kg. y E es la estatura en metros. 
#Lea un valor de P y de E, calcule el IMC y muestre su estado según la siguiente tabla:

peso = float(input("Ingrese el peso en Kg: "))
estatura = float(input("Ingrese la estatura en metros: "))

imc = peso / (estatura ** 2)

if imc < 18.5:
    estado = "Desnutrido"
elif imc < 25:
    estado = "Normal"
elif imc < 30:
    estado = "Sobrepeso"
elif imc < 35:
    estado = "Obesidad Grado 1"
elif imc < 40:
    estado = "Obesidad Grado 2"
else:
    estado = "Obesidad Grado 3"

print("El IMC es:", imc)
print("Estado: ", estado)