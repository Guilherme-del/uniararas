/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.exemplo2;

import java.util.Scanner;

public class Exemplo2 {
    public static void main(String[] args) {
       
        Scanner sc = new Scanner(System.in);
        
        //Atribuir valores a um vetor inteiro
        int[] meusNumeros = {1, 2, 3, 4, 5, 6, 7};
        float[] meusNumerosReais = {10.0f, 11.1f, 34.0f };
        String[] meusTextos = { "Marcilio 3", "Joao", "Jose", "Joaquim" };
        
        System.out.println(meusNumeros[0]);
        System.out.println(meusNumeros[2]);
        System.out.println(meusNumerosReais[0]);
        
        //estrutura de repetição
        //percorrendo meu vetor de textos
        for (int i = 0; i < meusTextos.length; i++) {
            System.out.println(meusTextos[i]);
        }
        
        //Percorrendo com o for "menor"
        for (String texto : meusTextos) {
            System.out.println(texto);
            //para acessar um único caracter na varíavel do tipo string
            //usamos o método charAt(..indice da letra...)
            if (texto.charAt(0) == 'A') 
            {
                System.out.println("Encontrei a letra A");
            }
        }
        
        int[] meuVetorInteiro = new int[10];
        
        //Inserindo valores no meu vetor
        for(int i = 0; i < meuVetorInteiro.length; i++) {
            meuVetorInteiro[i] = sc.nextInt();
        }
        
        //Percorrer vetores
        for (int i : meuVetorInteiro) {
            System.out.println(i);
        }
    }
}