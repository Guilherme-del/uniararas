/*
Exercícios de Introdução ao Java

2) Faça um programa que imprima a média aritmética de 3 números digitados pelo usuário,
após isso, imprima a divisão da soma desses números pela média.
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        double numero1 = scanner.nextDouble();
        System.out.print("Digite o segundo número: ");
        double numero2 = scanner.nextDouble();
        System.out.print("Digite o terceiro número: ");
        double numero3 = scanner.nextDouble();
        double media = (numero1 + numero2 + numero3) / 3;
        double divisao = (numero1 + numero2 + numero3) / media;
        System.out.println("A média aritmética dos números é: " + media);
        System.out.println("A divisão da soma dos números pela média é: " + divisao);

        scanner.close();
    }
}
