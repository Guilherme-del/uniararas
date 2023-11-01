/*
Exercícios de Introdução ao Java

1) Faça um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostre
a expressa em dias. Leve em consideração o ano com 365 dias e o mês com 30. (Exemplo
de saída: 3 anos, 2 meses e 15 dias = 1170 dias)
*/


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número de anos: ");
        int anos = scanner.nextInt();

        System.out.print("Digite o número de meses: ");
        int meses = scanner.nextInt();

        System.out.print("Digite o número de dias: ");
        int dias = scanner.nextInt();

        // Considerando que um ano tem 365 dias e um mês tem 30 dias
        int idadeEmDias = (anos * 365) + (meses * 30) + dias;

        System.out.println("A idade em dias é: " + idadeEmDias + " dias");

        scanner.close();
    }
}
