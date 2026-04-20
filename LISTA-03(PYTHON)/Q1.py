class Retangulo :
    def __init__(self, b, h) :
        self.SetBase(b)
        self.SetAltura(h)
    def SetBase(self, v) :
        if v >= 0 :
            self.__b = v
        else :
            raise ValueError()
    def SetAltura(self, v) :
        if v >= 0 :
            self.__h = v
        else :
            raise ValueError()
    def GetBase(self) :
        return self.__b
    def GetAltura(self) :
        return self.__h
    def CalcArea(self) :
        return self.__b * self.__h
    def CalcDiagonal(self) :
        return self.__b**2 + self.__h**2
    def __str__(self) :
        return f"Base = {self.__b} - Altura = {self.__h}"
    
class UI :
    @staticmethod
    def main():
        x = Retangulo(10, 10)
        print(f"Dados do meu retângulo: {x.__str__()}")
        print(f"A área é: {x.CalcArea()}. A diagonal é: {x.CalcDiagonal()}")

UI.main()