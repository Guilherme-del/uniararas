public class RelogioModel extends ProdutoModel {
    private String marca;
    private String tipo;

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    @Override
    public String getDetalhes() {
        return "Relógio - Marca: " + marca + ", Tipo: " + tipo;
    }
}