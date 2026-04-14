# A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e seu saldo.
# Além de métodos para realizar as operações de depósito e saque.
# Escrever um programa para testar a classe.

class contaBancaria()  :
    def __init__(self) :
        self.titular = ""
        self.numero  = ""
        self.saldo   = 0
    def depositar(self, v) :
        self.saldo += v
        return self.saldo
    def sacar(self, v) :
        self.saldo -= v
        return self.saldo

x = contaBancaria()
x.titular = "Ronaldo"
print(x.titular)
x.numero = "223"
print(x.numero)
x.saldo = 10
print(f'Meu saldo é: {x.saldo}')
print(f'Com o depósito, agora é: {x.depositar(100)}')
print(f'Com o saque, agora é: {x.sacar(50)}')