import pytest


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_wms_containers(client):
    response = client.get("/graphql/?query={ containers { code type { code } } }")
    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "containers": [
                {"code": "empl 1", "type": {"code": "LOCATION"}},
                {"code": "warehouse", "type": {"code": "LOCATION"}},
            ]
        }
    }
