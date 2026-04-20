class Circulo {
    private double r = 0;
    public void setRaio (double v) {
        if (v >= 0) this.r = v;
        else throw new IllegalArgumentException("Valor negativo é inválido");
    }
    public double getRaio() {
        return this.r;
    }
    public double calcArea() {
        return 3.14 * this.r * this.r;
    }
    public double calcCircun() {
        return 2 * 3.14 * this.r;
    }
}

public class Q1 {
    public static void main(String[] args) {
        Circulo x = new Circulo();
        x.setRaio(-10);
        System.out.println("A área é " + x.calcArea() + " e a circunferência é : " + x.calcCircun());
    }
}
