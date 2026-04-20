class Frete :
    def __init__(self, d, p) :
        self.SetDistancia(d)
        self.SetPeso(p)
    def SetDistancia(self, v) :
        if v >= 0 :
            self.__d = v
        else :
            raise ValueError()
    def SetPeso(self, v) :
        if v >= 0 :
            self.__p = v
        else :
            raise ValueError()
    def GetDistancia(self) :
        return self.__d
    def GetPeso(self) :
        return self.__p
    def CalcFrete(self) :
        return self.__d * self.__p * 0.01
    def __str__(self) :
        return f"Meus dados são: Distância = {self.__d} e Peso = {self.__p}"


class UI :
    @staticmethod
    def main() :
        x = Frete(10, 10)
        print(x.__str__())
        print(x.CalcFrete())

UI.main()