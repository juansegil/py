class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print("Se depositaron", cantidad, "en la cuenta", self.numero_cuenta)

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print("Se retiraron", cantidad, "de la cuenta", self.numero_cuenta)
        else:
            print("Fondos insuficientes en la cuenta", self.numero_cuenta)

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print("Se aplicó una cuota de manejo del 2% en la cuenta", self.numero_cuenta)

    def mostrar_detalles(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balance)

numero_cuenta = input("Ingrese el número de cuenta: ")
propietarios = input("Ingrese los nombres de los propietarios (separados por comas): ").split(',')
balance_inicial = float(input("Ingrese el balance inicial: "))

cuenta = CuentaBancaria(numero_cuenta, propietarios, balance_inicial)

while True:
    print("\nOpciones:")
    print("1. Mostrar detalles de la cuenta")
    print("2. Realizar depósito")
    print("3. Realizar retiro")
    print("4. Aplicar cuota de manejo")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        cuenta.mostrar_detalles()
    elif opcion == '2':
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuenta.depositar(cantidad)
    elif opcion == '3':
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar(cantidad)
    elif opcion == '4':
        cuenta.aplicar_cuota_manejo()
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
