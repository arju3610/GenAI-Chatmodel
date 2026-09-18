# GenAI Chatmodel

A collection of small LangChain examples for experimenting with chat models and text embeddings. The main application is a Streamlit **mood-based AI chatbot** that lets you chat with an angry, funny, or sad assistant personality.

## Features

- Streamlit chat interface with conversation memory for the current browser session
- Three selectable assistant personalities: Angry, Funny, and Sad
- Groq-powered chat model (`openai/gpt-oss-20b`)
- Command-line examples for Groq and Mistral chat models
- Hugging Face examples using both hosted endpoints and a local Transformers pipeline
- Text embedding examples using OpenAI and Hugging Face models

## Project structure

```text
.
|-- chatmodels/
|   |-- UIchatbot.py       # Streamlit mood-based chatbot (main app)
|   |-- chatbot.py         # Terminal-based Groq chatbot
|   |-- chat.py            # Basic Mistral chat-model example
|   |-- huggingface.py     # Hugging Face hosted-endpoint example
|   `-- localmodel.py      # Local TinyLlama pipeline example
|-- embeddingmodels/
|   |-- embeddings.py      # OpenAI embeddings example
|   `-- huggingface_embedding.py  # Hugging Face embeddings example
`-- requirements.txt
```

## Prerequisites

- Python 3.10 or newer
- An API key for the example you want to run:
  - Groq for the Streamlit app and `chatmodels/chatbot.py`
  - Mistral for `chatmodels/chat.py`
  - OpenAI for `embeddingmodels/embeddings.py`
  - Hugging Face token when required for hosted Hugging Face models

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/arju3610/GenAI-Chatmodel.git
cd GenAI-Chatmodel
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root. Add only the keys required by the script you run:

```env
GROQ_API_KEY=your_groq_api_key
MISTRAL_API_KEY=your_mistral_api_key
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token
```

The `.env` file is ignored by Git—do not commit credentials.

## Run the chatbot

Start the Streamlit application from the repository root:

```bash
streamlit run chatmodels/UIchatbot.py
```

Choose a mood, send messages in the chat box, use **Reset Chat** to clear the conversation, or enter `0` to end the current conversation.

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub. Do not commit `.env` or any API key.
2. Open [share.streamlit.io](https://share.streamlit.io/) and create a new app from the repository.
3. Set the main file path to `chatmodels/UIchatbot.py`.
4. In the app settings, add this secret:

  ```toml
  GROQ_API_KEY = "your_groq_api_key"
  ```

5. Deploy the app. Streamlit Cloud installs the packages from `requirements.txt` automatically.

For local development, keep using `.env` in the repository root and run `streamlit run chatmodels/UIchatbot.py`.

## Run individual examples

```bash
# Terminal-based Groq chatbot
python chatmodels/chatbot.py

# Mistral chat example
python chatmodels/chat.py

# Hugging Face hosted endpoint example
python chatmodels/huggingface.py

# Local TinyLlama pipeline (may download model files on first run)
python chatmodels/localmodel.py

# Embedding examples
python embeddingmodels/embeddings.py
python embeddingmodels/huggingface_embedding.py
```

## Notes

- Changing the selected mood in the Streamlit app starts a fresh conversation, so each mode has its own system instruction.
- The Streamlit app currently uses Groq. Its displayed HTTP error copy mentions Mistral; that message is cosmetic and does not affect the provider used.
- The local-model and Hugging Face examples can require substantial disk space, RAM, or a first-run model download.

## License

No license has been specified for this repository.
