from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def url_to_retriever(url):
    loader = WebBaseLoader(url)
    documents = loader.load()

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    return vectorstore.as_retriever()
