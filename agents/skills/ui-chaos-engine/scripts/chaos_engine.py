import random
import argparse
import json
import sys
import os


REQUIRED_KEYS = [
    "metafora",
    "paleta",
    "tipografia",
    "layout",
    "animacao",
    "copy_voice",
    "distinctive_reference",
]
REQUIRED_KEYS_SET = set(REQUIRED_KEYS)


def parse_options(data):
    if not isinstance(data, dict):
        print("Error: JSON root must be an object", file=sys.stderr)
        sys.exit(1)

    given_keys = set(data.keys())
    if given_keys != REQUIRED_KEYS_SET:
        missing = REQUIRED_KEYS_SET - given_keys
        extra = given_keys - REQUIRED_KEYS_SET
        parts = []
        if missing:
            parts.append(f"missing keys: {', '.join(sorted(missing))}")
        if extra:
            parts.append(f"unexpected keys: {', '.join(sorted(extra))}")
        print(f"Error: invalid structure — {'; '.join(parts)}", file=sys.stderr)
        sys.exit(1)

    for key in REQUIRED_KEYS:
        val = data[key]
        if not isinstance(val, list) or not val:
            print(f"Error: '{key}' must be a non-empty list of strings", file=sys.stderr)
            sys.exit(1)
        for item in val:
            if not isinstance(item, str):
                print(f"Error: '{key}' contains non-string item: {item!r}", file=sys.stderr)
                sys.exit(1)

    return data


def load_options(path):
    if not os.path.exists(path):
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON — {e}", file=sys.stderr)
        sys.exit(1)

    return parse_options(data)


def load_options_stdin():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON from stdin — {e}", file=sys.stderr)
        sys.exit(1)

    return parse_options(data)


def weighted_choice(options, weights=None):
    if weights is None:
        return random.choice(options)
    return random.choices(options, weights=weights, k=1)[0]


def generate(options, seed=None, weights=None):
    if seed is not None:
        random.seed(seed)

    result = {}
    for key in REQUIRED_KEYS:
        if weights and key in weights:
            result[key] = weighted_choice(options[key], weights[key])
        else:
            result[key] = random.choice(options[key])
    return result


def main():
    parser = argparse.ArgumentParser(
        description="UI Chaos Engine v2.0 — Anti-AI Slop Edition"
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--options", help="Caminho para arquivo JSON com listas de opções")
    source.add_argument("--stdin", action="store_true", help="Ler JSON de opções do stdin (pipe)")
    parser.add_argument("--seed", type=int, help="Semente aleatória para resultados reproduzíveis")
    parser.add_argument("--json", action="store_true", help="Saída em formato JSON")
    parser.add_argument("--weights", help="JSON com pesos por categoria para bias anti-slop")
    args = parser.parse_args()

    if args.stdin:
        options = load_options_stdin()
    else:
        options = load_options(args.options)

    weights = None
    if args.weights:
        try:
            weights = json.loads(args.weights)
        except json.JSONDecodeError as e:
            print(f"Error: invalid weights JSON — {e}", file=sys.stderr)
            sys.exit(1)

    rolls = generate(options, args.seed, weights)

    if args.json:
        json.dump(rolls, sys.stdout, ensure_ascii=False, indent=2)
        print()
        return

    labels = {
        "metafora": "1. Metáfora / Conceito Central",
        "paleta": "2. Paleta de Cores",
        "tipografia": "3. Tipografia",
        "layout": "4. Layout / Estrutura",
        "animacao": "5. Animação / Interatividade",
        "copy_voice": "6. Voz de Copy (Anti-Slop)",
        "distinctive_reference": "7. Distinctive Reference",
    }

    print("=" * 60)
    print("  [UI CHAOS ENGINE v2.0 — Anti-AI Slop Edition]")
    print("=" * 60)
    print()

    for key, label in labels.items():
        print(f"  {label}")
        print(f"    -> {rolls[key]}")
        print()

    if args.seed is not None:
        print(f"  Semente: {args.seed}")

    print("=" * 60)
    print("  Use isto como sua direção criativa.")
    print("  Valide contra references/anti-slop-patterns.md antes de aplicar.")
    print("=" * 60)


if __name__ == "__main__":
    main()