# tests/test_main.py
import pytest
import httpx
import os

@pytest.mark.asyncio
async def test_root_endpoint():
    """Tests the root endpoint (/)."""
    fastapi_url = os.environ.get("FASTAPI_URL", "http://localhost:8000") #default local
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(fastapi_url) # changed from fastapi_url + "/"
            assert response.status_code == 200
            assert response.json() == {"message": "Hello World"}
    except httpx.ConnectError as e:
        pytest.fail(f"FastAPI service not reachable at {fastapi_url}.  Error: {e}")

@pytest.mark.asyncio
async def test_health_check_endpoint():
    """Tests the health check endpoint (/health)."""
    fastapi_url = os.environ.get("FASTAPI_URL", "http://localhost:8000") #default local
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{fastapi_url}/health") # explicitly add the /health path
            assert response.status_code == 200
            assert response.json() == {"status": "ok"}
    except httpx.ConnectError as e:
        pytest.fail(f"FastAPI service not reachable at {fastapi_url}.  Error: {e}")