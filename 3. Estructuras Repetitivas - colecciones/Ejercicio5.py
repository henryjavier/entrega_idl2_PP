#Realizar un algoritmo para determinar cuánto ahorrará una persona en 
#un año, si al final de cada mes deposita cantidades variables de dinero; 
#se quiere saber cuánto lleva ahorrado cada vez que haga un deposito 
#en cada mes y luego mostrar el ahorro final de 12 meses. 

ahorro_total = 0
for mes in range(1, 13):
    deposito = float(input("Ingrese el depósito del mes " + str(mes) + ": S/ "))
    ahorro_total = ahorro_total + deposito
    print("Ahorro acumulado hasta el mes", mes, ": S/", ahorro_total)
print("\nAhorro final después de 12 meses: S/", ahorro_total)