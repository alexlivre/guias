import base64
import pytest
from src.multimodal import send_image_url

MINI_PNG_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPj/HwADBwIAMCbHYQ"
    "AAAABJRU5ErkJggg=="
)
TEST_IMAGE = f"data:image/png;base64,{MINI_PNG_BASE64}"


class TestMultimodal:
    def test_image_url_analysis(self):
        response = send_image_url(image_url=TEST_IMAGE)
        content = response.choices[0].message.content
        assert content
        assert len(content) > 10
