
import pytest
import httpx
from  app.main import app

@pytest.mark.asyncio
async def test_get_items():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport = transport, base_url = "http://test") as ac:
        response = await ac.get("/items/?limit=5")
        assert response.status_code == 200
        assert response.json() == {"items": [1,2,3,4,5]}


