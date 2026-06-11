#Ejercicio 10: Cajero automático

#Se necesita saber la cantidad de dinero que un cajero automático debe 
#proporcionar en diferentes denominaciones, teniendo en cuenta que el 
#usuario debe ingresar la cantidad a retirar y el cajero tiene disponible las 
#siguientes denominaciones de dinero: 200, 100, 50, 20, 10, 5, 1. Se debe 
#buscar entregar la menor cantidad de dinero por parte del cajero. 

monto = int(input("Monto a retirar: "))

d200 = monto // 200
monto %= 200

d100 = monto // 100
monto %= 100

d50 = monto // 50
monto %= 50

d20 = monto // 20
monto %= 20

d10 = monto // 10
monto %= 10

d5 = monto // 5
monto %= 5

d1 = monto

print("Billetes de 200:", d200)
print("Billetes de 100:", d100)
print("Billetes de 50:", d50)
print("Billetes de 20:", d20)
print("Billetes de 10:", d10)
print("Monedas de 5:", d5)
print("Monedas de 1:", d1)