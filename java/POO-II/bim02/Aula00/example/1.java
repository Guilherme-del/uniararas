/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.exemplo1;

import java.util.Scanner;

/**
 *
 * @author m4rci
 */
public class Exemplo1 {
    public static void main(String[] args) {
       
        /*comentarios em bloco
        comentarios em bloco*/
        //comentário unica linha
        
        //Exibindo frases na tela
        System.out.print("Um texto qualquer\n");
        System.out.println("Esse é o print line");
        
        //Variáveis
        int varInteira = 10;
        float varReal = 20.0f;
        boolean verdadeFalso = true; //false - 1 ou 0
        String meuTexto = "Marcilio Oliveira";
        
        System.out.println("Permite exibir dados das variáveis");
        System.out.println(varInteira);
        System.out.println("Meu número de ponto flutuante é" + varReal);
        System.out.println("Minha variável boolean é" + verdadeFalso);
        System.out.println(meuTexto);
        
        //Leitura de dados numérico do teclado
        Scanner sc = new Scanner(System.in);
        
        int meuNumero = sc.nextInt();
        float meuNumeroFlutuante = sc.nextFloat();
        
        //realizando o descarte de dados contidos no buffer
        sc.nextLine();
        
        String meuInputTextual = sc.nextLine();
    }
}