import pytest
import respx


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.fixture
def containers_data():
    return '[{"id": 2, "code": "empl 1", "type": {"id": 3}, "type_id": 3, "properties": null, "properties_id": null}, {"id": 1, "code": "warehouse", "type": {"id": 3}, "type_id": 3, "properties": null, "properties_id": null}]'


@pytest.fixture
def container_type_data():
    return '{"id": 3, "code": "LOCATION", "label": null, "behaviours": {"container": true}, "properties": null, "parent": null, "parent_id": null}'


@respx.mock
def test_wms_containers_only(client, containers_data):
    respx.get("http://localhost:3000/api/wms/containers", content=containers_data)
    response = client.get("/graphql/?query={ containers { code } }")
    assert response.status_code == 200
    assert response.json() == {
        "data": {"containers": [{"code": "empl 1"}, {"code": "warehouse"}]}
    }


@respx.mock
def test_wms_containers(client, containers_data, container_type_data):
    respx.get("http://localhost:3000/api/wms/containers", content=containers_data)
    respx.get(
        "http://localhost:3000/api/wms/container/type/3", content=container_type_data
    )
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
