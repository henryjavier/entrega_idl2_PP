#Calcular el producto utilizando arrays: 100 x 98 x 96 x 94 x . . . x 1 en 
#este orden. 

# Crear el array
numeros = []

for i in range(100, 0, -2):
    numeros.append(i)

# Agregar el 1 al final
numeros.append(1)

# Calcular el producto
producto = 1

for numero in numeros:
    producto *= numero

# Mostrar el array
print("Array:")
print(numeros)

# Mostrar el resultado
print("Producto =", producto)