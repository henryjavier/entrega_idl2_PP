#Solicite a usuario 3 números enteros (validar que sean diferentes) y 
#en que orden lo desean ver, para luego, mostrarlos a usuario, pero 
#ordenados de manera ascendente o descendente según los que 
#indique el usuario. 

# Ingreso de números
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

# Validar que sean diferentes
if n1 == n2 or n1 == n3 or n2 == n3:
    print("Error: Los números deben ser diferentes.")
else:
    orden = input("¿Desea verlos Ascendente (A) o Descendente (D)? ").upper()

    # Ordenar de menor a mayor
    numeros = [n1, n2, n3]

    if orden == "A":
        numeros.sort()
        print("Números en orden ascendente:", numeros)

    elif orden == "D":
        numeros.sort(reverse=True)
        print("Números en orden descendente:", numeros)

    else:
        print("Opción no válida.")