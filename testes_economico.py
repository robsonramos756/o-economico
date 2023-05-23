import unittest

from economico import *


class TesteEconomico(unittest.TestCase):

    def setUp(self):
        self.chatbot = iniciar()

    def test_questao1(self):
        pergunta = "Qual a maior economia do planeta?"
        resposta_esperada = "A maior economia do planeta é os Estados Unidos."

        resposta = self.chatbot.get_response(pergunta)

        self.assertEqual(resposta.text, resposta_esperada)
    
    def test_questao2(self):
        pergunta = "Qual o maior bloco econômico do planeta?"
        resposta_esperada = "O maior bloco econômico do planeta é a União Europeia."

        resposta = self.chatbot.get_response(pergunta)

        self.assertEqual(resposta.text, resposta_esperada)

    def test_questao3(self):
        pergunta = "Qual o país que registrou a maior alta do PIB em 2019?"
        resposta_esperada = "O país que registrou a maior alta do PIB em 2019 foi a China."

        resposta = self.chatbot.get_response(pergunta)

        self.assertEqual(resposta.text, resposta_esperada)

    def test_questao4(self):
        pergunta = "País que registrou a maior queda no PIB em 2019?"
        resposta_esperada = "A maior queda no PIB em 2019 foi a Venezuela."

        resposta = self.chatbot.get_response(pergunta)

        self.assertEqual(resposta.text, resposta_esperada)

    def test_questao5(self):
        pergunta = "Qual o PIB global em 2019?"
        resposta_esperada = "O PIB global em 2019 foi de 87,75 trilhões de dólares."

        resposta = self.chatbot.get_response(pergunta)

        self.assertEqual(resposta.text, resposta_esperada)    
        

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteEconomico))

    executor = unittest.TextTestRunner()
    executor.run(testes)


