class Conversor :
    def __init__(self, num) :
        self.SetNum(num)
    def SetNum(self, v) :
        if v >= 0 :
            self.__num = v
        else :
            raise ValueError()
    def GetNum(self) :
        return self.__num
    def Binario(self) :
        return f"{self.__num:b}"
    def __str__(self):
        return f"Decimal: {self.__num}"

class UI :
    @staticmethod
    def main() :
        x = Conversor(13)
        print(x.__str__())
        print(x.Binario())

UI.main()