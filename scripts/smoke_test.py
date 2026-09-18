import os
import sys

import httpx

BASE_URL = os.getenv("SMOKE_BASE_URL", "http://localhost:8000")


def check(path: str) -> None:
    response = httpx.get(f"{BASE_URL}{path}", timeout=10)
    response.raise_for_status()
    print(f"PASS {path} -> {response.status_code}")


def main() -> int:
    for path in ("/health", "/health/db", "/health/providers", "/ready", "/release"):
        check(path)

    print("Smoke test completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
