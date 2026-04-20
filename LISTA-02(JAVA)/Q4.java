class Entrada {
    private String dia = "";
    private int hora = 0;

    public void setDia(String v) {
        this.dia = v;
    }
    public void setHora(int v) {
        if (v >= 0) this.hora = v;
        else throw new IllegalArgumentException("Hora inválida");
    }
    public String getDia() {
        return this.dia;
    }
    public int getHora() {
        return this.hora;
    }

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
        x.setDia("segunda");
        x.setHora(17);
        System.out.println("Sua inteira é " + x.inteira() + " e a meia é " + x.meia());
    }
}