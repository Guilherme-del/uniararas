public class Produto {
    private int codigo;
    private String nome;
    private double volume;
    private double peso;
    private double valor;

    // Construtor
    public Produto(int codigo, String nome, double volume, double peso, double valor) {
        this.codigo = codigo;
        this.nome = nome;
        this.volume = volume;
        this.peso = peso;
        this.valor = valor;
    }

    // Getters e Setters
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getVolume() {
        return volume;
    }

    public void setVolume(double volume) {
        this.volume = volume;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }
}