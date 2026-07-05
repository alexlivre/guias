from anthropic import Anthropic

from src.config import ANTHROPIC_BASE_URL, MINIMAX_API_KEY


LARGE_SYSTEM_PROMPT = """You are an AI assistant tasked with analyzing literary works.
Your goal is to provide insightful commentary on themes, characters, and writing style.
You should always respond in a clear, structured format.
When analyzing texts, consider the historical context, author's background,
and literary devices used. Provide specific examples from the text.
Your analysis should be thorough but accessible to a general audience."""


def passive_caching_example(
    model: str = "MiniMax-M3",
    max_tokens: int = 10240,
):
    client = Anthropic(
        base_url=ANTHROPIC_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )
    large_text = "The quick brown fox " * 200

    response1 = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=LARGE_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": large_text[:1000] + "\nSummarize this."}],
    )
    usage1 = response1.usage

    response2 = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=LARGE_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": large_text[:1000] + "\nSummarize this differently."}],
    )
    usage2 = response2.usage

    return usage1, usage2


def explicit_caching_anthropic(
    model: str = "MiniMax-M2.7",
    max_tokens: int = 1024,
):
    client = Anthropic(
        base_url=ANTHROPIC_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )
    large_text = "The quick brown fox " * 400

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=[
            {
                "type": "text",
                "text": LARGE_SYSTEM_PROMPT,
            },
            {
                "type": "text",
                "text": large_text,
                "cache_control": {"type": "ephemeral"},
            },
        ],
        messages=[
            {"role": "user", "content": "What are the major themes in this text?"}
        ],
    )
    return response.usage
