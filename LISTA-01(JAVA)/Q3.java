/* A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e seu saldo.
  Além de métodos para realizar as operações de depósito e saque.
  Escrever um programa para testar a classe. */


class ContaBancaria {
    public String titular = "";
    public String conta = "";
    public double saldo = 0;

    public void sacar(double v) {
        this.saldo -= v;
    }
    public void depositar(double v) {
        this.saldo += v;
    }
}

public class Q3 {
    public static void main(String[] args) {
        ContaBancaria x = new ContaBancaria();
        x.depositar(100);
        System.out.println(x.saldo);
        x.sacar(50);
        System.out.println(x.saldo);

    }
}
