from langchain import OpenAI, ChatPromptTemplate, create_retrieval_chain
from your_module import url_to_retriever

openai = OpenAI(api_key="SUA_CHAVE_API")

retriever = url_to_retriever("https://pt.wikipedia.org/wiki/Filme_Openheimer")

prompt_template = ChatPromptTemplate(
    template="Quantos Oscars o filme {filme} ganhou em {ano}?",
    input_variables=["filme", "ano"]
)

chain = create_retrieval_chain(
    llm=openai,
    retriever=retriever,
    prompt_template=prompt_template
)

resposta = chain.run(filme="Openheimer", ano="2024")
print(resposta)
