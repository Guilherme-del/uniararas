import java.util.List;

public class VendaController {
    private ProdutoDAO produtoDAO;

    public VendaController() {
        this.produtoDAO = ProdutoDAOImpl.getInstancia();
    }

    public void realizarCompra(List<Integer> codigos) {
        double valorTotal = 0;

        System.out.println("===== Carrinho de Compras =====");
        for (int codigo : codigos) {
            ProdutoModel produto = produtoDAO.consultarProduto(codigo);

            if (produto != null && produto.getQuantidadeEstoque() > 0) {
                valorTotal += produto.getPreco();
                produto.vender(); // Método fictício para atualizar o estoque

                // Atualiza o estoque no banco de dados
                produtoDAO.atualizarEstoque(codigo, produto.getQuantidadeEstoque());

                System.out.println("Produto adicionado ao carrinho: " + produto.getDetalhes());
            } else {
                System.out.println("Produto não disponível para compra: Código " + codigo);
            }
        }

        System.out.println("===============================");
        System.out.println("Valor Total da Compra: " + valorTotal);
        System.out.println("Compra realizada com sucesso!");
    }

    public void cadastrarProduto(ProdutoModel produto) {
        produtoDAO.cadastrarProduto(produto);
    }

    public ProdutoModel consultarProduto(int codigo) {
        return produtoDAO.consultarProduto(codigo);
    }
}
