````markdown
# ⚡ Velox

> A fast AI-powered search agent built with LangChain, Groq, Google Serper, and Streamlit.

Velox is an AI agent that combines the high-speed inference of Groq with Google Search capabilities through the Serper API. The agent can determine when external information is required, use the search tool to retrieve relevant results, and generate a natural-language response through an interactive Streamlit interface.

## ✨ Features

- ⚡ High-speed inference with Groq
- 🤖 LangChain AI agent
- 🔎 Google Search using Serper API
- 🧠 Agent-based tool calling
- 🔄 Real-time streaming responses
- 💬 Interactive Streamlit chat interface
- 📝 Conversation history
- 🔐 Environment-based API key management

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Groq**
- **Google Serper API**
- **Streamlit**
- **python-dotenv**

## 🧠 How Velox Works

```text
                User Query
                    │
                    ▼
              ┌───────────┐
              │   Velox   │
              │ AI Agent  │
              └─────┬─────┘
                    │
             ┌──────┴──────┐
             │             │
        Direct Answer   Needs Search?
             │             │
             │            YES
             │             ▼
             │       Google Serper
             │          Search
             │             │
             │             ▼
             │       Search Results
             │             │
             └──────┬──────┘
                    ▼
                Groq LLM
                    │
                    ▼
            Streaming Response
                    │
                    ▼
              Streamlit UI
````

## 🔧 Tools

### Google Search

Velox uses the Google Serper API through LangChain to provide the agent with web-search capabilities.

This allows the agent to retrieve information that may be:

* Current or time-sensitive
* Not available in the model's knowledge
* Requiring external sources
* Related to recent events or updates

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/velox.git
cd velox
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

### 5. Run the application

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
Velox/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 🎯 Project Purpose

Velox was developed to explore how modern AI agents can combine an LLM with external tools to overcome the limitations of relying solely on model knowledge.

The project demonstrates:

* LLM integration
* AI agent architecture
* Tool calling
* Web search integration
* Streaming responses
* Conversational interfaces

## 🔮 Future Improvements

* [ ] Multi-tool agent
* [ ] RAG integration
* [ ] Persistent conversation memory
* [ ] Source citations
* [ ] Multiple LLM/model selection
* [ ] Authentication
* [ ] Cloud deployment

## 📄 License

This project is licensed under the MIT License.


