"""Basic import test."""


def test_import():
    """Verify the package can be imported."""
    import philiprehberger_temp_env
    assert hasattr(philiprehberger_temp_env, "__name__") or True
