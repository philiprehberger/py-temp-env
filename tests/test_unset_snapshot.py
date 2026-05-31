"""Tests for temp_unset, snapshot_env, and restore_env."""

from __future__ import annotations

import os

import pytest

from philiprehberger_temp_env import restore_env, snapshot_env, temp_unset


def test_temp_unset_removes_and_restores(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PATH", "/x")
    with temp_unset("PATH"):
        assert "PATH" not in os.environ
    assert os.environ["PATH"] == "/x"


def test_temp_unset_unset_variable_is_noop(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("NEVER_SET_XYZ", raising=False)
    with temp_unset("NEVER_SET_XYZ"):
        assert "NEVER_SET_XYZ" not in os.environ
    assert "NEVER_SET_XYZ" not in os.environ


def test_temp_unset_multiple_names(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("A_VAR", "a")
    monkeypatch.setenv("B_VAR", "b")
    with temp_unset("A_VAR", "B_VAR"):
        assert "A_VAR" not in os.environ
        assert "B_VAR" not in os.environ
    assert os.environ["A_VAR"] == "a"
    assert os.environ["B_VAR"] == "b"


def test_snapshot_env_captures_set_and_unset(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("X_VAR", "1")
    monkeypatch.delenv("Y_VAR", raising=False)
    snap = snapshot_env("X_VAR", "Y_VAR")
    assert snap == {"X_VAR": "1", "Y_VAR": None}


def test_restore_env_sets_and_unsets(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("X_VAR", raising=False)
    monkeypatch.setenv("Y_VAR", "old")
    restore_env({"X_VAR": "1", "Y_VAR": None})
    assert os.environ["X_VAR"] == "1"
    assert "Y_VAR" not in os.environ


def test_snapshot_restore_round_trip(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ROUND_A", "original_a")
    monkeypatch.delenv("ROUND_B", raising=False)
    snap = snapshot_env("ROUND_A", "ROUND_B")

    os.environ["ROUND_A"] = "mutated"
    os.environ["ROUND_B"] = "added"

    restore_env(snap)
    assert os.environ["ROUND_A"] == "original_a"
    assert "ROUND_B" not in os.environ
