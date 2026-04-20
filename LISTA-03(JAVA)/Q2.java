class Frete {
    private double d = 0;
    private double p = 0;
    public Frete(double d, double p) {
        this.setDistancia(d);
        this.setPeso(p);
    }
    public void setDistancia(double v) {
        if (v >= 0) this.d = v;
        else throw new IllegalArgumentException("Valor inválido");
    }
    public void setPeso(double v) {
        if (v >= 0) this.p = v;
        else throw new IllegalArgumentException("Valor inválido");
    }
    public double getDistancia() {
        return this.d;
    }
    public double getPeso() {
        return this.p;
    }
    public double calcFrete() {
        return this.d * this.p * 0.01;
    }
    public String toString() {
        return "O valor da distância e peso são, respectivamente, " + this.getDistancia() + " " + this.getPeso();
    }
}

public class Q2 {
    public static void main(String[] args) {
        Frete x = new Frete(30, 15);
        System.out.println(x);
        System.out.println("O valor od frete é: " + x.calcFrete());
    }
    
}
