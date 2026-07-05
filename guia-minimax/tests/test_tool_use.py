import pytest
from src.tool_use import (
    tool_use_anthropic,
    continue_with_tool_result,
    tool_use_openai,
    continue_with_tool_result_openai,
)


class TestToolUseAnthropic:
    def test_tool_call_response(self):
        response, messages = tool_use_anthropic()
        tool_use_blocks = [b for b in response.content if b.type == "tool_use"]
        assert tool_use_blocks
        assert tool_use_blocks[0].name == "get_weather"

    def test_tool_call_with_tool_result(self):
        response, messages = tool_use_anthropic()
        final_response = continue_with_tool_result(response, messages)
        text_blocks = [b for b in final_response.content if b.type == "text"]
        combined = " ".join(b.text for b in text_blocks)
        assert "24" in combined or "sunny" in combined.lower() or "°" in combined


class TestToolUseOpenAI:
    def test_tool_call_response(self):
        response, messages = tool_use_openai()
        assert response.choices[0].message.tool_calls
        tool_call = response.choices[0].message.tool_calls[0]
        assert tool_call.function.name == "get_weather"

    def test_tool_call_with_tool_result(self):
        response, messages = tool_use_openai()
        final_response, function_args = continue_with_tool_result_openai(response, messages)
        content = final_response.choices[0].message.content
        assert content
        assert "24" in content or "sunny" in content.lower() or "°" in content
