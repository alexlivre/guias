import pytest
from src.streaming import stream_anthropic, stream_openai


class TestStreamingAnthropic:
    def test_anthropic_stream_collects_content(self):
        result = stream_anthropic("Count from 1 to 3.")
        assert result["text"]
        assert "1" in result["text"]
        assert "2" in result["text"]
        assert "3" in result["text"]

    def test_anthropic_stream_with_thinking(self):
        result = stream_anthropic(
            "What is 15 + 7? Explain step by step."
        )
        assert result["text"]


class TestStreamingOpenAI:
    def test_openai_stream_collects_content(self):
        result = stream_openai("Count from 1 to 5.")
        assert result["text"]
        for num in ["1", "2", "3", "4", "5"]:
            assert num in result["text"]
