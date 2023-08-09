class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

mi_auto = Vehículo(200, 50000)

print("Velocidad máxima:", mi_auto.velocidad_maxima)
print("Kilometraje:", mi_auto.kilometraje)
