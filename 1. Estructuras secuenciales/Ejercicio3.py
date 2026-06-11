# Ejercicio 3: Porcentaje de inversión

#Tres personas deciden invertir su dinero para fundar una empresa. Cada
#una de ellas invierte una cantidad distinta. Obtener el porcentaje que
#cada uno invierte con respecto a la cantidad total invertida.

p1 = float(input("Inversión persona 1: "))
p2 = float(input("Inversión persona 2: "))
p3 = float(input("Inversión persona 3: "))

total = p1 + p2 + p3

print("Persona 1:", p1 * 100 / total, "%")
print("Persona 2:", p2 * 100 / total, "%")
print("Persona 3:", p3 * 100 / total, "%")