class Viagem :
    def __init__(self) :
        self.__d = 0
        self.__t = 0
    def set_distancia(self, v) :
        if v >= 0 :
            self.__d = v
        else :
            raise ValueError("Distância Inválida")
    def set_tempo(self, v) :
        if v >= 0 :
            self.__t = v
        else :
            raise ValueError("Tempo Inválido")
    def get_distancia(self) :
        return self.__d
    def get_tempo(self) :
        return self.__t
    def calc_vel_media(self) :
        vel_media = self.__d / self.__t
        return vel_media
    
class UI :
    @staticmethod
    def main() :
         x = Viagem()
         x.set_distancia(100)
         x.set_tempo(1)
         print(x.calc_vel_media())

UI.main()