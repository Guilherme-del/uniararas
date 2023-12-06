import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static VendaController vendaController = new VendaController();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            exibirMenu();

            int opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {
                case 1:
                    cadastrarProduto();
                    break;
                case 2:
                    consultarProduto();
                    break;
                case 3:
                    realizarCompra();
                    break;
                case 4:
                    System.out.println("Saindo do sistema. Até logo!");
                    System.exit(0);
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
        }
    }

    private static void exibirMenu() {
        System.out.println("===== Menu =====");
        System.out.println("1. Cadastrar Produto");
        System.out.println("2. Consultar Produto");
        System.out.println("3. Realizar Compra");
        System.out.println("4. Sair");
        System.out.println("=================");
        System.out.print("Escolha uma opção: ");
    }

    private static void cadastrarProduto() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o código do produto: ");
        int codigo = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Digite a descrição do produto: ");
        String descricao = scanner.nextLine();

        System.out.print("Digite o preço do produto: ");
        double preco = scanner.nextDouble();

        System.out.print("Digite a quantidade em estoque do produto: ");
        int quantidade = scanner.nextInt();

        System.out.print("Escolha o tipo de produto (1 para Relógio, 2 para Perfume): ");
        int tipoProduto = scanner.nextInt();
        scanner.nextLine();

        ProdutoModel novoProduto;
        if (tipoProduto == 1) {
            System.out.print("Digite a marca do relógio: ");
            String marcaRelogio = scanner.nextLine();

            System.out.print("Digite o tipo do relógio (mecânico, quartz ou digital): ");
            String tipoRelogio = scanner.nextLine();

            novoProduto = new RelogioModel();
            ((RelogioModel) novoProduto).setMarca(marcaRelogio);
            ((RelogioModel) novoProduto).setTipo(tipoRelogio);
        } else if (tipoProduto == 2) {
            System.out.print("Digite a marca do perfume: ");
            String marcaPerfume = scanner.nextLine();

            System.out.print("Digite o tamanho do perfume em mililitros: ");
            int tamanhoPerfume = scanner.nextInt();

            novoProduto = new PerfumeModel();
            ((PerfumeModel) novoProduto).setMarca(marcaPerfume);
            ((PerfumeModel) novoProduto).setTamanhoML(tamanhoPerfume);
        } else {
            System.out.println("Opção inválida. Cadastro cancelado.");
            return;
        }

        novoProduto.setCodigo(codigo);
        novoProduto.setDescricao(descricao);
        novoProduto.setPreco(preco);
        novoProduto.setQuantidadeEstoque(quantidade);

        vendaController.cadastrarProduto(novoProduto);
        System.out.println("Produto cadastrado com sucesso!");
    }

    private static void consultarProduto() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o código do produto a ser consultado: ");
        int codigo = scanner.nextInt();

        ProdutoModel produto = vendaController.consultarProduto(codigo);

        if (produto != null) {
            System.out.println("Detalhes do Produto:");
            System.out.println(produto.getDetalhes());
        } else {
            System.out.println("Produto não encontrado.");
        }
    }

    private static void realizarCompra() {
        Scanner scanner = new Scanner(System.in);

        List<Integer> produtosComprados = new ArrayList<>();

        while (true) {
            System.out.print("Digite o código do produto a ser comprado (ou 0 para finalizar): ");
            int codigo = scanner.nextInt();

            if (codigo == 0) {
                break;
            }

            produtosComprados.add(codigo);
        }

        vendaController.realizarCompra(produtosComprados);
    }
}
