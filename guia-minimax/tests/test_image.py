import pytest
from src.image_client import generate_images, generate_with_retry


TEST_PROMPT = "Pôr do sol na praia, cores vibrantes, estilo cinematográfico"


class TestImageGeneration:
    def test_basic_text_to_image(self):
        data = generate_images(prompt=TEST_PROMPT, n=1)
        assert data["base_resp"]["status_code"] == 0
        assert data["data"]["image_base64"]
        assert len(data["data"]["image_base64"]) == 1

    def test_multiple_images_n9(self):
        data = generate_images(prompt=TEST_PROMPT, n=9, timeout=120)
        assert data["base_resp"]["status_code"] == 0
        assert len(data["data"]["image_base64"]) == 9

    def test_with_seed(self):
        seed = 12345
        data = generate_images(prompt=TEST_PROMPT, n=1, seed=seed)
        assert data["base_resp"]["status_code"] == 0
        assert data["data"]["image_base64"]

    def test_with_prompt_optimizer(self):
        data = generate_images(prompt=TEST_PROMPT, n=1, prompt_optimizer=True)
        assert data["base_resp"]["status_code"] == 0

    def test_different_aspect_ratios(self):
        for ratio in ["1:1", "16:9", "4:3"]:
            data = generate_images(prompt=TEST_PROMPT, aspect_ratio=ratio, n=1)
            assert data["base_resp"]["status_code"] == 0
            assert data["data"]["image_base64"]

    def test_url_response_format(self):
        data = generate_images(
            prompt=TEST_PROMPT, n=1, response_format="url"
        )
        assert data["base_resp"]["status_code"] == 0
        assert data["data"]["image_urls"]
        assert len(data["data"]["image_urls"]) == 1


class TestImageErrorHandling:
    def test_generate_with_retry_success(self):
        data = generate_with_retry(prompt=TEST_PROMPT)
        assert data["base_resp"]["status_code"] == 0
