import unittest
from biblioteca import Biblioteca

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_adicionar_livro(self):
        self.biblioteca.adicionar_livro("Livro A")
        self.assertIn("Livro A", self.biblioteca.livros)

    def test_buscar_livro(self):
        self.biblioteca.adicionar_livro("Livro B")
        resultado = self.biblioteca.buscar_livro("Livro B")
        self.assertEqual(resultado, "Livro B")

    def test_remover_livro(self):
        self.biblioteca.adicionar_livro("Livro C")
        self.biblioteca.remover_livro("Livro C")
        self.assertNotIn("Livro C", self.biblioteca.livros)

if __name__ == '__main__':
    unittest.main()
