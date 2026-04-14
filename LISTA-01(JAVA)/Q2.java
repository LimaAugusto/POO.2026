/* A classe deve ter atributos para armazenar a distância em km e o tempo gasto em horas e minutos da viagem realizada. 
  A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de acordo com a distância e o tempo gasto.
  Escrever um programa para testar a classe. */

class Velocidade {
    public double d = 0;
    public double t = 0;

    public double calc_Vel() {
        return this. d / this.t;
    }
}

public class Q2 {
    public static void main(String[] args) {
        Velocidade x = new Velocidade();
        x.d = 100;
        x.t = 1;
        System.out.println(x.calc_Vel());
    }
}