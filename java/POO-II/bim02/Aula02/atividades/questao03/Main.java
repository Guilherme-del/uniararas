/*
Exercícios de Introdução ao Java

3) Faça um programa que simule um sorteio de um número entre 1 a 1000. (Dica: Pesquise a
utilização da biblioteca Math.Random()).
a. Após isso, pedir o palpite do número sorteado ao usuário. Caso o palpite esteja
errado, informe se ele é maior ou menor que o número sorteado.
b. Fazer com que o programa peça palpites até que o usuário acerte. No final, mostre
a quantidade de tentativas que ele realizou.
*/

import java.util.Scanner;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numeroSorteado = (int) (Math.random() * 1000) + 1;
        int tentativas = 0;

        System.out.println("Bem-vindo ao jogo de adivinhação!");

        while (true) {
            System.out.print("Adivinhe o número (entre 1 e 1000): ");
            int palpite = scanner.nextInt();
            tentativas++;

            if (palpite == numeroSorteado) {
                System.out.println("Parabéns! Você acertou o número sorteado, que era " + numeroSorteado);
                System.out.println("Número de tentativas: " + tentativas);
                break;
            } else if (palpite < numeroSorteado) {
                System.out.println("Tente novamente. O número sorteado é maior.");
            } else {
                System.out.println("Tente novamente. O número sorteado é menor.");
            }
        }

        scanner.close();
    }
}
