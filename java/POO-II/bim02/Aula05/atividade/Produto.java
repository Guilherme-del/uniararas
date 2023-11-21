public class Produto {
    private int codigo;
    private String nome;
    private float volume;
    private float peso;
    private float valor;

    public Produto(int codigo, String nome, float volume, float peso, float valor) {
        this.codigo = codigo;
        this.nome = nome;
        this.volume = volume;
        this.peso = peso;
        this.valor = valor;
    }

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

    public float getVolume() {
        return volume;
    }

    public void setVolume(float volume) {
        this.volume = volume;
    }

    public float getPeso() {
        return peso;
    }

    public void setPeso(float peso) {
        this.peso = peso;
    }

    public float getValor() {
        return valor;
    }

    public void setValor(float valor) {
        this.valor = valor;
    }

    @Override
    public String toString() {
        return "Produto{" +
                "codigo=" + codigo +
                ", nome='" + nome + '\'' +
                ", volume=" + volume +
                ", peso=" + peso +
                ", valor=" + valor +
                '}';
    }
}