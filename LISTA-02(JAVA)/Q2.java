class Viagem {
    private double d = 0;
    private double t = 0;

    public void setDistancia(double v) {
        if (v >= 0) this.d = v;
        else throw new IllegalArgumentException("Valor negativo é inválido");
    }
        public void setTempo(double v) {
        if (v >= 0) this.t = v;
        else throw new IllegalArgumentException("Valor negativo é inválido");
    }
    public double getDistancia() {
        return this.d;
    }
    public double getTempo() {
        return this.t;
    }

    public double calcVel() {
        return this.d / this.t;
    }
}

public class Q2 {
    public static void main(String[] args) {
        Viagem x = new Viagem();
        x.setDistancia(20);
        x.setTempo(10);
        System.out.println("A velocidade média é: " + x.calcVel());
    }
}
