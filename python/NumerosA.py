import random

def generar_lista_numeros_aleatorios(cantidad, rango_inicio, rango_fin):
    lista_numeros = [random.randint(rango_inicio, rango_fin) for _ in range(cantidad)]
    return lista_numeros

cantidad_numeros = int(input('ingrese la cantidad de numeros aleatorios que desea  obtener: '))    
rango_inicio = int(input('ingrese el limite de rango menor de  los numeros: '))       
rango_fin = int(input('ingrese el limite de rango mayor de  los numeros: '))       

lista_aleatoria = generar_lista_numeros_aleatorios(cantidad_numeros, rango_inicio, rango_fin)
print("Lista de números aleatorios:", lista_aleatoria)