public class Controlador {
    private static IBancoDeDadosProdutos bancoDeDados;

    static {
        bancoDeDados = BancoDeDadosProdutos.getInstance();
    }

    public static void consultarValorTotal() {
        System.out.println("O valor total dos produtos é: " + bancoDeDados.consultarValorTotal());
    }

    public static void inserirProduto() {
        System.out.println("Digite o código do produto: ");
        int codigo = Integer.parseInt(System.console().readLine());

        System.out.println("Digite o nome do produto: ");
        String nome = System.console().readLine();

        System.out.println("Digite o volume do produto: ");
        float volume = Float.parseFloat(System.console().readLine());

        System.out.println("Digite o peso do produto: ");
        float peso = Float.parseFloat(System.console().readLine());

        System.out.println("Digite o valor do produto: ");
        float valor = Float.parseFloat(System.console().readLine());

        Produto produto = new Produto(codigo, nome, volume, peso, valor);
        bancoDeDados.inserir(produto);
        System.out.println("Produto inserido com sucesso!");
    }

    public static void removerProduto() {
        System.out.println("Digite o código do produto a ser removido: ");
        int codigo = Integer.parseInt(System.console().readLine());

        bancoDeDados.remover(codigo);
        System.out.println("Produto removido com sucesso!");
    }

    public static Produto consultarProduto() {
        System.out.println("Digite o código do produto a ser consultado: ");
        int codigo = Integer.parseInt(System.console().readLine());

        Produto produto = bancoDeDados.consultar(codigo);
        if (produto == null) {
            System.out.println("Produto não encontrado!");
        } else {
            System.out.println(produto);
        }
        return produto;
    }

    public static void editarProduto() {
        System.out.println("Digite o código do produto a ser editado: ");
        int codigo = Integer.parseInt(System.console().readLine());

        Produto produto = bancoDeDados.consultar(codigo);
        if (produto == null) {
            System.out.println("Produto não encontrado!");
        } else {
            System.out.println("Digite o novo nome do produto: ");
            String nome = System.console().readLine();

            System.out.println("Digite o novo volume do produto: ");
            float volume = Float.parseFloat(System.console().readLine());

            System.out.println("Digite o novo peso do produto: ");
            float peso = Float.parseFloat(System.console().readLine());

            System.out.println("Digite o novo valor do produto: ");
            float valor = Float.parseFloat(System.console().readLine());

            produto.setNome(nome);
            produto.setVolume(volume);
            produto.setPeso(peso);
            produto.setValor(valor);
            bancoDeDados.inserir(produto);
            System.out.println("Produto editado com sucesso!");
        }
    }
}