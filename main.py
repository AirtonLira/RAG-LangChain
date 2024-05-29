from langchain import OpenAI, PromptTemplate, LLMChain

openai = OpenAI(api_key="SUA_CHAVE_API")

prompt_template = PromptTemplate(
    template="Quantos Oscars o filme {filme} ganhou em {ano}?",
    input_variables=["filme", "ano"]
)

llm_chain = LLMChain(llm=openai, prompt=prompt_template)

resposta = llm_chain.run(filme="Openheimer", ano="2024")
print(resposta)
