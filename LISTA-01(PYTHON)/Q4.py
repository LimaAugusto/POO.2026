# A classe deve ter atributos para armazenar o dia e horário de uma sessão de cinema, métodos para calcular o valor da entrada inteira e da meia-entrada.
# O valor das entradas deve ser calculado com base nas seguintes regras:
#   • Segunda, terça e quinta, o valor base do ingresso é R$ 16,00.
#   • Nas quartas todos pagam meia-entrada no valor de R$ 8,00, em qualquer horário.
#   • Sexta, sábado e domingo, o valor base do ingresso é R$ 20,00.
#   • Das 17h à meia-noite, há acréscimo de 50% no valor base do ingresso.
# Escrever um programa para testar a classe.

class Entrada() : 
    def __init__(self) :
        self.dia  = ''
        self.hora = 0
    def inteira(self)  :
        if self.dia == 'quarta' :
            return 8.00
        valor_base = 00.00
        if self.dia == 'segunda' or self.dia == 'terça' or self.dia == 'quinta'   :
            valor_base = 16.00
        elif self.dia == 'sexta' or self.dia == 'sabado' or self.dia == 'domingo' :
            valor_base = 20.00
        else :
            return 'data invalida'
        if 17 <= self.hora <= 23 :
            valor_base = valor_base * 1.5
            return valor_base
        else :
            return valor_base
    def meia(self)     :
        if self.dia == 'quarta' :
            return 8.00
        else :
            return self.inteira() / 2.0


x = Entrada()
x.dia = 'sexta'
x.hora = 18
print(x.inteira(), x.meia())