def encontrar_maximo_minimo(lista):
    if not lista:
        return None, None
    maximo = minimo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero
    return maximo, minimo

numeros_str = input("Ingresa los números separados por espacios: ")

lista_numeros = [int(num) for num in numeros_str.split()]

maximo, minimo = encontrar_maximo_minimo(lista_numeros)

if maximo is not None and minimo is not None:
    print("El número más grande en la lista es:", maximo)
    print("El número más pequeño en la lista es:", minimo)
else:
    print("La lista está vacía, no se encontraron números más grandes ni más pequeños.")
