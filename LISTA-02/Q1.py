class Circulo :
    def __init__(self) :
        self.__r = 0.0
    def set_raio(self, v) :
        if v >= 0 :
            self.__r = v
        else :
            raise ValueError("Valor negativo é inválido")
    def get_raio(self) :
        return self.__r
    def calc_area(self) :
        area = 3.14 * self.__r * self.__r
        return area
    def calc_circun(self) :
        circunferencia = 2 * 3.14 * self.__r
        return circunferencia
    
class UI :
    @staticmethod
    def main() :
        x = Circulo()
        x.set_raio(-10)
        print(x.calc_area(), x.calc_circun())

UI.main()