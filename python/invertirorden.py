def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

elementos_str = input("Ingresa los elementos de la lista separados por espacios: ")

lista_elementos = elementos_str.split()

lista_numeros = [int(num) for num in lista_elementos]

lista_invertida = invertir_lista(lista_numeros)

print("Lista original:", lista_numeros)
print("Lista invertida:", lista_invertida)
