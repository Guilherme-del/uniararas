import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)) {
      System.out.print("Digite o primeiro numero: ");
      int primeiroNumero = sc.nextInt();
      System.out.print("Digite o segundo numero: ");
      int segundoNumero = sc.nextInt();
      
      MaiorNumero maiorNum = new MaiorNumero(primeiroNumero, segundoNumero);
      int calculo = maiorNum.calculaMaiorNumero();
          System.out.println("O maior número é: " + calculo);
    }
	}
	public static class MaiorNumero {
	    private int Numero1, Numero2;
	    
	    //Construtor
	    public MaiorNumero(int Numero1, int Numero2) {
	        this.Numero1 = Numero1;
	        this.Numero2 = Numero2;
	    }
	    
	    public int calculaMaiorNumero() {
	        if (Numero1 > Numero2) {
	        	return Numero1;
	        } else {
	        	return Numero2;
	        }
	    }
	}
}