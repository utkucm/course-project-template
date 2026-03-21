import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")


def get(key: str, default: str | None = None) -> str | None:
    """Return the value of an environment variable, or `default` if unset."""
    return os.getenv(key, default)


def require(key: str) -> str:
    """Return the value of an environment variable, raising if unset."""
    value = os.getenv(key)
    if value is None:
        raise RuntimeError(f"Required environment variable '{key}' is not set")
    return value
