import pytest
from app import app

@pytest.fixture()
def client():
    """Return a test client"""
    return app.test_client()


@pytest.fixture()
def runner():
    """Return a runner"""
    return app.test_cli_runner()