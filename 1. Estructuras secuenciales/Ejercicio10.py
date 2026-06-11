#Ejercicio 10: Cajero automático

#Se necesita saber la cantidad de dinero que un cajero automático debe 
#proporcionar en diferentes denominaciones, teniendo en cuenta que el 
#usuario debe ingresar la cantidad a retirar y el cajero tiene disponible las 
#siguientes denominaciones de dinero: 200, 100, 50, 20, 10, 5, 1. Se debe 
#buscar entregar la menor cantidad de dinero por parte del cajero. 

# Entrada de datos
monto = int(input("Ingrese el monto a retirar: S/ "))

# Cálculo de denominaciones
billetes_200 = monto // 200
monto = monto % 200

billetes_100 = monto // 100
monto = monto % 100

billetes_50 = monto // 50
monto = monto % 50

billetes_20 = monto // 20
monto = monto % 20

billetes_10 = monto // 10
monto = monto % 10

monedas_5 = monto // 5
monto = monto % 5

monedas_1 = monto

# Salida de resultados
print("\n========== DESGLOSE DEL RETIRO ==========")
print(f"Billetes de S/200 : {billetes_200}")
print(f"Billetes de S/100 : {billetes_100}")
print(f"Billetes de S/50  : {billetes_50}")
print(f"Billetes de S/20  : {billetes_20}")
print(f"Billetes de S/10  : {billetes_10}")
print(f"Monedas de S/5    : {monedas_5}")
print(f"Monedas de S/1    : {monedas_1}")
print("=========================================")