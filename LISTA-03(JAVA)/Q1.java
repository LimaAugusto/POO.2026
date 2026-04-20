class Retangulo {
    private double b = 0;
    private double h = 0;
    public Retangulo(double b, double h) {
        this.setBase(b);
        this.setAltura(h);
    }

    public void setBase(double v) {
        if (v >= 0) this.b = v;
        else throw new IllegalArgumentException("valor inválido");
    }
    public void setAltura(double v) {
        if (v >= 0) this.h = v;
        else throw new IllegalArgumentException("valor inválido");
    }
    public double getBase() {
        return this.b;
    }
    public double getAltura() {
        return this.h;
    }
    
    public double calcArea() {
        return this.b * this.h;
    }
    public double calcDiagonal() {
        return (this.b * this.b) + (this.h * this.h);
    }
    public String toString() {
        return "Base =" + this.b + "- Altura = " +  this.h;
    }
}


public class Q1 {
    public static void main(String[] args) {
        Retangulo x = new Retangulo(10, 20);
        System.out.println(x);
        System.out.println(x.calcArea());
    }
    
}
