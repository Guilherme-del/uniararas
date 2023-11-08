import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
          int MaiorNum = 1000;
          int MenorNum = 1;
          int randomNum = (int)(Math.random() * MaiorNum) + MenorNum ;
          
          int qtdTentativas = 0;
          System.out.println(randomNum);
          System.out.print("Chuta um numero inteiro: ");
          int chute = sc.nextInt();
          
          while(true){
              
              if(chute == randomNum){
                  System.out.println("Parabens você acertou!!");
                  System.out.print(qtdTentativas);
                  break;
              }
              else if(chute > randomNum){
                  System.out.println("Seu chute é maior que o numero sorteado!!");
              }
              else if(chute < randomNum){
                  System.out.println("Seu chute foi menor que o numero sorteado!!");
              }
              qtdTentativas++;
              System.out.print("Chuta um numero inteiro: ");
              chute = sc.nextInt();
              
              
          }
        }
        
        
        
     
    }
    
}