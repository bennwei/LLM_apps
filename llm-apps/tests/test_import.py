"""Test LLM_apps."""

import llm_apps


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(llm_apps.__name__, str)
