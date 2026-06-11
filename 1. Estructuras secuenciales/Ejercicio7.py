#Ejercicio 7: Cobro de estacionamiento

#Un estacionamiento requiere determinar el cobro que debe aplicar a las 
#personas que lo utilizan. Considere que el cobro es con base en las 
#horas que lo disponen y que las fracciones de hora se toman como 
#completas y realice un programa que permita determinar el cobro. El 
#pago por hora es de S/5.00 y el pago por los minutos restantes de S/0.10 
#por minuto. 


# Entrada de datos
horas = int(input("Ingrese las horas de permanencia: "))
minutos = int(input("Ingrese los minutos adicionales: "))

# Cálculo del pago
pago_horas = horas * 5.00
pago_minutos = minutos * 0.10

# Total a pagar
total_pagar = pago_horas + pago_minutos

# Salida de resultados
print("\n========== REPORTE DE PAGO ==========")
print(f"Horas utilizadas      : {horas}")
print(f"Minutos adicionales   : {minutos}")
print(f"Pago por horas        : S/ {pago_horas:.2f}")
print(f"Pago por minutos      : S/ {pago_minutos:.2f}")
print(f"Total a pagar         : S/ {total_pagar:.2f}")
print("=====================================")
