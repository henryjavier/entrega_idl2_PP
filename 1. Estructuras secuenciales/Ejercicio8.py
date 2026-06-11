#Ejercicio 8: Área de un terreno

#Una empresa constructora vende terrenos con la forma A de la figura. 
#Obtener el área respectiva de un terreno de medidas ingresando el valor 
#de los 3 lados.

# Entrada de datos
A = float(input("Ingrese el lado A: "))
B = float(input("Ingrese el lado B: "))
C = float(input("Ingrese el lado C: "))

# Cálculo de áreas
area_rectangulo = B * C
area_triangulo = (B * (A - C)) / 2

# Área total
area_total = area_rectangulo + area_triangulo

# Salida
print("\n========== RESULTADOS ==========")
print(f"Área del rectángulo : {area_rectangulo:.2f}")
print(f"Área del triángulo  : {area_triangulo:.2f}")
print(f"Área total          : {area_total:.2f}")
print("================================")