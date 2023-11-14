import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Obtenha a capacidade e o total de andares do usuário
        System.out.print("Informe a capacidade do elevador: ");
        int capacidade = scanner.nextInt();

        System.out.print("Informe o total de andares no prédio (excluindo o térreo): ");
        int totalAndares = scanner.nextInt();

        // Crie uma instância da classe Elevador
        Elevador elevador = new Elevador(capacidade, totalAndares);

        int escolha;

        do {
            System.out.println("\nMenu:");
            System.out.println("1 - Entrar no elevador");
            System.out.println("2 - Sair do elevador");
            System.out.println("3 - Subir um andar");
            System.out.println("4 - Descer um andar");
            System.out.println("5 - Obter informações do elevador");
            System.out.println("0 - Sair");

            System.out.print("Escolha uma opção: ");
            escolha = scanner.nextInt();

            switch (escolha) {
                case 1:
                    elevador.entra();
                    break;
                case 2:
                    elevador.sai();
                    break;
                case 3:
                    elevador.sobe();
                    break;
                case 4:
                    elevador.desce();
                    break;
                case 5:
                    exibirInformacoes(elevador);
                    break;
                case 0:
                    System.out.println("Encerrando o programa.");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
        } while (escolha != 0);

        scanner.close();
    }

    public static void exibirInformacoes(Elevador elevador) {
        System.out.println("Andar Atual: " + elevador.getAndarAtual());
        System.out.println("Total de Andares: " + elevador.getTotalAndares());
        System.out.println("Capacidade: " + elevador.getCapacidade());
        System.out.println("Pessoas Presentes: " + elevador.getPessoasPresentes());
    }
}
