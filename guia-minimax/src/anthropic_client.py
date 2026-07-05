from anthropic import Anthropic

from src.config import ANTHROPIC_BASE_URL, MINIMAX_API_KEY, DEFAULT_MODEL


def get_client() -> Anthropic:
    return Anthropic(
        base_url=ANTHROPIC_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )


def send_text_message(
    model: str = DEFAULT_MODEL,
    system_prompt: str = "You are a helpful assistant.",
    user_message: str = "Hi, how are you?",
    max_tokens: int = 1000,
):
    client = get_client()
    return client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )


def send_thinking_message(
    model: str = DEFAULT_MODEL,
    system_prompt: str = "You are a helpful assistant.",
    user_message: str = "What is 2+2? Explain step by step.",
    max_tokens: int = 2000,
):
    client = get_client()
    return client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        thinking={"type": "adaptive"},
        messages=[{"role": "user", "content": user_message}],
    )


def count_tokens(text: str, model: str = DEFAULT_MODEL):
    client = get_client()
    response = client.messages.count_tokens(
        model=model,
        messages=[{"role": "user", "content": text}],
    )
    return response.input_tokens
