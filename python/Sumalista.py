def calcular_suma_lista(lista):
    suma = sum(lista)
    return suma

numeros_str = input("Ingresa los números separados por espacios: ")

lista_numeros = [int(num) for num in numeros_str.split()]

suma_total = calcular_suma_lista(lista_numeros)

print("La suma de los números en la lista es:", suma_total)
