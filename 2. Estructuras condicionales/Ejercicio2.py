# Caso 2 - Mayor y menor de tres numeros
# Se usan estructuras condicionales para practicar la logica
# (Python tambien tiene max() y min(), pero aqui se resuelve con if).

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))

if a >= b and a >= c:
    mayor = a
elif b >= c:
    mayor = b
else:
    mayor = c

if a <= b and a <= c:
    menor = a
elif b <= c:
    menor = b
else:
    menor = c

print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")