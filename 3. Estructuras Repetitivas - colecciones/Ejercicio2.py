#Realizar un algoritmo que permita pedir 10 números y determine e 
#imprima cuantos son pares, impares, positivos, neutros y negativos. 

# Inicialización de contadores
cont_par = 0
cont_impar = 0
cont_pos = 0
cont_neg = 0
cont_neu = 0

# Bucle para iterar 10 veces (de 1 a 10 inclusive)
for i in range(1, 11):
    # Lectura del número (se convierte a entero, usa float si esperas decimales)
    num = int(input(f"Ingrese el número {i}: "))
    
    # Verificación de par o impar
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
        
    # Verificación de positivo, negativo o neutro
    if num > 0:
        cont_pos += 1
    elif num < 0:
        cont_neg += 1
    else:
        cont_neu += 1

# Mostrar los resultados
print("\n--- Resultados ---")
print(f"Cantidad de números pares: {cont_par}")
print(f"Cantidad de números impares: {cont_impar}")
print(f"Cantidad de números positivos: {cont_pos}")
print(f"Cantidad de números negativos: {cont_neg}")
print(f"Cantidad de números neutros: {cont_neu}")