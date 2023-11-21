public class Main {
    public static void main(String[] args) {
        int opcao;
        do {
            System.out.println("Menu de opções:");
            System.out.println("1. Consultar valor total");
            System.out.println("2. Inserir produto");
            System.out.println("3. Remover produto");
            System.out.println("4. Consultar produto");
            System.out.println("5. Editar produto");
            System.out.println("0. Sair");
            System.out.println("Digite sua opção: ");
            opcao = Integer.parseInt(System.console().readLine());

            switch (opcao) {
                case 1:
                    Controlador.consultarValorTotal();
                    break;
                case 2:
                    Controlador.inserirProduto();
                    break;
                case 3:
                    Controlador.removerProduto();
                    break;
                case 4:
                    Controlador.consultarProduto();
                    break;
                case 5:
                    Controlador.editarProduto();
                    break;
                case 0:
                    System.out.println("Obrigado por usar nosso sistema!");
                    break;
                default:
                    System.out.println("Opção inválida!");
                    break;
            }
        } while (opcao != 0);
    }
}
