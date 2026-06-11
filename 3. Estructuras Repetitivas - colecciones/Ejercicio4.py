#De una lista de N números determinar simultáneamente el máximo y 
#mínimo número. 

# Inicio
# Leer N
N = int(input("Ingrese la cantidad total de números (N): "))

# Leer el primer número
num = int(input("Ingrese el número 1: "))

# Inicializar maximo y minimo con el primer valor leído
maximo = num
minimo = num

# Para i desde 2 hasta N hacer (en Python, range llega hasta N-1, por eso usamos N + 1)
for i in range(2, N + 1):
    # Leer num
    num = int(input(f"Ingrese el número {i}: "))
    
    # Si num > maximo Entonces
    if num > maximo:
        maximo = num
        
    # Si num < minimo Entonces
    if num < minimo:
        minimo = num

# FinPara

# Mostrar maximo y minimo
print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)

# Fin