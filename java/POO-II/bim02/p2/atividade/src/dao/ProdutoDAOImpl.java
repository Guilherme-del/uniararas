import java.util.ArrayList;
import java.util.List;

public class ProdutoDAOImpl implements ProdutoDAO {
    private static ProdutoDAOImpl instancia;
    private List<ProdutoModel> bancoDeDados;

    private ProdutoDAOImpl() {
        bancoDeDados = new ArrayList<>();
    }

    public static ProdutoDAOImpl getInstancia() {
        if (instancia == null) {
            instancia = new ProdutoDAOImpl();
        }
        return instancia;
    }

    @Override
    public void cadastrarProduto(ProdutoModel produto) {
        bancoDeDados.add(produto);
        System.out.println("Produto cadastrado no banco de dados.");
    }

    @Override
    public ProdutoModel consultarProduto(int codigo) {
        for (ProdutoModel produto : bancoDeDados) {
            if (produto.getCodigo() == codigo) {
                System.out.println("Produto consultado no banco de dados.");
                return produto;
            }
        }
        System.out.println("Produto não encontrado no banco de dados.");
        return null;
    }

    @Override
    public void atualizarEstoque(int codigo, int quantidade) {
        for (ProdutoModel produto : bancoDeDados) {
            if (produto.getCodigo() == codigo) {
                produto.setQuantidadeEstoque(quantidade);
                System.out.println("Estoque do produto atualizado no banco de dados.");
                return;
            }
        }
        System.out.println("Produto não encontrado para atualização de estoque.");
    }
}
