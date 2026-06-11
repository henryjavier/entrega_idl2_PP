#Elabore un programa que lea la hora (HH MM SS) y muestre por 
#pantalla la hora N segundos después. 

# Leer la hora y los segundos a agregar
hh = int(input("Hora (HH): "))
mm = int(input("Minutos (MM): "))
ss = int(input("Segundos (SS): "))
n = int(input("N segundos a agregar: "))

# Sumar los segundos
ss = ss + n

# Ajustar segundos
if ss >= 60:
    mm = mm + (ss // 60)
    ss = ss % 60

# Ajustar minutos
if mm >= 60:
    hh = hh + (mm // 60)
    mm = mm % 60

# Ajustar horas
if hh >= 24:
    hh = hh % 24

print("Nueva hora:", hh, ":", mm, ":", ss)