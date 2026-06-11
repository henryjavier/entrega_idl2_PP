#A una fiesta asistieron personas de diferentes edades y sexos. Construir 
#un algoritmo donde se ingrese los datos de los N asistentes. Calcular:  
#• Cuantas personas asistieron a la fiesta  
#• Cuantos hombres y cuantas mujeres 
#• Promedio de edades por sexo 
#• La edad de la persona de menor y mayor edad que asistió. 
#Nota: El sistema debe permitir al menos el ingreso los datos de una 
#persona y solicitar si se desasea registrar a otra. 

# Inicialización de variables
total_personas = 0
hombres = 0
mujeres = 0

suma_edades_hombres = 0
suma_edades_mujeres = 0

mayor_edad = 0
menor_edad = 0

continuar = "S"

while continuar.upper() == "S":

    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (H/M): ").upper()

    total_personas += 1

    # Determinar mayor y menor edad
    if total_personas == 1:
        mayor_edad = edad
        menor_edad = edad
    else:
        if edad > mayor_edad:
            mayor_edad = edad

        if edad < menor_edad:
            menor_edad = edad

    # Contar hombres y mujeres
    if sexo == "H":
        hombres += 1
        suma_edades_hombres += edad
    elif sexo == "M":
        mujeres += 1
        suma_edades_mujeres += edad

    continuar = input("¿Desea registrar otra persona? (S/N): ")

# Cálculo de promedios
if hombres > 0:
    promedio_hombres = suma_edades_hombres / hombres
else:
    promedio_hombres = 0

if mujeres > 0:
    promedio_mujeres = suma_edades_mujeres / mujeres
else:
    promedio_mujeres = 0

# Resultados
print("\n===== REPORTE DE LA FIESTA =====")
print("Total de personas:", total_personas)
print("Cantidad de hombres:", hombres)
print("Cantidad de mujeres:", mujeres)
print("Promedio de edad de hombres:", promedio_hombres)
print("Promedio de edad de mujeres:", promedio_mujeres)
print("Menor edad:", menor_edad)
print("Mayor edad:", mayor_edad)