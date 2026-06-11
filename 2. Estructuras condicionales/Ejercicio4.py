# Caso 4 - Colegiatura con descuento por promedio
# Cada materia cuesta S/100. Si el promedio >= 18 se descuenta el 50%
# sobre la mitad de los cursos; si no, se paga la colegiatura completa.

materias = int(input("Numero de materias: "))
promedio = float(input("Promedio del ultimo periodo: "))

completa = materias * 100

if promedio >= 18:
    descuento = (materias / 2) * 100 * 0.5
    total = completa - descuento
else:
    total = completa

print(f"El alumno debe pagar: S/ {total:.2f}")