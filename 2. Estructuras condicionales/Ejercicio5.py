#Determinar mediante el ingreso de los 3 lados de un triángulo, si este 
#es Equilátero (Mostrar el perímetro del), Isósceles (Indicar que lados 
#son Iguales) o Escaleno (triángulo mostrar el área del triángulo). 

# Entrada de datos

lado1 = float(input("Ingrese el lado 1 del triángulo: "))
lado2 = float(input("Ingrese el lado 2 del triángulo: "))
lado3 = float(input("Ingrese el lado 3 del triángulo: "))

# Verificación de tipo de triángulo

if lado1 == lado2 == lado3:
    tipo_triangulo = "Equilátero"
    perimetro = lado1 + lado2 + lado3
    print(f"El triángulo es {tipo_triangulo} y su perímetro es: {perimetro:.2f}")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo_triangulo = "Isósceles"
    lados_iguales = []
    if lado1 == lado2:
        lados_iguales.append("lado 1 y lado 2")
    if lado1 == lado3:
        lados_iguales.append("lado 1 y lado 3")
    if lado2 == lado3:
        lados_iguales.append("lado 2 y lado 3")
    print(f"El triángulo es {tipo_triangulo} y los lados iguales son: {', '.join(lados_iguales)}")

else:
    tipo_triangulo = "Escaleno"

# Cálculo del área usando la fórmula de Herón

    s = (lado1 + lado2 + lado3) / 2  
    
# Semiperímetro

    area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5
    print(f"El triángulo es {tipo_triangulo} y su área es: {area:.2f}")
