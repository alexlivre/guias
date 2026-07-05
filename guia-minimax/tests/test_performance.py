import random
import time

import pytest

from src.anthropic_client import get_client


PERFORMANCE_PROMPT = (
    "Write a detailed 1000-word essay about the history and future of "
    "artificial intelligence. Cover the following topics in depth: "
    "the Turing test, symbolic AI vs connectionism, deep learning "
    "revolution, transformer architecture, large language models, "
    "multimodal AI, agentic systems, reasoning models, alignment "
    "research, open-source vs proprietary models, AI regulation "
    "worldwide, economic impact, ethical concerns, and predictions "
    "for the next decade. Be thorough and specific."
)

MODELS = ["MiniMax-M2.7-highspeed", "MiniMax-M2.7"]

RUNS_PER_MODEL = 5


def measure_tps(model: str) -> dict:
    client = get_client()
    start = time.perf_counter()

    response = client.messages.create(
        model=model,
        max_tokens=2000,
        system="You are a helpful assistant. Write a comprehensive, detailed response.",
        messages=[{"role": "user", "content": PERFORMANCE_PROMPT}],
    )

    elapsed = time.perf_counter() - start
    output_tokens = response.usage.output_tokens
    tps = output_tokens / elapsed if elapsed > 0 else 0

    return {
        "model": model,
        "elapsed_seconds": round(elapsed, 2),
        "output_tokens": output_tokens,
        "tps": round(tps, 1),
        "input_tokens": response.usage.input_tokens,
    }


class TestPerformance:
    @pytest.mark.parametrize("model", MODELS)
    def test_model_responds(self, model):
        result = measure_tps(model)
        assert result["output_tokens"] > 0
        assert result["tps"] > 0

    def test_tps_comparison(self):
        all_results = {m: [] for m in MODELS}

        all_runs = []
        for i in range(RUNS_PER_MODEL):
            random.shuffle(MODELS)
            for model in MODELS:
                all_runs.append((i + 1, model))

        for run_num, model in all_runs:
            result = measure_tps(model)
            all_results[model].append(result)
            print(f"  Run {run_num:2d} | {model:26s} | "
                  f"TPS: {result['tps']:5.1f} | "
                  f"Out: {result['output_tokens']:4d} tok | "
                  f"Tempo: {result['elapsed_seconds']:.2f}s")

        print(f"\n  {'='*60}")
        print(f"  {'MEDIA FINAL':^60s}")
        print(f"  {'='*60}")

        final = []
        for model in MODELS:
            tps_list = [r["tps"] for r in all_results[model]]
            tok_list = [r["output_tokens"] for r in all_results[model]]
            time_list = [r["elapsed_seconds"] for r in all_results[model]]

            avg_tps = sum(tps_list) / len(tps_list)
            avg_tok = sum(tok_list) / len(tok_list)
            avg_time = sum(time_list) / len(time_list)

            final.append({
                "model": model,
                "avg_tps": round(avg_tps, 1),
                "avg_output_tokens": round(avg_tok, 1),
                "avg_time_seconds": round(avg_time, 2),
            })

            print(f"\n  {model}:")
            print(f"    TPS medio:           {avg_tps:.1f}")
            print(f"    Output tokens medio: {avg_tok:.0f}")
            print(f"    Tempo total medio:   {avg_time:.2f}s")

        highspeed = next(f for f in final if "highspeed" in f["model"])
        m27 = next(f for f in final if f["model"] == "MiniMax-M2.7")

        assert highspeed["avg_tps"] > 0
        assert m27["avg_tps"] > 0

        ratio = highspeed["avg_tps"] / m27["avg_tps"]
        print(f"\n  {'='*60}")
        print(f"  M2.7-highspeed vs M2.7: {ratio:.2f}x")
        if ratio >= 1.0:
            print(f"  Highspeed eh {ratio:.2f}x mais rapido")
        else:
            print(f"  Highspeed eh {ratio:.2f}x do M2.7 normal")
