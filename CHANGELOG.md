# Changelog

## 0.2.0 (2026-05-30)

- Add `temp_unset()` context manager for explicitly removing env vars
- Add `snapshot_env()` / `restore_env()` pair for explicit save/restore beyond context managers

## 0.1.8 (2026-03-31)

- Standardize README to 3-badge format with emoji Support section
- Update CI checkout action to v5 for Node.js 24 compatibility
- Add GitHub issue templates, dependabot config, and PR template

## 0.1.7

- Standardize README structure and fix compliance issues

## 0.1.6

- Add pytest and mypy tool configuration to pyproject.toml

## 0.1.5

- Add basic import test

## 0.1.4

- Add Development section to README

## 0.1.1

- Re-release for PyPI publishing

## 0.1.0 (2026-03-15)

- Initial release
- `temp_env()` context manager for temporary env var overrides
- `env_override()` decorator for test functions
- `TempEnv` class with `.from_file()` classmethod for .env file support
- Pass `None` to remove a variable temporarily
