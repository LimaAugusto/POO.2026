class contaBancaria {
    private String titular = "";
    private String conta = "";
    private double saldo = 0;

    public void setSaldo(double v) {
        if (v >= 0) this.saldo = v;
        else throw new IllegalArgumentException("Saldo inválido");
    }
     public void setTitular(String v) {
        this.titular = v;
    }
      public void setConta(String v) {
        this.conta = v;
    }
    
    public double getSaldo() {
        return this.saldo;
    }
    public String getTitular() {
        return this.titular;
    }
    public String getConta () {
        return this.conta;
    }

    public void depositar(double v) {
        if (v >= 0) this.saldo += v;
        else throw new IllegalArgumentException("Valor inválido");
    }
    public void sacar(double v) {
        if (v >= 0) this.saldo -= v;
        else throw new IllegalArgumentException("Valor Inválido");
    } 
}

public class Q3 {
    public static void main(String[] args) {
        contaBancaria x = new contaBancaria();
        x.setConta("12332347");
        x.setTitular("Augusto");
        x.setSaldo(100);
        x.sacar(50);
        x.depositar(150);
        System.out.println("Dono da conta: " + x.getTitular() + ", " + x.getConta() + "Seu saldo é: " + x.getSaldo());
    }
}
