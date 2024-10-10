import unittest
from distribucao_alimentos import DistribuicaoAlimentos

class TestDistribuicaoAlimentos(unittest.TestCase):
    def setUp(self):
        self.distribuicao = DistribuicaoAlimentos()

    def test_adicionar_doacao(self):
        self.distribuicao.adicionar_doacao("arroz", 10)
        self.assertEqual(self.distribuicao.verificar_estoque("arroz"), 10)

    def test_distribuir_alimento(self):
        self.distribuicao.adicionar_doacao("feijao", 15)
        self.distribuicao.distribuir_alimento("feijao", 5)
        self.assertEqual(self.distribuicao.verificar_estoque("feijao"), 10)

    def test_distribuir_alimento_sem_estoque_suficiente(self):
        self.distribuicao.adicionar_doacao("arroz", 5)
        with self.assertRaises(ValueError):
            self.distribuicao.distribuir_alimento("arroz", 10)

# Rodando os testes
if __name__ == '__main__':
    unittest.main(verbosity=2)
