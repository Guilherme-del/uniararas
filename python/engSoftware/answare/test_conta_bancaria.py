# test_conta_bancaria.py
import unittest
from conta_bancaria import ContaBancaria

class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria(100)

    def test_depositar(self):
        self.conta.depositar(50)
        self.assertEqual(self.conta.verificar_saldo(), 150)

    def test_sacar(self):
        self.conta.sacar(30)
        self.assertEqual(self.conta.verificar_saldo(), 70)

    def test_sacar_saldo_insuficiente(self):
        with self.assertRaises(ValueError):
            self.conta.sacar(200)

    def test_verificar_saldo(self):
        self.conta.depositar(50)
        self.conta.sacar(30)
        self.assertEqual(self.conta.verificar_saldo(), 120)

if __name__ == '__main__':
    unittest.main()
