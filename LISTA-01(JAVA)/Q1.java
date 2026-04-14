/* A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área e sua
circunferência.
Escrever um programa para testar a classe.*/

class Circulo {
    public double raio = 0;

    public double area() {
        return 3.14 * this.raio * this.raio;
    }
    public double circunferência() {
        return 2 * 3.14 * this.raio;
    }
}

class Q1 {
    public static void main(String[] args) {
        Circulo x = new Circulo();
        x.raio = 10;
        System.out.println(x.area());
        System.out.println(x.circunferência());
    }
}