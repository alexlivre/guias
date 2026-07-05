from openai import OpenAI

from src.config import OPENAI_BASE_URL, MINIMAX_API_KEY, DEFAULT_MODEL


def get_client() -> OpenAI:
    return OpenAI(
        base_url=OPENAI_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )


def send_chat_completion(
    model: str = DEFAULT_MODEL,
    system_prompt: str = "You are a helpful assistant.",
    user_message: str = "Hi, how are you?",
    max_tokens: int = 1000,
    reasoning_split: bool = True,
):
    client = get_client()
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        extra_body={"reasoning_split": reasoning_split},
    )
    return response


def send_native_format(
    model: str = DEFAULT_MODEL,
    system_prompt: str = "You are a helpful assistant.",
    user_message: str = "What is 2+2? Explain step by step.",
    max_tokens: int = 2000,
):
    client = get_client()
    return client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        extra_body={"reasoning_split": False},
    )


def parse_think_tags(content: str) -> dict:
    thinking = ""
    text = content
    start_tag = "<think>"
    end_tag = "</think>"
    start = content.find(start_tag)
    end = content.find(end_tag)
    if start != -1 and end != -1:
        thinking = content[start + len(start_tag):end]
        text = content[:start] + content[end + len(end_tag):]
    return {"thinking": thinking.strip(), "text": text.strip()}


def send_with_thinking_disabled(
    model: str = DEFAULT_MODEL,
    user_message: str = "What is 2+2? Explain step by step.",
    max_tokens: int = 2000,
):
    client = get_client()
    return client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": user_message}],
        extra_body={"thinking": {"type": "disabled"}},
    )
