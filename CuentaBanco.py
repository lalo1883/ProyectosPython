
import random


class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta, saldo):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def verSaldo(self):
        return print(f'Tu saldo es: {self.saldo}')
    
    def retirarSaldo(self, montoRetirado):
        if montoRetirado < self.saldo:
            self.saldo -= montoRetirado
            return print(f'Haz retirado: {montoRetirado}')
        else:
            print("No tienes suficiente dinero!! ")


    def AgregarSaldo(self, montoAgregado):
        self.saldo += montoAgregado
        return print(f'Haz agregado: {montoAgregado}')
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Numero de cuenta:{self.num_cuenta}, Saldo: {self.saldo}'


# Pides los atributos del cliente 
def crearCliente():
    name = input("Ingresa tu nombre: ")
    ap = input("Ingresa tu apellido: ")
    numeroCuenta = random.randint(5002220,9000000)
    saldo = 0 
    # Creas una variable en la que se guarde el objeto
    cuenta = Cliente(name, ap, numeroCuenta, saldo)
    # Devuelves el objeto
    return cuenta




def start():
    print("Bienvenido al sistema de cuentas")
    print("Creemos tu cuenta")
    # Creas un objeto
    cliente = crearCliente()
    flow = 0
    print(cliente)
    while flow != 3:
        print("Opciones:")
        print("1) Agregar saldo")
        print("2) Retirar saldo")
        print("3) Salir")
        opcion = int(input("Ingresa una opción: "))
        
        if opcion == 1:
            saldoAgregar = float(input("Ingresa el saldo a agregar: "))
            cliente.AgregarSaldo(saldoAgregar)
            cliente.verSaldo()
        elif opcion == 2:
            saldoRetirar = float(input("Ingresa el saldo a retirar: "))
            cliente.retirarSaldo(saldoRetirar)
            cliente.verSaldo()
        elif opcion == 3:
            flow = 3
        else:
            print("Opción inválida. Por favor, selecciona una opción válida del menú.")
    
    print("Nos vemos luego!")
start()
