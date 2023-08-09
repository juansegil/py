import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def calcular_perímetro(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base == altura

esquina_sup_izq = Punto(9, 17)
esquina_inf_der = Punto(5, 9)

mi_rectangulo = Rectángulo(esquina_sup_izq, esquina_inf_der)

print("Perímetro:", mi_rectangulo.calcular_perímetro())
print("Área:", mi_rectangulo.calcular_area())

if mi_rectangulo.es_cuadrado():
    print("Es un cuadrado.")
else:
    print("No es un cuadrado.")