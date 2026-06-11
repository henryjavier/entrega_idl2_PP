# Ejercicio 5: Inversión bancaria

# Suponga que un individuo desea invertir su capital en un banco y desea
# saber cuánto dinero ganará después de un año si el banco paga a razón
# de 2% mensual.

capital = float(input("Capital inicial: "))

monto_final = capital * (1 + 0.02) ** 12
ganancia = monto_final - capital

print("Monto final:", monto_final)
print("Ganancia:", ganancia)