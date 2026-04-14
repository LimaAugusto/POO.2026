package POO2026.java.lista001;

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