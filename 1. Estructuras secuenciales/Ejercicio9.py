#Ejercicio 9: Descuento y cambio

#Cuanto pagaría un cliente por una compra con descuento y cuanto sería 
#el cambio que recibiría en un pago en efectivo. Ingresar el monto base, 
#el porcentaje de descuento y el con cuánto dinero está pagando el 
#cliente. 

# Entrada de datos
monto_base = float(input("Ingrese el monto de la compra (S/): "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (%): "))
pago_cliente = float(input("Ingrese el monto con el que paga el cliente (S/): "))

# Cálculos
monto_descuento = monto_base * (porcentaje_descuento / 100)
total_pagar = monto_base - monto_descuento
cambio = pago_cliente - total_pagar

# Salida de resultados
print("\n========== REPORTE DE COMPRA ==========")
print(f"Monto de la compra      : S/ {monto_base:.2f}")
print(f"Descuento aplicado     : {porcentaje_descuento:.2f}%")
print(f"Monto de descuento     : S/ {monto_descuento:.2f}")
print(f"Total a pagar          : S/ {total_pagar:.2f}")
print(f"Pago del cliente       : S/ {pago_cliente:.2f}")
print(f"Cambio a recibir       : S/ {cambio:.2f}")
print("=======================================")