from anthropic import Anthropic
from openai import OpenAI

from src.config import ANTHROPIC_BASE_URL, OPENAI_BASE_URL, MINIMAX_API_KEY, DEFAULT_MODEL


def stream_anthropic(
    user_message: str = "Hi, how are you?",
    model: str = DEFAULT_MODEL,
    max_tokens: int = 1000,
):
    client = Anthropic(
        base_url=ANTHROPIC_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )
    stream = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are a helpful assistant.",
        messages=[{"role": "user", "content": user_message}],
        stream=True,
    )
    collected = {"thinking": "", "text": ""}
    for chunk in stream:
        if chunk.type == "content_block_delta":
            if hasattr(chunk, "delta") and chunk.delta:
                if chunk.delta.type == "thinking_delta":
                    collected["thinking"] += chunk.delta.thinking
                elif chunk.delta.type == "text_delta":
                    collected["text"] += chunk.delta.text
    return collected


def stream_openai(
    user_message: str = "Hi, how are you?",
    model: str = DEFAULT_MODEL,
    max_tokens: int = 1000,
):
    client = OpenAI(
        base_url=OPENAI_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )
    stream = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
        extra_body={"reasoning_split": True},
        stream=True,
    )
    collected = {"reasoning": "", "text": ""}
    for chunk in stream:
        delta = chunk.choices[0].delta if chunk.choices else None
        if delta:
            if hasattr(delta, "reasoning_details") and delta.reasoning_details:
                for detail in delta.reasoning_details:
                    if "text" in detail:
                        collected["reasoning"] = detail["text"]
            if delta.content:
                collected["text"] += delta.content
    return collected
