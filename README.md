# philiprehberger-temp-env

[![Tests](https://github.com/philiprehberger/py-temp-env/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-temp-env/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-temp-env.svg)](https://pypi.org/project/philiprehberger-temp-env/)
[![Last updated](https://img.shields.io/github/last-commit/philiprehberger/py-temp-env)](https://github.com/philiprehberger/py-temp-env/commits/main)

Temporarily set, override, or remove environment variables with a context manager.

## Installation

```bash
pip install philiprehberger-temp-env
```

## Usage

### Context manager

```python
from philiprehberger_temp_env import temp_env

with temp_env(API_KEY="test-key", DEBUG="1"):
    # API_KEY and DEBUG are set
    ...
# Original values are restored
```

### Remove a variable temporarily

```python
from philiprehberger_temp_env import temp_env

with temp_env(SECRET=None):
    # SECRET is removed from the environment
    ...
# SECRET is restored
```

### Decorator for tests

```python
from philiprehberger_temp_env import env_override

@env_override(DATABASE_URL="sqlite:///:memory:", DEBUG="0")
def test_database():
    ...
```

### Load from .env file

```python
from philiprehberger_temp_env import TempEnv

ctx = TempEnv.from_file(".env")
with ctx:
    ...
```

### TempEnv class directly

```python
from philiprehberger_temp_env import TempEnv

with TempEnv(API_KEY="test", VERBOSE="1"):
    ...
```

## API

| Name | Description |
|---|---|
| `temp_env(**kwargs: str \| None)` | Context manager that temporarily sets, overrides, or removes env vars. Pass `None` to remove a variable. |
| `env_override(**kwargs: str \| None)` | Decorator that wraps a function with temporary env var overrides. |
| `TempEnv(**kwargs: str \| None)` | Class that can be used as a context manager directly. |
| `TempEnv.from_file(path)` | Classmethod that parses a `.env` file and returns a `TempEnv` instance. |

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## Support

If you find this project useful:

⭐ [Star the repo](https://github.com/philiprehberger/py-temp-env)

🐛 [Report issues](https://github.com/philiprehberger/py-temp-env/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

💡 [Suggest features](https://github.com/philiprehberger/py-temp-env/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

❤️ [Sponsor development](https://github.com/sponsors/philiprehberger)

🌐 [All Open Source Projects](https://philiprehberger.com/open-source-packages)

💻 [GitHub Profile](https://github.com/philiprehberger)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/philiprehberger)

## License

[MIT](LICENSE)
