def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

grados_fahrenheit = int(input('ingrese los grado fahrenheit:  '))
grados_celsius = fahrenheit_a_celsius(grados_fahrenheit)
print(grados_fahrenheit, "grados Fahrenheit son equivalentes a", grados_celsius, "grados Celsius.")
