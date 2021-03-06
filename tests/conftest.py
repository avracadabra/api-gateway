import pytest
from starlette.testclient import TestClient

from avracadabra.api.app import create_app


@pytest.fixture(name="client", scope="session")
def fixture_test_client():
    with TestClient(create_app()) as client:
        yield client
