# Caso 1 - Pago en la llantera
# Precio: S/150 si se compran menos de 5 llantas; S/120 si son 5 o mas.

cantidad = int(input("Ingrese la cantidad de llantas: "))

if cantidad < 5:
    precio = 150
else:
    precio = 120

total = cantidad * precio
print(f"Total a pagar: S/ {total}")