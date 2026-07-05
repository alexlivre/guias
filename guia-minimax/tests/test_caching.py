import pytest
from src.caching import passive_caching_example, explicit_caching_anthropic


class TestPassiveCaching:
    def test_passive_caching_returns_usage(self):
        usage1, usage2 = passive_caching_example()
        assert usage1.input_tokens >= 0
        assert usage1.output_tokens >= 0
        assert usage2.input_tokens >= 0
        assert usage2.output_tokens >= 0


class TestExplicitCaching:
    def test_explicit_caching_anthropic(self):
        usage = explicit_caching_anthropic()
        assert usage.input_tokens >= 0
        assert usage.output_tokens >= 0
