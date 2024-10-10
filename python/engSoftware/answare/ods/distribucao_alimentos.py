class DistribuicaoAlimentos:
    def __init__(self):
        self.estoque = {}

    def adicionar_doacao(self, alimento, quantidade):
        if alimento not in self.estoque:
            self.estoque[alimento] = 0
        self.estoque[alimento] += quantidade

    def distribuir_alimento(self, alimento, quantidade):
        if alimento not in self.estoque or self.estoque[alimento] < quantidade:
            raise ValueError("Quantidade insuficiente no estoque")
        self.estoque[alimento] -= quantidade

    def verificar_estoque(self, alimento):
        return self.estoque.get(alimento, 0)
