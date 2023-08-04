def factorial_iterativo(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input('Ingrese un número para calcular su factorial: '))
if numero < 0:
    print('El factorial no está definido para números negativos.')
else:
    factorial = factorial_iterativo(numero)
    print('El factorial de' ,numero, 'es:', factorial)
