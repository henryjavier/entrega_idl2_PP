#Hacer un programa que muestre un cronometro (hh:mm:ss), indicando
#las horas, minutos y segundos(Considerar que el tiempo no será exacto
#al de un cronometro real solo será referencial).

# Cronómetro referencial (hh:mm:ss)

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")