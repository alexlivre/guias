from openai import OpenAI

from src.config import OPENAI_BASE_URL, MINIMAX_API_KEY, DEFAULT_MODEL


def send_image_url(
    image_url: str,
    prompt: str = "Describe what you see in this image.",
    model: str = DEFAULT_MODEL,
    max_tokens: int = 1000,
):
    client = OpenAI(
        base_url=OPENAI_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                            "detail": "low",
                        },
                    },
                ],
            }
        ],
    )
    return response
