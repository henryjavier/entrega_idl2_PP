# Ejercicio 4: Cálculo de comisiones

# Un vendedor recibe su sueldo base más 25% extra por comisión de sus
#ventas; el vendedor desea saber cuánto dinero recibirá por concepto de
#comisiones por lastres ventas que realiza en el mes y el total que recibirá
#en el mes tomando en cuenta sueldo base y comisiones.

sueldo = float(input("Sueldo base: "))

v1 = float(input("Venta 1: "))
v2 = float(input("Venta 2: "))
v3 = float(input("Venta 3: "))

ventas = v1 + v2 + v3
comision = ventas * 0.25

total = sueldo + comision

print("Comisión:", comision)
print("Total a recibir:", total)