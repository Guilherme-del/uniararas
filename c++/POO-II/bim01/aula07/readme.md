# Integrantes do grupo

| Nome | Ra |
| ------------- | ------------- |
| Wayner Moraes  | 109097  |
| Guilherme Cavenaghi | 109317 |
| Vinicius Rossi | 110273 |
| Caio Hernandez | 109049 |
| Valter Chieregatto | 109049 |
| Rafael Souza | 109680 |
| Bruno Silva | 109317 |

## Funcoes com polimorfismo

Função compartilhar na Classe Post:
Na classe Post, você pode adicionar a função compartilhar como uma função virtual pura. Isso permite que as classes derivadas, como TwitterPost e InstagramPost, 
O polimorfismo entra em ação quando você chama a função compartilhar em um objeto de uma classe derivada usando um ponteiro ou referência da classe base Post.

Função criarPost na Classe SocialNetwork:
Na função criarPost da classe SocialNetwork, você pode criar instâncias de TwitterPost ou InstagramPost com base na escolha da rede social,pois você pode armazenar esses objetos em um vetor de ponteiros para Post e chamar a função compartilhar.