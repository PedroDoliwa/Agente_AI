from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
Você é um assistente jurídico brasileiro que responde perguntas com base na legislação penal.

Aqui estão alguns trechos relevantes de leis:
{reviews}

Pergunta do usuário:
{question}

Responda de forma clara, objetiva, e cite o artigo quando possível.
Se a pergunta não tiver relação com os trechos fornecidos, diga: 
"Não localizei base legal nos documentos fornecidos."
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Digite sua pergunta jurídica (x para encerrar): ")
    print("\n\n")
    if question == "x":
        break
    
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print("\nResposta:\n", result)

    print("\n[Fontes utilizadas:]\n")
    for i, doc in enumerate(reviews):
        print(f"{i+1}. Artigo {doc.metadata.get('artigo')} – {doc.page_content}")
