from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import json

def iniciar():
    # Configuração do chatbot
    chatbot = ChatBot(
        'Economico',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.db',
        read_only=True,
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace'
        ],
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'Não tenho uma resposta para essa pergunta, tente novamente.',
                'maximum_similarity_threshold': 0.6
            }
        ],
        input_adapter='chatterbot.input.TerminalAdapter',
        output_adapter='chatterbot.output.TerminalAdapter',
        io_adapter='chatterbot.adapters.io.NoIOAdapter',
        language='pt',
        encoding='utf-8'
    )

    arquivos_conversas = [
        'conversas/saudacoes.json',
        'conversas/questoes.json',
    ]

    # Treina o chatbot
    trainer = ListTrainer(chatbot)

    for arquivo in arquivos_conversas:
        with open(arquivo, 'r', encoding='utf-8') as file:
            data = json.load(file)

        pergs = data['perguntas_respostas']

        for perg in pergs:
            pergunta = perg['pergunta']
            resposta = perg['resposta']
            trainer.train([pergunta, resposta])

    
    trainer_corpus = ChatterBotCorpusTrainer(chatbot)
    trainer_corpus.train("chatterbot.corpus.portuguese")

    return chatbot


def interagir(chatbot):
    while True:
        pergunta = input("Diga algo ao Econômico: ")
        resposta = chatbot.get_response(pergunta)
        print(">>", resposta.text)


# Iniciar o chatbot
if __name__ == '__main__':
    chatbot = iniciar()
    interagir(chatbot)
