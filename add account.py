class Banco:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, titular, balance, numero_cuenta):
        nueva_cuenta = CuentaBancaria(titular, balance, numero_cuenta)
        self.cuentas.append(nueva_cuenta)

    def buscar_cuenta(self, titular, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.titular == titular and cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None
