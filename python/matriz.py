def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            num = int(input(f"Ingrese el número para la posición [{i}][{j}]: "))
            fila.append(num)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    try:
        filas = int(input("Ingrese el número de filas de la matriz: "))
        columnas = int(input("Ingrese el número de columnas de la matriz: "))
        if filas <= 0 or columnas <= 0:
            print("Error: Las dimensiones deben ser mayores que cero.")
            return

        matriz = crear_matriz(filas, columnas)
        print("\nLa matriz generada es:")
        imprimir_matriz(matriz)
    except ValueError:
        print("Error: Ingrese un número entero válido para las dimensiones.")

if __name__ == "__main__":
    main()
