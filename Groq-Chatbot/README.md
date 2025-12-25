# Gemini Streamlit Chatbot

A small Streamlit-based chat UI that demonstrates both streaming and non-streaming responses using the Groq API.

## Table of contents

- [Built with](#built-with)
- [Quickstart](#quickstart)
- [Run](#run)
- [Usage](#usage)
- [Notes & troubleshooting](#notes--troubleshooting)
- [Author / Contact](#author--contact)
- [License](#license)

## Built with

- Python 3.10+
- Streamlit — UI and simple state management
- groq — Groq Python client
- python-dotenv — loads environment variables from `.env`

## Quickstart

1. Copy the example environment file and add your Groq API key:

```bash
cp .env.example .env
# then edit .env and set:
# GROQ_API_KEY=your_real_groq_api_key_here
```

On Windows (PowerShell):

```powershell
copy .env.example .env
# then edit .env and set GROQ_API_KEY
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\Activate.ps1 # Windows PowerShell
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the URL shown by Streamlit in your browser.

## Usage

- Type a prompt into the chat input and press Enter.
- Use the **Enable Streaming** toggle in the sidebar to switch between token-by-token streaming and full (non-streaming) responses.
- Chat messages persist for the session in Streamlit's session state.

## Notes & troubleshooting

- If you see **GROQ_API_KEY is not set**, ensure `.env` exists and contains `GROQ_API_KEY`, then restart the app.
- Network issues or invalid API keys will produce API errors surfaced in the UI.

## Author / Contact

- **Name:** mmrcode
- **Email:** mmrcode1@gmail.com
- **GitHub:** https://github.com/mmrcode/Groq-chatbot

## License

This project is provided as-is. Add a `LICENSE` file (for example MIT) before publishing.

