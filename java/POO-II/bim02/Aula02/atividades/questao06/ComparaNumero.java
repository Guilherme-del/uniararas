/*
Exercícios de Introdução ao Java

6) Crie uma classe java ComparaNumero que contenha um método que receba dois números
e indique se são iguais ou se são diferentes. Mostre o maior e o menor (nesta sequência).
*/

public class ComparaNumero {
    public static void main(String[] args) {
        int numero1 = 10;
        int numero2 = 20;
        compararNumeros(numero1, numero2);
    }

    public static void compararNumeros(int numero1, int numero2) {
        if (numero1 == numero2) {
            System.out.println("Os números são iguais: " + numero1);
        } else {
            System.out.println("Os números são diferentes.");

            int maior = Math.max(numero1, numero2); // Encontra o maior número
            int menor = Math.min(numero1, numero2); // Encontra o menor número

            System.out.println("O maior número é: " + maior);
            System.out.println("O menor número é: " + menor);
        }
    }
}