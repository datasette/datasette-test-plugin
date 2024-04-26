from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_permissions():
    ds = Datasette()
    ds._special_test_permissions = {"view-instance": {"id": "root"}}
    response = await ds.client.get("/")
    assert response.status_code == 403
    response = await ds.client.get(
        "/", cookies={"ds_actor": ds.sign({"a": {"id": "root"}}, "actor")}
    )
    assert response.status_code == 200
