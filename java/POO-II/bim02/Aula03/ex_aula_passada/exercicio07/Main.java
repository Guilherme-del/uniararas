//package parte1;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		try (Scanner scMain = new Scanner(System.in)) {
			ControleRemoto CR = new ControleRemoto();
			while(true) {
				escopo();
				int escolha = scMain.nextInt();
				if(escolha == 1) {
					CR.ligarDesligar();
				}
				else if(escolha == 2) {
					CR.TrocarCanal();
				}
				else if(escolha == 3) {
					CR.TrocarVolume();
				}
				else if(escolha == 4) {
					
					break;
				}
				else {
					System.out.println("Escolha impossivel!!");
				}
				
			}
		}
	}

	public static void escopo() {	
		System.out.println("1 - OnOff");
		System.out.println("2 - Canal");
		System.out.println("3 - Volume");
		System.out.println("4 - Largar controle");
		
	}

public static class ControleRemoto{
		Scanner scClasse = new Scanner(System.in);
		private int canal, volume, OnOff;
		
		public ControleRemoto() {
			this.canal = 6;
			this.volume = volume;
			this.OnOff = 0;
		}
		
		public void ligarDesligar() {
			if(OnOff == 0) {
				OnOff = 1;
				System.out.println("SUA TV ESTÁ LIGADA!!");
			}
			else if(OnOff == 1){
				OnOff = 0;
				System.out.println("DESLIGANDO TV....");
			}
		}
		
		public void TrocarCanal() {
			if(OnOff == 1) {
				System.out.println("CANAL "  + canal);
				System.out.print("Digite o canal (númerico inteiro) que deseja assistir: ");
				int varTempCanal = scClasse.nextInt();
				if(canal != varTempCanal) {
					canal = varTempCanal;
					System.out.println("Canal " + canal );
				}
				else {
					System.out.println("Você já esta no canal " +canal);
				}
			}
			else {
				System.out.println("TV DESLIGADA!!");
			}
			
		}
	
		public void TrocarVolume() {
			if(OnOff == 1) {
				String opcao = "";
				System.out.println("VOLUME "  + volume);
				if(volume == 0){
					System.out.println("+\n- ");
					opcao = scClasse.next();
					if(opcao.equals("+")) {
						volume++;
						System.out.println("VOLUME "  + volume);
					}
					else if(opcao.equals("-")) {
						System.out.println("Volume minimo é 0");
					}
					else {
						System.out.println("Opção invalida");
					}
				}
				else if(volume == 100) {
					System.out.println("+ para aumentar\n- para diminuir ");
					opcao = scClasse.next();
					if(opcao.equals("+")) {
						System.out.println("Volume maximo é 100");
					}
					else if(opcao.equals("+")) {
						volume--;
						System.out.println("VOLUME "  + volume);
					}
					else {
						System.out.println("Opção invalida");
					}
				}
				else if(volume != 0 && volume != 100){
					System.out.println("+\n-");
					opcao = scClasse.next();
					if(opcao.equals("+")) {
						volume++;
						System.out.println("VOLUME "  + volume);
					}
					else if(opcao.equals("-")) {
						volume--;
						System.out.println("VOLUME "  + volume);
					}
					else {
						System.out.println("Opção invalida");
					}
				}
			}
			else {
				System.out.println("TV DESLIGADA!!");
			}
			
		}
		
	}
}