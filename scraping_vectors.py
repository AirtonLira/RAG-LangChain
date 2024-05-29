from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

loader = WebBaseLoader("https://pt.wikipedia.org/wiki/Filme_Openheimer")
documents = loader.load()

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)

retriever = vectorstore.as_retriever()
