# Ejercicio 6: Cálculo de tiempo vivido

#Realice un programa que representen el algoritmo donde se ingrese la
#edad de una persona para determinar aproximadamente cuántos
#meses, semanas, días y horas ha vivido una persona.

edad = int(input("Edad en años: "))

meses = edad * 12
semanas = edad * 52
dias = edad * 365
horas = dias * 24

print("Meses:", meses)
print("Semanas:", semanas)
print("Días:", dias)
print("Horas:", horas)