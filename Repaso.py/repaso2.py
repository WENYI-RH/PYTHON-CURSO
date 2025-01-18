peso = float(input("Indique su peso (en kg): "))
estatura = float(input("Indique su estatura (en metros): "))

# Calcular IMC
IMC = peso / (estatura ** 2)

# Clasificar el resultado
if IMC < 18.5:
    clasificacion = "Bajo peso (flaco)"
elif 18.5 <= IMC < 24.9:
    clasificacion = "Peso normal"
elif 25 <= IMC < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad (gordo)"

# Mostrar el resultado
print(f"Tu índice de masa corporal es: {IMC:.2f}")
print(f"Clasificación: {clasificacion}")