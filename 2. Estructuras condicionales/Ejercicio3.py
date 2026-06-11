# Caso 3 - Calculo de impuesto a tributar
# Tributa si es mayor de 18 anios Y gana 3000 o mas. Monto = 5% del ingreso.

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))

if edad > 18 and ingresos >= 3000:
    monto = ingresos * 0.05
    print("El usuario SI debe tributar.")
    print(f"Monto a tributar: S/ {monto:.2f}")
else:
    print("El usuario NO debe tributar.")