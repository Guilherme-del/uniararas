public class ControleRemotoTV {
    private boolean ligada;
    private int volume;
    private int canal;

    public ControleRemotoTV() {
        ligada = false;
        volume = 10;
        canal = 1;
    }

    public void ligar() {
        ligada = true;
        System.out.println("A TV está ligada.");
    }

    public void desligar() {
        ligada = false;
        System.out.println("A TV está desligada.");
    }

    public void aumentarVolume() {
        if (ligada && volume < 100) {
            volume++;
            System.out.println("Volume aumentado para " + volume);
        }
    }

    public void diminuirVolume() {
        if (ligada && volume > 0) {
            volume--;
            System.out.println("Volume diminuído para " + volume);
        }
    }

    public void trocarCanal(int novoCanal) {
        if (ligada && novoCanal >= 1 && novoCanal <= 100) {
            canal = novoCanal;
            System.out.println("Canal alterado para " + canal);
        }
    }

    public void mostrarInformacoes() {
        System.out.println("Status da TV:");
        System.out.println("TV " + (ligada ? "ligada" : "desligada"));
        System.out.println("Canal atual: " + canal);
        System.out.println("Volume: " + volume);
    }
}
