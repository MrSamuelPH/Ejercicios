# Inicializar la suma de los voltajes
suma_voltajes = 0

# Pedir al usuario que ingrese los cinco voltajes
for i in range(5):
    voltaje = float(input("Ingrese el voltaje: "))
    suma_voltajes += voltaje

# Calcular el promedio de los voltajes
promedio = suma_voltajes / 5

# Verificar si el promedio es mayor a 220 o no
if promedio > 220:
    print("ALTO VOLTAJE =", promedio)
else:
    print("VOLTAJE CORRECTO =", promedio)