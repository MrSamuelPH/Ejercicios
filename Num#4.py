 
def convertir_a_kilometros(distancia_metros):
    distancia_km = distancia_metros / 1000
    return distancia_km

# Solicitar al usuario el valor de la distancia en metros
distancia_metros = float(input("Ingrese la distancia en metros:"))

# Convertir la distancia a kilómetros
distancia_km = convertir_a_kilometros(distancia_metros)

# Imprimir la distancia en kilómetros
print(f"La distancia en kilómetros es: {distancia_km} km")