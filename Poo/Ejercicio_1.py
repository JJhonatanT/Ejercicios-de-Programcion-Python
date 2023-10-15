#1. Escriba una clase que represente un vehículo con métodos y atributos. Dentro atributos cree uno 
#llamado “placa” y en los métodos cree uno que permita determinar de acuerdo con el día, si el vehículo 
#tiene restricción por pico y placa o no, en la ciudad de Bogotá. 

import datetime

class Vehiculo:
    def __init__(self, placa, fecha):
        self.placa = placa
        self.fecha = fecha

    def pico_placa(self):
        ultimo_digito_placa = int(self.placa[-1])
        dia_semana = self.fecha.weekday()
        if dia_semana in [1, 3] and ultimo_digito_placa in [0, 1]:
            return True
        elif dia_semana in [2, 4] and ultimo_digito_placa in [2, 3]:
            return True
        elif dia_semana == 5 and ultimo_digito_placa in [4, 5]:
            return True
        else:
            return False


placa = input("Ingresa la placa del vehículo: ")


fecha_actual = datetime.date.today()

vehiculo = Vehiculo(placa, fecha_actual)
tiene_restriccion = vehiculo.pico_placa()

if tiene_restriccion:
    print(f"El vehículo con placa {placa} tiene restricción de pico y placa hoy.")
else:
    print(f"El vehículo con placa {placa} no tiene restricción de pico y placa hoy.")
