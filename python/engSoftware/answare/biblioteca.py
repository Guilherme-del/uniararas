class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo):
        self.livros.append(titulo)

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro == titulo:
                return livro
        return None

    def remover_livro(self, titulo):
        self.livros.remove(titulo)
