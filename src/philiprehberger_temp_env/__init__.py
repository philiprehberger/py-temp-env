from __future__ import annotations

import functools
import os
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Iterator

__all__ = ["temp_env", "env_override", "TempEnv"]

_UNSET = object()


class TempEnv:
    """Temporarily set, override, or remove environment variables."""

    def __init__(self, **kwargs: str | None) -> None:
        self._overrides: dict[str, str | None] = kwargs
        self._originals: dict[str, str | object] = {}

    @classmethod
    def from_file(cls, path: str | Path) -> TempEnv:
        """Parse a .env file and return a TempEnv instance.

        Lines starting with ``#`` or blank lines are ignored.
        Each line should be ``KEY=VALUE`` (optional quoting on value).
        """
        overrides: dict[str, str | None] = {}
        with open(path) as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip("\"'")
                overrides[key] = value
        return cls(**overrides)

    def __enter__(self) -> TempEnv:
        for key, value in self._overrides.items():
            self._originals[key] = os.environ.get(key, _UNSET)
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        return self

    def __exit__(self, *_: Any) -> None:
        for key, original in self._originals.items():
            if original is _UNSET:
                os.environ.pop(key, None)
            else:
                os.environ[key] = original  # type: ignore[assignment]
        self._originals.clear()


@contextmanager
def temp_env(**kwargs: str | None) -> Iterator[TempEnv]:
    """Context manager to temporarily set, override, or remove env vars.

    Pass ``None`` as the value to remove a variable for the duration.

    Example::

        with temp_env(API_KEY="test-key", DEBUG="1"):
            ...
    """
    ctx = TempEnv(**kwargs)
    with ctx:
        yield ctx


def env_override(**kwargs: str | None) -> Callable[..., Any]:
    """Decorator that wraps a function with temporary env var overrides.

    Useful for test functions::

        @env_override(DATABASE_URL="sqlite:///:memory:")
        def test_database():
            ...
    """

    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(fn)
        def wrapper(*args: Any, **kw: Any) -> Any:
            with TempEnv(**kwargs):
                return fn(*args, **kw)

        return wrapper

    return decorator
