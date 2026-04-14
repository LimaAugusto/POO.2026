# A classe deve ter atributos para armazenar a distância em km e o tempo gasto em horas e minutos da viagem realizada. 
# A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de acordo com a distância e o tempo gasto.
# Escrever um programa para testar a classe.

class Viagem() :
    def __init__(self) :
        self.dist  = 0
        self.horas = 0
        self.min   = 0
    def calc_vel_media(self) :
        minutos = self.min / 60
        tempo   = self.horas + minutos
        vel_media = self.dist / tempo
        return vel_media


x = Viagem()
x.dist = 100
x.horas = 1
x.min = 30
print(Viagem(), x.calc_vel_media())