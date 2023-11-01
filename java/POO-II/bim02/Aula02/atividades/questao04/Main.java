/*
Exercícios de Introdução ao Java

4) Faça um programa que abrevie o nome completo digitado pelo usuário. Existe a restrição
de não abreviar as palavras com 2 ou menos letras. A abreviatura deve vir separada por
pontos. (Exemplo: Marcilio Francisco de Oliveira Neto. Abreviatura: M. F. de O. N.)
Dicas:
- Pesquise o uso do método split(...) de uma string, que devolverá um vetor de strings
separados pelo caracter desejado;
- Pesquise o uso do método chartAt(...) de uma string, que devolverá o caracter dado o
índice.
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o nome completo: ");
        String nomeCompleto = scanner.nextLine();

        String[] palavras = nomeCompleto.split(" "); // Divide o nome em palavras usando o espaço como separador

        StringBuilder abreviatura = new StringBuilder();

        for (int i = 0; i < palavras.length; i++) {
            if (palavras[i].length() > 2) {
                abreviatura.append(palavras[i].charAt(0)).append(". "); // Abrevia a palavra pegando a primeira letra e adiciona um ponto
            } else {
                abreviatura.append(palavras[i]).append(" "); // Mantém palavras curtas sem abreviação
            }
        }

        System.out.println("Abreviatura: " + abreviatura.toString().trim()); // Exibe a abreviatura, removendo espaços extras

        scanner.close();
    }
}