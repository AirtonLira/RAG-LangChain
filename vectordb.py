import requests

class Embeddings:
    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key

    def get_embeddings(self, docs):
        # Converte os objetos Document em dicionários ou outro formato serializável
        payload = {"documents": [doc.to_dict() for doc in docs]}
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(self.endpoint, json=payload, headers=headers)
        return response.json()

def url_to_retriver():
    endpoint = "your_endpoint_here"
    api_key = "your_api_key_here"
    embeddings = Embeddings(endpoint, api_key)
    
    # Supondo que 'docs' é uma lista de objetos Document
    docs = get_documents_somehow()
    embeddings_response = embeddings.get_embeddings(docs)
    return embeddings_response

# Exemplo de implementação de to_dict() para a classe Document
class Document:
    def __init__(self, content):
        self.content = content

    def to_dict(self):
        return {"content": self.content}

# Função fictícia para obter documentos
def get_documents_somehow():
    # Retorna uma lista de objetos Document
    return [Document("Example content 1"), Document("Example content 2")]

if __name__ == "__main__":
    teste = url_to_retriver()
    print(teste)
