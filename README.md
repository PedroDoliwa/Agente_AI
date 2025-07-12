# 🧑‍⚖️ Agente Jurídico Inteligente (IA)

Este projeto é um agente de IA baseado em Python, LangChain, Ollama e ChromaDB, treinado para responder perguntas sobre **leis penais brasileiras**, com foco em **roubo e furto** conforme o Código Penal.

## ✅ Funcionalidades

- 🔍 Respostas com base em textos reais da legislação
- 📚 Recuperação vetorial de leis penais (furto, roubo, latrocínio, etc.)
- 🧠 Modelo local usando `llama3.2` (via Ollama)
- 💬 Interação em linguagem natural com o usuário
- 🗂️ Estrutura modular com separação de vetorização e execução

---

## 📁 Estrutura do Projeto
├── main.py # Executa o chatbot

├── vector.py # Faz ingestão dos dados e cria o retriever

├── leis_roubo_reais.csv # Base de dados com 50 leis reais (furto/roubo)

├── README.md # Este arquivo


---

## ⚙️ Requisitos

- Python 3.10+
- [Ollama](https://ollama.com) instalado e rodando (`ollama run llama3`)
- Modelos baixados: `llama3.2` e `mxbai-embed-large`
- Bibliotecas Python:

```bash
pip install langchain langchain_community langchain-core langchain_chroma langchain_ollama pandas
````

----
Como Rodar
Inicie o servidor Ollama (caso não esteja rodando):
```
ollama run llama3
```

Execute o chatbot:
```
python main.py
```
---

## 🧪Exemplos de perguntas jurídicas

→ Qual a pena para o roubo com arma de fogo?

→ O que é considerado furto noturno?

→ Roubo contra idoso tem agravante?

→ E se o roubo for cometido em transporte coletivo?

→ Qual a diferença entre roubo simples e latrocínio?
