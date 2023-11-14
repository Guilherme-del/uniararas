import java.util.ArrayList;

public class CestaProdutos {
    private String nomeCliente;
    private ArrayList<Produto> produtos;
    private double valorTotal;

    // Construtor
    public CestaProdutos(String nomeCliente) {
        this.nomeCliente = nomeCliente;
        this.produtos = new ArrayList<>();
        this.valorTotal = 0.0;
    }

    // Métodos
    public double consultarValorTotal() {
        return valorTotal;
    }

    public void inserirProduto(Produto produto) {
        produtos.add(produto);
        valorTotal += produto.getValor();
    }

    public void removerProduto(int codigo) {
        for (Produto produto : produtos) {
            if (produto.getCodigo() == codigo) {
                valorTotal -= produto.getValor();
                produtos.remove(produto);
                break;
            }
        }
    }

    public void consultarProduto(int codigo) {
        for (Produto produto : produtos) {
            if (produto.getCodigo() == codigo) {
                System.out.println("Código: " + produto.getCodigo());
                System.out.println("Nome: " + produto.getNome());
                System.out.println("Volume: " + produto.getVolume());
                System.out.println("Peso: " + produto.getPeso());
                System.out.println("Valor: " + produto.getValor());
                break;
            }
        }
    }

    public void editarProduto(int codigo, Produto novoProduto) {
        for (Produto produto : produtos) {
            if (produto.getCodigo() == codigo) {
                valorTotal -= produto.getValor();
                produto.setCodigo(novoProduto.getCodigo());
                produto.setNome(novoProduto.getNome());
                produto.setVolume(novoProduto.getVolume());
                produto.setPeso(novoProduto.getPeso());
                produto.setValor(novoProduto.getValor());
                valorTotal += novoProduto.getValor();
                break;
            }
        }
    }
}
