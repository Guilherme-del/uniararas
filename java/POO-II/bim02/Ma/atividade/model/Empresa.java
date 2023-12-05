package model;

public abstract class Empresa {
    private String nome;
    private String descricao;
    private int totalFuncionarios;


    public Empresa(){}

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDescricao() {
        return descricao;
    }
    public void setTotalFuncionarios(int totalFuncionarios) {
        this.totalFuncionarios = totalFuncionarios;
    }
    public void contratarFuncionario() {
        totalFuncionarios++;
    }
    public void demitirFuncionario() {
        totalFuncionarios--;
    }
    public int getTotalFuncionarios() {
        return totalFuncionarios;
    }
    public String getNome() {
        return nome;
    }
    public abstract void imprime();
}
