#10. Programa que permita determinar el salario a pagar a un empleado, teniendo como entradas el salario diario y el 
#número de días trabajados. Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% 
#por concepto de salud.

salario_diario = float(input("Ingrese el salario diario por favor: "))
dias_trabajados = int(input("Ingrese el número de días trabajados por favor: "))


salario_b = salario_diario * dias_trabajados


pension = salario_b * 0.10
salud = salario_b * 0.15


salario_neto = salario_b - pension - salud


print(f"Salario bruto: ${salario_b}")
print(f"Deducción de pensión (10%): ${pension}")
print(f"Deducción de salud (15%): ${salud}")
print(f"Salario neto a pagar: ${salario_neto}")
