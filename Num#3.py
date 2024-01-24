# Solicitar al usuario que ingrese tres voltajes distintos
voltaje1 = float(input("Ingrese voltaje 1: "))
voltaje2 = float(input("Ingrese voltaje 2: "))
voltaje3 = float(input("Ingrese voltaje 3: "))

# Calcular el promedio de los voltajes
promedio = (voltaje1 + voltaje2 + voltaje3) / 3

# Verificar si el promedio es menor a 115 y mostrar el mensaje correspondiente
if promedio < 115:
    print("<VOLTAJE CORRECTO")
# Verificar si el promedio es mayor a 115 y menor a 220 y mostrar el mensaje correspondiente
elif promedio > 115 and promedio < 220:
    print("<ALTO VOLTAJE=")
# El promedio es mayor a 220, mostrar el mensaje correspondiente
else:
    print("< PELIGRO =")