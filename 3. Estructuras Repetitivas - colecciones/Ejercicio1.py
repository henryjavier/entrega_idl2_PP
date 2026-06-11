#Calcular la suma y promedio de los números pares e impares por 
#separado ,de 1 hasta N. 

# Leer N
N = int(input("Ingrese el valor de N: "))

# Inicialización de variables
suma_par = 0
suma_impar = 0
cont_par = 0
cont_impar = 0

# Para i desde 1 hasta N hacer
for i in range(1, N + 1):
    # Si i MOD 2 = 0 Entonces
    if i % 2 == 0:
        suma_par += i
        cont_par += 1
    # Sino
    else:
        suma_impar += i
        cont_impar += 1

# Calcular promedios (con validación para evitar división por cero si N=0)

prom_par = suma_par / cont_par if cont_par > 0 else 0
prom_impar = suma_impar / cont_impar if cont_impar > 0 else 0

# Escribir resultados
print("Suma de pares:", suma_par)
print("Promedio de pares:", prom_par)
print("Suma de impares:", suma_impar)
print("Promedio de impares:", prom_impar)