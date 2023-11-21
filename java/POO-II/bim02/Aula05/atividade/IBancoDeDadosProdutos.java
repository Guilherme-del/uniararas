import java.util.List;
import java.util.ArrayList;

public interface IBancoDeDadosProdutos {
    void inserir(Produto produto);
    void remover(int codigo);
    Produto consultar(int codigo);
    List<Produto> listar();
    float consultarValorTotal();
}

