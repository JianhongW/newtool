from __future__ import annotations

import argparse
import json
from importlib.util import find_spec

from newtool.config import load_config


def health() -> dict[str, object]:
    config = load_config()

    return {
        "status": "ok",
        "python_package": "newtool",
        "config_loaded": bool(config),
        "optional_modules": {
            "chromadb": find_spec("chromadb") is not None,
            "torch": find_spec("torch") is not None,
        },
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="newtool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    health_parser = subparsers.add_parser("health", help="Run a local health check.")
    health_parser.add_argument("--json", action="store_true", dest="json_mode")

    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.command == "health":
        result = health()
        if args.json_mode:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print("newtool: OK")
            print(f"config_loaded: {result['config_loaded']}")
            for name, available in result["optional_modules"].items():
                print(f"{name}: {'available' if available else 'not installed'}")


if __name__ == "__main__":
    main()
