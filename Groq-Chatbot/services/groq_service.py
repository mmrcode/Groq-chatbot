import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Model to use
MODEL = "llama-3.1-8b-instant"


def _get_client():
    """Return a Groq client using `GROQ_API_KEY` from environment.

    Raises a RuntimeError with actionable instructions if the key is missing.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Copy .env.example to .env and set GROQ_API_KEY, "
            "or set the GROQ_API_KEY environment variable before running the app."
        )
    return Groq(api_key=api_key)


def get_chat_response(messages):
    """Non-streaming response"""
    client = _get_client()
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
    )
    return response.choices[0].message.content


def stream_chat_response(messages):
    """Streaming response generator yielding text deltas"""
    client = _get_client()
    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        stream=True,
    )

    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta and getattr(delta, "content", None):
            yield delta.content
