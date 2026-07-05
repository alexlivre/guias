import pytest
from src.anthropic_client import (
    send_text_message,
    send_thinking_message,
    count_tokens,
)


class TestAnthropicTextGeneration:
    def test_send_basic_message(self):
        response = send_text_message()
        assert response.content
        assert response.usage.input_tokens > 0
        assert response.usage.output_tokens > 0

    def test_send_with_custom_prompt(self):
        response = send_text_message(
            user_message="Say 'hello' in Portuguese."
        )
        text_blocks = [b for b in response.content if b.type == "text"]
        combined = " ".join(b.text for b in text_blocks)
        assert "olá" in combined.lower() or "oi" in combined.lower()

    def test_different_models(self):
        for model in ["MiniMax-M3", "MiniMax-M2.7", "MiniMax-M2.7-highspeed"]:
            response = send_text_message(model=model)
            assert response.content

    def test_thinking_block(self):
        response = send_thinking_message()
        thinking_blocks = [b for b in response.content if b.type == "thinking"]
        text_blocks = [b for b in response.content if b.type == "text"]
        assert thinking_blocks
        assert text_blocks


class TestAnthropicTokenCounting:
    def test_count_tokens(self):
        token_count = count_tokens("Hello, how are you today?")
        assert token_count > 0
