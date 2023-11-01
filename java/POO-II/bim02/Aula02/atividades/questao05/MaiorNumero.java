/*
Exercícios de Introdução ao Java

5) Crie uma classe java denominada MaiorNumero que contenha um método que receba dois
números inteiros e imprima o maior entre eles.
*/

public class MaiorNumero {
    public static void main(String[] args) {
        int numero1 = 10;
        int numero2 = 20;
        imprimirMaiorNumero(numero1, numero2);
    }

    public static void imprimirMaiorNumero(int numero1, int numero2) {
        if (numero1 > numero2) {
            System.out.println("O maior número é: " + numero1);
        } else if (numero2 > numero1) {
            System.out.println("O maior número é: " + numero2);
        } else {
            System.out.println("Os números são iguais: " + numero1);
        }
    }
}
