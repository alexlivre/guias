import json
from anthropic import Anthropic
from openai import OpenAI

from src.config import ANTHROPIC_BASE_URL, OPENAI_BASE_URL, MINIMAX_API_KEY, DEFAULT_MODEL


WEATHER_TOOLS = [
    {
        "name": "get_weather",
        "description": "Get weather of a location, the user should supply a location first.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, US",
                }
            },
            "required": ["location"],
        },
    }
]

WEATHER_TOOLS_OPENAI = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply a location first.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, US",
                    }
                },
                "required": ["location"],
            },
        },
    }
]


def tool_use_anthropic(
    user_message: str = "How's the weather in San Francisco?",
    model: str = DEFAULT_MODEL,
    max_tokens: int = 4096,
):
    client = Anthropic(
        base_url=ANTHROPIC_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )
    messages = [{"role": "user", "content": user_message}]

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=messages,
        tools=WEATHER_TOOLS,
    )
    return response, messages


def continue_with_tool_result(response, messages):
    client = Anthropic(
        base_url=ANTHROPIC_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )
    tool_use_blocks = [b for b in response.content if b.type == "tool_use"]
    tool_use_block = tool_use_blocks[0]

    messages.append({"role": "assistant", "content": response.content})
    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": "24℃, sunny",
                }
            ],
        }
    )

    final_response = client.messages.create(
        model=DEFAULT_MODEL,
        max_tokens=4096,
        messages=messages,
        tools=WEATHER_TOOLS,
    )
    return final_response


def tool_use_openai(
    user_message: str = "How's the weather in San Francisco?",
    model: str = DEFAULT_MODEL,
    max_tokens: int = 4096,
):
    client = OpenAI(
        base_url=OPENAI_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )
    messages = [{"role": "user", "content": user_message}]

    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=messages,
        tools=WEATHER_TOOLS_OPENAI,
        extra_body={"reasoning_split": True},
    )
    return response, messages


def continue_with_tool_result_openai(response, messages, max_tokens: int = 4096):
    client = OpenAI(
        base_url=OPENAI_BASE_URL,
        api_key=MINIMAX_API_KEY,
    )
    tool_call = response.choices[0].message.tool_calls[0]
    function_args = json.loads(tool_call.function.arguments)

    messages.append(response.choices[0].message)
    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": "24℃, sunny",
        }
    )

    final_response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        max_tokens=max_tokens,
        messages=messages,
        tools=WEATHER_TOOLS_OPENAI,
        extra_body={"reasoning_split": True},
    )
    return final_response, function_args
