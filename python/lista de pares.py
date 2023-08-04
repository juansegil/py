def generar_lista_pares():
    lista_pares = []
    for num in range(2, 101, 2):
        lista_pares.append(num)
    return lista_pares

lista_pares = generar_lista_pares()

print(lista_pares)
