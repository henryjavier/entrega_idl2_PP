#Desarrolla un programa que para N (con un mínimo de 5 y máximo de 
#20) estudiantes permita leer sus notas (calificación) obtenidas en un 
#curso. Se debe validar que la nota tenga un valor entre 0 y 20. Se sabe 
#que la mínima nota aprobatoria es 13. Al final calcule: 
#a) La mayor nota 
#b) La menor nota 
#c) La cantidad de alumnos que obtuvieron la mayor nota 
#d) La cantidad de alumnos que obtuvieron la menor nota 
#e) El promedio de notas del salón 
#f) La cantidad de notas pares 
#g) La cantidad de notas impares 
#h) La cantidad de alumnos aprobados 
#i) La cantidad de alumnos desaprobados 
#j) El porcentaje de alumnos aprobados 
#k) El porcentaje de alumnos desaprobados 

# Leer cantidad de estudiantes
while True:
    n = int(input("Ingrese la cantidad de estudiantes (5 a 20): "))
    if 5 <= n <= 20:
        break
    print("Error. Debe ingresar un valor entre 5 y 20.")

# Array para almacenar las notas
notas = []

# Ingreso de notas
for i in range(n):
    while True:
        nota = int(input(f"Ingrese la nota del estudiante {i + 1}: "))
        if 0 <= nota <= 20:
            notas.append(nota)
            break
        print("Error. La nota debe estar entre 0 y 20.")

# Inicialización de variables
mayor = notas[0]
menor = notas[0]
suma = 0
pares = 0
impares = 0
aprobados = 0
desaprobados = 0

# Recorrer el array
for nota in notas:
    suma += nota

    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

    if nota % 2 == 0:
        pares += 1
    else:
        impares += 1

    if nota >= 13:
        aprobados += 1
    else:
        desaprobados += 1

# Contar repeticiones de la mayor y menor nota
cant_mayor = 0
cant_menor = 0

for nota in notas:
    if nota == mayor:
        cant_mayor += 1

    if nota == menor:
        cant_menor += 1

# Cálculos finales
promedio = suma / n
porc_aprobados = (aprobados * 100) / n
porc_desaprobados = (desaprobados * 100) / n

# Resultados
print("\n===== REPORTE FINAL =====")
print("Mayor nota:", mayor)
print("Menor nota:", menor)
print("Cantidad de alumnos con la mayor nota:", cant_mayor)
print("Cantidad de alumnos con la menor nota:", cant_menor)
print("Promedio del salón:", round(promedio, 2))
print("Cantidad de notas pares:", pares)
print("Cantidad de notas impares:", impares)
print("Cantidad de aprobados:", aprobados)
print("Cantidad de desaprobados:", desaprobados)
print("Porcentaje de aprobados:", round(porc_aprobados, 2), "%")
print("Porcentaje de desaprobados:", round(porc_desaprobados, 2), "%")