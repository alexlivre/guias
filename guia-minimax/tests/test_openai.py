import pytest
from src.openai_client import (
    send_chat_completion,
    send_native_format,
    send_with_thinking_disabled,
    parse_think_tags,
)


class TestOpenAITextGeneration:
    def test_send_basic_message(self):
        response = send_chat_completion()
        assert response.choices[0].message.content
        assert response.usage.prompt_tokens > 0
        assert response.usage.completion_tokens > 0

    def test_send_with_custom_prompt(self):
        response = send_chat_completion(
            user_message="Say 'hello' in French."
        )
        content = response.choices[0].message.content.lower()
        assert "bonjour" in content

    def test_reasoning_split_enabled(self):
        response = send_chat_completion(reasoning_split=True)
        message = response.choices[0].message
        model_dump = message.model_dump()
        assert "reasoning_details" in model_dump

    def test_thinking_disabled(self):
        response = send_with_thinking_disabled()
        content = response.choices[0].message.content
        thinking_present = "<think>" in (content or "")
        assert not thinking_present
        assert content

    def test_different_models(self):
        for model in ["MiniMax-M3", "MiniMax-M2.7", "MiniMax-M2.7-highspeed"]:
            response = send_chat_completion(model=model)
            assert response.model.startswith("MiniMax")
            assert response.choices[0].message.content


class TestThinkTagNativeFormat:
    def test_native_format_contains_think_tag(self):
        response = send_native_format()
        content = response.choices[0].message.content
        assert "<think>" in content
        assert "</think>" in content

    def test_parse_think_tags_extracts_thinking_and_text(self):
        content = "<think>Let me calculate.\n</think>\n\nThe answer is 4."
        parsed = parse_think_tags(content)
        assert "Let me calculate" in parsed["thinking"]
        assert "answer is 4" in parsed["text"]

    def test_parse_think_tags_with_real_response(self):
        response = send_native_format()
        content = response.choices[0].message.content
        parsed = parse_think_tags(content)
        assert parsed["thinking"]
        assert not "<think>" in parsed["text"]
        assert not "<think>" in parsed["thinking"]
