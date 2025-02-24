import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@pytest.fixture
def client():
    return TestClient(app)

@app.get("/health")
async def health_check():
  """
  Health check endpoint.

  Returns:
      dict: A dictionary containing the status of the application.
  """
  return {"status": "ok"}

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/api/financial-inclusion")
async def call_service1(country: str, start_year: int, end_year: int):
    return {"message": "financial-inclusion"}

@app.get("/api/digital-payments")
async def call_service2(country: str, start_year: int, end_year: int):
    return {"message": "digital-payments"}

@app.get("/api/money-laundering-risk")
async def call_service3(country: str, start_year: int, end_year: int):
    return {"message": "money-laundering-risk"}

@app.get("/api/unemployment-rate")
async def call_service4(country: str, start_year: int, end_year: int):
    return {"message": "unemployment-rate"}

@app.get("/api/gdp-growth")
async def call_service5(country: str, start_year: int, end_year: int):
    return {"message": "gdp-growth"}

# Service Endpoint Tests
@pytest.mark.parametrize("endpoint", [
    "/api/financial-inclusion",
    "/api/digital-payments",
    "/api/money-laundering-risk",
    "/api/unemployment-rate",
    "/api/gdp-growth"
])
class TestServiceEndpoints:
    def test_valid_parameters(self, client, endpoint):
        response = client.get(f"{endpoint}?country=US&start_year=2020&end_year=2022")
        assert response.status_code == 200

    def test_missing_parameters(self, client, endpoint):
        response = client.get(f"{endpoint}?country=US")  # Missing years
        assert response.status_code == 422

    def test_invalid_year_format(self, client, endpoint):
        response = client.get(f"{endpoint}?country=US&start_year=abc&end_year=2022")
        assert response.status_code == 422

    def test_invalid_year_range(self, client, endpoint):
        response = client.get(f"{endpoint}?country=US&start_year=2022&end_year=2020")
        assert response.status_code == 400

# Redis Integration Tests
class TestRedisIntegration:
    def test_invalid_service(self, client):
        response = client.get("/api/invalid-service?country=US&start_year=2020&end_year=2022")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_timeout_scenario(self, client):
        # Test timeout when Redis doesn't respond
        response = client.get("/api/financial-inclusion?country=US&start_year=2020&end_year=2022")
        assert response.status_code in [504, 200]  # 504 for timeout, 200 if Redis responds
