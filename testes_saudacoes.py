import unittest

from economico import *


class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.chatbot = iniciar()

    def test_saudacao1(self):
        pergunta = "olá"
        resposta_esperada = "Olá, sou o econômico. Qual a questão sobre a economia que você quer saber?"

        resposta = self.chatbot.get_response(pergunta)

        self.assertEqual(resposta.text, resposta_esperada)
    
    def test_saudacao2(self):
        pergunta = "bom dia"
        resposta_esperada = "Bom dia, sou o econômico. Qual a questão sobre a economia que você quer saber?"

        resposta = self.chatbot.get_response(pergunta)

        self.assertEqual(resposta.text, resposta_esperada)

    def test_saudacao3(self):
        pergunta = "boa tarde"
        resposta_esperada = "Boa tarde, sou o econômico. Qual a questão sobre a economia que você quer saber?"

        resposta = self.chatbot.get_response(pergunta)

        self.assertEqual(resposta.text, resposta_esperada)

    def test_saudacao4(self):
        pergunta = "boa noite"
        resposta_esperada = "Boa noite, sou o econômico. Qual a questão sobre a economia que você quer saber?"

        resposta = self.chatbot.get_response(pergunta)

        self.assertEqual(resposta.text, resposta_esperada)

    
        
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)
