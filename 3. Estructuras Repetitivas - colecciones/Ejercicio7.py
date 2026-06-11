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