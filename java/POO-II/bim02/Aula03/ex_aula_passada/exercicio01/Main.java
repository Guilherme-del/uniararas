import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)) {
			System.out.print("Digite o primeiro numero: ");
			float primeiroNumero = sc.nextFloat();
			System.out.print("Digite o segundo numero: ");
			float segundoNumero = sc.nextFloat();
			
			ComparaNumero  maiorNum = new ComparaNumero (primeiroNumero, segundoNumero);
			maiorNum.comparaNum();
		}
	}
	public static class ComparaNumero {
	    private float Numero1, Numero2;
	    
	    
	    public ComparaNumero (float Numero1, float Numero2) {
	        this.Numero1 = Numero1;
	        this.Numero2 = Numero2;
	    }
	    public void maiorNum() {
	        if (Numero1 > Numero2) {
	        	System.out.println("Maior numero " + Numero1 + "\nO menor numero é " + Numero2);
	        } else {
	        	System.out.println("Maior numero " + Numero2 + "\nO menor numero é " + Numero1);
	        }
	    }
	    
	    public void comparaNum() {
	       if(Numero1 == Numero2) {
	    	   System.out.println("Os números são iguais!!");
	       }
	       else {
	    	   System.out.println("Os números são diferentes!!");
	    	   maiorNum();
	    	   
	       }
	    }
	}
}

