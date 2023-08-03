import math

def calcular_area_circulo(radio):
    if radio < 0:
        raise ValueError("El radio del círculo no puede ser negativo.")
    area = math.pi * (radio ** 2)
    return area

radio_del_circulo = float(input('ingrese el radio del circulo: '))
area_del_circulo = calcular_area_circulo(radio_del_circulo)
print("El área del círculo con radio", radio_del_circulo, "es:", area_del_circulo)
