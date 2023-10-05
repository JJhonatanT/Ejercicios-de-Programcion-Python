#14. Solicitar al usuario una distancia en metros y transformar a km., cm. o mm. 

d_metros = float(input("Ingrese una distancia en metros: "))

d_kilometros = d_metros / 1000
d_centimetros = d_metros * 100
d_milimetros = d_metros * 1000

print(f"Distancia ingresada: {d_metros} metros")
print(f"Distancia en kilómetros: {d_kilometros} km")
print(f"Distancia en centímetros: {d_centimetros} cm")
print(f"Distancia en milímetros: {d_milimetros} mm")
