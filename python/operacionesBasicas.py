def suma(a, b):
    suma= a + b
    return suma

def resta(a, b):
    resta= a - b
    return resta

def multiplicacion(a, b):
    muliplicacion= a * b
    return muliplicacion

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."


def main():
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        print(f"\nSuma: {suma(numero1, numero2)}")
        print(f"Resta: {resta(numero1, numero2)}")
        print(f"Multiplicación: {multiplicacion(numero1, numero2)}")
        print(f"División: {division(numero1, numero2)}")
    except ValueError:
        print("Error: Ingrese números válidos.")

if __name__ == "__main__":
    main()
