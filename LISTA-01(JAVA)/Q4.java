/* A classe deve ter atributos para armazenar o dia e o horário de uma sessão de cinema e métodos para calcular o
valor da entrada inteira e da meia-entrada.
O valor das entradas deve ser calculado com base nas seguintes regras:
• Segunda, terça e quinta, o valor base do ingresso é R$ 16,00.
• Nas quartas todos pagam meia-entrada no valor de R$ 8,00, em qualquer horário.
• Sexta, sábado e domingo, o valor base do ingresso é R$ 20,00.
• Das 17h à meia-noite, há acréscimo de 50% no valor base do ingresso.
Escrever um programa para testar a classe. */

class Entrada {
    public String dia = "";
    public int hora = 0;

    public double inteira() {
        if (this.dia == "quarta") {
            return 8.00;
        }
        double valor_base = 0;
        if (this.dia.equals("segunda") || this.dia.equals("terça") || this.dia.equals("quinta")) {
            valor_base = 16.00;
        }
        else if (this.dia.equals("sexta") || this.dia.equals("sabado") || this.dia.equals("domingo")) { 
            valor_base = 20.00;
        }
        else {
            return -1;
        }
        if (17 <= this.hora && this.hora <= 23) {
            valor_base = valor_base * 1.5;
            return valor_base;
        }
        else {
            return valor_base;
        }
    }
    
    public double meia() {
        if (this.dia.equals("quarta")) {
            return 8.00;
        }
        else {
            return this.inteira() / 2.0;
        }
    }
}

public class Q4 {
    public static void main(String[] args) {
        Entrada x = new Entrada();
        x.dia ="segunda";
        x.hora = 17;
        System.out.println(x.inteira());
        System.out.println(x.meia());
    }
}