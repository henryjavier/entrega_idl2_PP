#Hacer un programa que permita ingresar un conjunto de N números y un 
#numero más X mostrar como resultado: 
#• Porcentaje de números menores que X. 
#• Porcentaje de números mayores de X. 
#• Porcentaje de números iguales de X. 
#• Porcentaje de números comprendidos entre 1 y X. 
#• Porcentaje de números que no cumple ninguna condición. 

def main():
    # Leer N y X
    try:
        N = int(input("Ingrese la cantidad de números a procesar (N): "))
        X = float(input("Ingrese el valor de referencia (X): "))
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")
        return

    # Inicializar contadores
    menor = 0
    mayor = 0
    igual = 0
    entre = 0
    ninguno = 0

    # Bucle Para i desde 1 hasta N
    for i in range(N):
        try:
            num = float(input(f"Ingrese el número {i + 1}: "))
        except ValueError:
            print("Valor no válido, se omitirá este ingreso.")
            continue

        # Condiciones
        if num < X:
            menor += 1
        
        if num > X:
            mayor += 1
        
        if num == X:
            igual += 1
        
        if 1 <= num <= X:  # En Python se pueden encadenar comparaciones
            entre += 1
        
        if num < 1:
            ninguno += 1

    # Calcular porcentajes (evitando división por cero)
    if N > 0:
        por_menor = (menor * 100) / N
        por_mayor = (mayor * 100) / N
        por_igual = (igual * 100) / N
        por_entre = (entre * 100) / N
        por_ninguno = (ninguno * 100) / N

        # Mostrar porcentajes con 2 decimales
        print("\n--- Resultados ---")
        print(f"Porcentaje menor que X:     {por_menor:.2f}%")
        print(f"Porcentaje mayor que X:     {por_mayor:.2f}%")
        print(f"Porcentaje igual a X:       {por_igual:.2f}%")
        print(f"Porcentaje entre 1 y X:     {por_entre:.2f}%")
        print(f"Porcentaje menor que 1:     {por_ninguno:.2f}%")
    else:
        print("N debe ser mayor que 0 para calcular los porcentajes.")

if __name__ == "__main__":
    main()