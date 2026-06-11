#Ejercicio 10: Costo de llamada internacional

codigo = int(input("Ingrese código de zona: "))
minutos = float(input("Ingrese minutos hablados: "))

if codigo == 10:
    zona = "America del Norte"
    costo = 2.2

elif codigo == 12:
    zona = "America Central"
    costo = 2.5

elif codigo == 20:
    zona = "America del Sur"
    costo = 1.2

elif codigo == 22:
    zona = "Asia"
    costo = 3.5

elif codigo == 30:
    zona = "Europa"
    costo = 3.0

elif codigo == 32:
    zona = "Africa"
    costo = 3.2

else:
    print("Código inválido")
    exit()

total = minutos * costo

print("Zona:", zona)
print("Costo por minuto:", costo)
print("Costo total:", total)