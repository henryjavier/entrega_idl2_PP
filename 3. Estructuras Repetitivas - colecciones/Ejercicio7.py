#Ejercicio 7: Desarrollo de factoriales
#Crea una aplicación que pida dos números y calcule su factorial de cada 
#número, pero el programa también tiene que indicar hasta que valor 
#serian. Ejemplo: 
#7!   > 1x2x3x4x5x6x7 
#10! > 1x2x3x4x5x6x7x8x9x10 
#>> son iguales hasta el múltiplo 7 


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Mostrar el desarrollo del primer factorial
print(f"\n{num1}! > ", end="")
for i in range(1, num1 + 1):
    if i < num1:
        print(i, end="x")
    else:
        print(i, end="")

# Mostrar el desarrollo del segundo factorial
print(f"\n{num2}! > ", end="")
for i in range(1, num2 + 1):
    if i < num2:
        print(i, end="x")
    else:
        print(i, end="")

# Determinar hasta qué múltiplo son iguales
if num1 < num2:
    limite = num1
else:
    limite = num2

print(f"\n\nSon iguales hasta el múltiplo {limite}")