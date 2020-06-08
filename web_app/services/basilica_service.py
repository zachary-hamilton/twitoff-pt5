# web_app/services/basilica_service.py

import basilica
import os
from dotenv import load_dotenv


load_dotenv()

BASILICA_API_KEY = os.getenv('BASILICA_API_KEY')

connection = basilica.Connection(BASILICA_API_KEY)

def basilica_api_client():
    return connection
    
if __name__ == '__main__':
    sentences = ["Hello world!", "How are you?"]
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]