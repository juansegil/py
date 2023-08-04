def media_aritmetica_usuario():
    numeros = []
    n = int(input("Ingrese la cantidad de números que desea promediar: "))
    
    if n <= 0:
        raise ValueError("La cantidad de números debe ser mayor a cero.")
    
    for i in range(n):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)
    
    suma = sum(numeros)
    media = suma / n
    return media

try:
    resultado = media_aritmetica_usuario()
    print("La media aritmética es:", resultado)
except ValueError as e:
    print("Error:", e)
