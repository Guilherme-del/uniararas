
import java.util.List;
import java.util.ArrayList;

public class BancoDeDadosProdutos implements IBancoDeDadosProdutos {

    private static BancoDeDadosProdutos instance;
    private List<Produto> produtos;

    private BancoDeDadosProdutos() {
        this.produtos = new ArrayList<>();
    }

    public static BancoDeDadosProdutos getInstance() {
        if (instance == null) {
            instance = new BancoDeDadosProdutos();
        }
        return instance;
    }

    @Override
    public void inserir(Produto produto) {
        this.produtos.add(produto);
    }

    @Override
    public void remover(int codigo) {
        for (Produto produto : this.produtos) {
            if (produto.getCodigo() == codigo) {
                this.produtos.remove(produto);
                break;
            }
        }
    }

    @Override
    public Produto consultar(int codigo) {
        for (Produto produto : this.produtos) {
            if (produto.getCodigo() == codigo) {
                return produto;
            }
        }
        return null;
    }

    @Override
    public List<Produto> listar() {
        return this.produtos;
    }

    @Override
    public float consultarValorTotal() {
        float valorTotal = 0;
        for (Produto produto : this.produtos) {
            valorTotal += produto.getValor();
        }
        return valorTotal;
    }
}