#Ejercicio 9: Descuento por cantidad de camisas

#Permita calcular el total a pagar por la compra de N camisas. Si se 
#compran entre 1 a 4 camisas se aplica un descuento del 12.5%, si se 
#compra una cantidad comprendida entre 5 y 8 camisas se aplica un 
#descuento del 20% y si se compran cantidades mayores, se aplica un 
#descuento del 31.5% sobre el total de la compra. Debe imprimirse en 
#pantalla la compra final sin descuento, monto del descuento y la 
#compra con descuento. 

cantidad_camisas = int(input("Ingrese cantidad de camisas: "))
precio_camisa = float(input("Ingrese precio por camisa: "))

total = cantidad_camisas * precio_camisa

if 1 <= cantidad_camisas <= 4:
    descuento = total * 0.125
elif 5 <= cantidad_camisas <= 8:
    descuento = total * 0.20
else:
    descuento = total * 0.315

total_pagar = total - descuento

print("Compra sin descuento:", total)
print("Monto descuento:", descuento)
print("Total a pagar:", total_pagar)