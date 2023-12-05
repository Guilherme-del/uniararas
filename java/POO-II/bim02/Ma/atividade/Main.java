
import java.util.Scanner;
import controller.EmpresaController;

public class Main {
    static void menu(){
        System.out.println("1. Adicionar empresa");
        System.out.println("2. Editar empresa");
        System.out.println("3. Excluir empresa");
        System.out.println("4. Exibir empresa");
        System.out.println("5. Sair");
    }
    public static void main(String[] args) {
        int op=0;
        String nomeEmpresa, descricaoEmpresa;
        int totalFuncionarios;
        Scanner input = new Scanner(System.in);
        boolean exit = false;
        while(exit == false){
            menu();
            op=input.nextInt();
            input.nextLine();


            switch(op){
                case 1:
                    System.out.println("Nome da empresa: ");
                    nomeEmpresa = input.nextLine();

                    System.out.println("Descrição da empresa: ");
                    descricaoEmpresa = input.nextLine();

                    System.out.println("Total de funcionários: ");
                    totalFuncionarios = input.nextInt();

                    System.out.println("1. Empresa de infraestrutura");
                    System.out.println("2. Empresa de inovação");
                    op = input.nextInt();
                    input.nextLine();
                    if(op == 1){
                        EmpresaController.adicionarEmpresa(nomeEmpresa, descricaoEmpresa, totalFuncionarios, 1);
                    }else if(op == 2){
                        EmpresaController.adicionarEmpresa(nomeEmpresa, descricaoEmpresa, totalFuncionarios, 2);
                    }

                    break;
                case 2:
                    System.out.println("Nome da empresa: ");
                    nomeEmpresa = input.nextLine();

                    System.out.println("Descrição da empresa: ");
                    descricaoEmpresa = input.nextLine();

                    System.out.println("Total de funcionários: ");
                    totalFuncionarios = input.nextInt();

                    EmpresaController.updateEmpresa(nomeEmpresa, descricaoEmpresa, totalFuncionarios);

                    break;
                case 3:
                    System.out.println("Nome da empresa: ");
                    nomeEmpresa = input.nextLine();

                    EmpresaController.deleteEmpresa(nomeEmpresa);

                    break;
                case 4:
                    System.out.println("Nome da empresa: ");
                    nomeEmpresa = input.nextLine();
                    EmpresaController.vizualizarEmpresa(nomeEmpresa);
                    break;
                case 5:
                    exit = true;
                    break;
                default:
                    System.out.println("Opção inválida");
                    break;
            }

        }
    }
}