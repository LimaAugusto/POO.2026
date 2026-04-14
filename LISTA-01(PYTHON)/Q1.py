# A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área e sua circunferência. 
# Escrever um programa para testar a classe.

class Circulo() :
    def __init__(self) :
        self.raio = 0
    def calc_area(self) :
        area = 3.14 * self.raio * self.raio
        return area
    def calc_circun(self) :
        circunferencia = 2 * 3.14 * self.raio
        return circunferencia

x = Circulo()
x.raio = 10
print(Circulo(), x.calc_area(), x.calc_circun())