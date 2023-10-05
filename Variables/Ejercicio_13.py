#13. Solicitar tiempo en segundos y transformar a horas y minutos. 

tiempo_s = int(input("Ingrese un tiempo en segundos: "))

horas = tiempo_s // 3600
minutos = (tiempo_s % 3600) // 60
segundos = tiempo_s % 60

print(f"Tiempo ingresado: {tiempo_s} segundos")
print(f"Horas: {horas}h, Minutos: {minutos}m, Segundos: {segundos}s")
