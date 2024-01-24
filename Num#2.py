import math

# Función para calcular el área de un triángulo equilátero
def calcular_area(lado):
    area = (math.sqrt(3) / 4) * lado ** 2
    return area

# Solicitar al usuario el tamaño del lado del triángulo
lado = float(input("Ingrese el tamaño del lado del triángulo equilátero: "))

# Validar que el lado del triángulo sea mayor a cero
if lado > 0:
    # Calcular el área del triángulo
    area = calcular_area(lado)

    # Verificar si el área es mayor a 1000
    if area > 1000:
        print("El área del triángulo es:", area)
        print("¡DATOS NO VÁLIDOS! El área es mayor a 1000.")
    else:
        print("El área del triángulo es:", area)
else:
    print("Valor inválido. El lado del triángulo debe ser mayor que cero.")
