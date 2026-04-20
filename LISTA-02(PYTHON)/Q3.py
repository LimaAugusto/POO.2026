class contaBancaria :
    def __init__(self) :
        self.__titular = ""
        self.__conta = ""
        self.__saldo = 0
    def get_conta(self) :
        return self.__conta
    def get_titular(self) :
        return self.__titular
    def get_saldo(self) :
        return self.__saldo
    def set_conta(self, v) :
        self.__conta = v
        return self.__conta
    def set_titular(self, v) :
        self.__titular = v
        return self.__titular
    def set_saldo(self, v) :
        if v >= 0 :
            self.__saldo = v
        else :
            raise ValueError("Saldo Inválido")
    def depositar(self, v) :
        if v < 0 :
            raise ValueError("Número Inválido")
        else :
            self.__saldo += v
            return self.__saldo
    def sacar(self, v) :
        if v < 0 :
            raise ValueError("Número Inválido")
        elif v > self.__saldo :
            raise ValueError("Saldo insuficiente")
        else :
            self.__saldo -= v
            return self.__saldo
    
class UI :
    @staticmethod
    def main() :
        x = contaBancaria()
        x.set_titular("Augusto Cesar")
        x.set_conta("1234")
        x.set_saldo(10)
        print(f"O titular é: {x.get_titular()}, {x.get_conta()}")
        print(f"Seu saldo é: {x.get_saldo()}")
        print(f"Após depositar: {x.depositar(100)}")
        print(f"Após sacar: {x.sacar(10)}")


UI.main()