/*
7) Construa uma classe que apresente as funções de um controle remoto de um aparelho de
televisão. Instancie o objeto dessa classe no main e faça uso dos métodos que ela expõe.
*/

public class Main {
    public static void main(String[] args) {
        ControleRemotoTV controle = new ControleRemotoTV();

        controle.ligar();
        controle.aumentarVolume();
        controle.trocarCanal(5);
        controle.mostrarInformacoes();
        controle.desligar();
    }
}