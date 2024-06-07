class Cliente:
def __init__(self, __dni,__nombre,__apellidos) -> None:
    self.set_Documento_identidad(__ID):V-12226750
    self.set_nombre(__nombre):Leonardo 
    self.set_apellidos(__apellidos):Daza Blanco

def set_ID(self, ID):
    self.__ID = ID

def get_ID(self):
    return self.__ID

def set_nombre(self, nombre):
    self.__nombre = nombre

def get_nombre(self):
    return self.__nombre

def set_apellidos(self, apellidos):
    self.__apellidos = apellidos

def get_apellidos(self):
    return self.__apellidos

def __eq__(self, otro: object) -> bool:
    if type(self) != type(otro):
        return NotImplemented
    return self.__ID == otro.__ID

class Movimiento:

def __init__(self, __concepto, __cantidad) -> None:
    self.__concepto = __concepto
    self.__cantidad = __cantidad

def get_concepto(self):
    return self.__concepto

def get_cantidad(self):
    return self.__cantidad

def __hash__(self) -> int:
    return hash((self.__concepto, self.__cantidad)) 


class Cuenta:
  def __init__(self, __numero, __titular, __saldo, __movimientos = None) -> None:
    self.__numero = __numero
    self.set_titular(__titular)
    self.__saldo = __saldo

    if __movimientos is None:
        self.__movimientos = {}
    else:
        self.__movimientos = __movimientos

def set_titular(self, titular):
        self.__titular = titular

def get_titular(self):
        return self.__titular

def get_numero(self):
    return self.__numero

def __hash__(self) -> int:
    return hash(self.__numero)

def get_saldo(self):
    return self.__saldo
'saldo':'currency': 'USD',

class Banco:
  def_init_(self):
  self.saldo=98745321.00
  return self.saldo 
else:
  print (saldo suficiente) 

account_number = response["accounts"][1]["number"]

    transfer_data = {
        'origin_account': account_number,
        'destination_account': '037069523',
        'destination_institution': '5600010',
        'authorization_device_number': '01',
      
        'currency': 'USD',
      
