#Cuanto pagaría un cliente por una compra con descuento y cuanto sería 
#el cambio que recibiría en un pago en efectivo. Ingresar el monto base, 
#el porcentaje de descuento y el con cuánto dinero está pagando el 
#cliente. 

monto_base = float(input("Monto base de la compra: S/ "))
porcentaje_descuento = float(input("Porcentaje de descuento: % "))
dinero_pagado = float(input("Dinero con el que está pagando el cliente: S/ "))

descuento = monto_base * (porcentaje_descuento / 100)
monto_con_descuento = monto_base - descuento
cambio = dinero_pagado - monto_con_descuento

print("Monto con descuento: S/ ", monto_con_descuento)
print("Cambio a recibir: S/ ", cambio)
