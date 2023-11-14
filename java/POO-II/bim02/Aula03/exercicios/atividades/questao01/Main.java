import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CestaProdutos cestaProdutos = new CestaProdutos("Cliente");

        while (true) {
            System.out.println("1. Consultar Valor Total");
            System.out.println("2. Inserir Produto");
            System.out.println("3. Remover Produto");
            System.out.println("4. Consultar Produto");
            System.out.println("5. Editar Produto");
            System.out.println("6. Sair");

            System.out.print("Escolha uma opção: ");
            int escolha = scanner.nextInt();

            switch (escolha) {
                case 1:
                    System.out.println("Valor Total: " + cestaProdutos.consultarValorTotal());
                    break;
                case 2:
                    // Lógica para adicionar um novo produto
                    System.out.print("Digite o código do produto: ");
                    int codigo = scanner.nextInt();
                    scanner.nextLine();  // Consumir a quebra de linha pendente
                    System.out.print("Digite o nome do produto: ");
                    String nome = scanner.nextLine();
                    System.out.print("Digite o volume do produto: ");
                    double volume = scanner.nextDouble();
                    System.out.print("Digite o peso do produto: ");
                    double peso = scanner.nextDouble();
                    System.out.print("Digite o valor do produto: ");
                    double valor = scanner.nextDouble();

                    Produto novoProduto = new Produto(codigo, nome, volume, peso, valor);
                    cestaProdutos.inserirProduto(novoProduto);
                    System.out.println("Produto inserido com sucesso!");
                    break;
                case 3:
                    System.out.print("Digite o código do produto a ser removido: ");
                    int codigoRemover = scanner.nextInt();
                    cestaProdutos.removerProduto(codigoRemover);
                    System.out.println("Produto removido com sucesso!");
                    break;
                case 4:
                    System.out.print("Digite o código do produto a ser consultado: ");
                    int codigoConsultar = scanner.nextInt();
                    cestaProdutos.consultarProduto(codigoConsultar);
                    break;
                case 5:
                    // Lógica para editar um produto
                    System.out.print("Digite o código do produto a ser editado: ");
                    int codigoEditar = scanner.nextInt();
                    scanner.nextLine();  // Consumir a quebra de linha pendente
                    System.out.print("Digite o novo nome do produto: ");
                    String novoNome = scanner.nextLine();
                    System.out.print("Digite o novo volume do produto: ");
                    double novoVolume = scanner.nextDouble();
                    System.out.print("Digite o novo peso do produto: ");
                    double novoPeso = scanner.nextDouble();
                    System.out.print("Digite o novo valor do produto: ");
                    double novoValor = scanner.nextDouble();

                    Produto produtoEditado = new Produto(codigoEditar, novoNome, novoVolume, novoPeso, novoValor);
                    cestaProdutos.editarProduto(codigoEditar, produtoEditado);
                    System.out.println("Produto editado com sucesso!");
                    break;
                case 6:
                    System.out.println("Saindo do programa.");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
        }
    }
}
