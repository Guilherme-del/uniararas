public interface ProdutoDAO {
    void cadastrarProduto(ProdutoModel produto);
    ProdutoModel consultarProduto(int codigo);
    void atualizarEstoque(int codigo, int quantidade);
}