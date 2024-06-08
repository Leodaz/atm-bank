def main():
    banco = Banco()
    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            titular = input("Ingrese el nombre del titular: ")
            balance = float(input("Ingrese el balance inicial: "))
            numero_cuenta = input("Ingrese el número de cuenta: ")
            banco.agregar_cuenta(titular, balance, numero_cuenta) 
