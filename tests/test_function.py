"""Test spin_cli_py functions."""

from spin_cli_py import app


def test_app():
    """Test app.main function."""
    assert app.main("ah ", 3) == "ah ah ah "
