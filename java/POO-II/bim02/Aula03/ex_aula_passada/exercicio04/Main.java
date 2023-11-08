
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Digite seu nome completo: ");
		String Nome = sc.nextLine();
		String arrayNome[] = new String[100];
		arrayNome = Nome.split(" ");
		
		for(int i = 0; i <arrayNome.length; i++) {
			if(arrayNome[i].length() > 2) {
				System.out.print(arrayNome[i].charAt(0) + "." + " ");
			}
			else if(arrayNome[i].length() <= 2) {
				System.out.print(arrayNome[i] + " ");
			}
		}	
		
	}
}
