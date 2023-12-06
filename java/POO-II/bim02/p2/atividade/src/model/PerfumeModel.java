public class PerfumeModel extends ProdutoModel {
    private String marca;
    private int tamanhoML;

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getTamanhoML() {
        return tamanhoML;
    }

    public void setTamanhoML(int tamanhoML) {
        this.tamanhoML = tamanhoML;
    }

    @Override
    public String getDetalhes() {
        return "Perfume - Marca: " + marca + ", Tamanho: " + tamanhoML + "ml";
    }
}