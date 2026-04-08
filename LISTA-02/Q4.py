class Entrada() : 
    def __init__(self) :
        self.__dia  = ''
        self.__hora = 0
    def set_dia(self, v) :
        self.__dia = v
        return self.__dia
    def set_hora(self, v) :
        if v < 0 :
            raise ValueError("Hora Inválida")
        else :
            self.__hora = v
            return self.__hora
    def get_dia(self) :
        return self.__dia
    def get_hora(self) :
        return self.__hora
    def inteira(self)  :
        if self.__dia == 'quarta' :
            return 8.00
        valor_base = 00.00
        if self.__dia == 'segunda' or self.__dia == 'terça' or self.__dia == 'quinta'   :
            valor_base = 16.00
        elif self.__dia == 'sexta' or self.__dia == 'sabado' or self.__dia == 'domingo' :
            valor_base = 20.00
        else :
            return 'data invalida'
        if 17 <= self.__hora <= 23 :
            valor_base = valor_base * 1.5
            return valor_base
        else :
            return valor_base
    def meia(self)     :
        if self.__dia == 'quarta' :
            return 8.00
        else :
            return self.inteira() / 2.0

class UI :
    @staticmethod
    def main() :
        x = Entrada()
        x.set_dia('sexta')
        x.set_hora(18)
        print(f"Seu ingresso é para {x.get_dia()}, às {x.get_hora()} horas.")
        print(f"O valor da inteira é R${x.inteira():.2f} e o valor da meia é R${x.meia():.2f}")

UI.main()