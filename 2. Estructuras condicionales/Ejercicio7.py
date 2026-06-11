#Calcular el pago de una llamada, el cobro es por el tiempo que ésta 
#dura, de tal forma que los primeros cinco minutos cuestan S/ 1.00 c/u, 
#los siguientes tres, S/0.80 c/u, los siguientes dos minutos, S/0.70 c/u, 3 
#y a partir del décimo minuto, S/0.50 c/u. Además, se carga un 
#impuesto de 3 % cuando es domingo, y 5% si es domingo de turno 
#nocturno. Realice un algoritmo para determinar cuánto debe pagar 
#por cada concepto una persona que realiza una llamada. 

# Entrada de datos
minutos = int(input("Ingrese la duración de la llamada (minutos): "))
domingo = input("¿Es domingo? (S/N): ").upper()

# Cálculo del costo de la llamada
if minutos <= 5:
    costo = minutos * 1.00
elif minutos <= 8:
    costo = 5 * 1.00 + (minutos - 5) * 0.80
elif minutos <= 10:
    costo = 5 * 1.00 + 3 * 0.80 + (minutos - 8) * 0.70
else:
    costo = 5 * 1.00 + 3 * 0.80 + 2 * 0.70 + (minutos - 10) * 0.50

# Cálculo del impuesto
impuesto = 0

if domingo == "S":
    nocturno = input("¿La llamada fue en turno nocturno? (S/N): ").upper()

    if nocturno == "S":
        impuesto = costo * 0.05
    else:
        impuesto = costo * 0.03

# Total a pagar
total = costo + impuesto

# Salida
print("\n--- DETALLE DEL PAGO ---")
print("Costo de la llamada: S/", round(costo, 2))
print("Impuesto: S/", round(impuesto, 2))
print("Total a pagar: S/", round(total, 2))