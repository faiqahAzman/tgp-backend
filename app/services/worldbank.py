import httpx
from app.core.constants import RiskIndicator

class WorldBankService:
    def __init__(self):
        self.base_url = "https://api.worldbank.org/v2"
        self.country_code = "MYS"  # Malaysia

    async def get_raw_indicator_data(self, indicator: RiskIndicator, year: int = 2021) -> dict:
        """Fetch raw indicator data from World Bank API"""
        async with httpx.AsyncClient() as client:
            url = f"{self.base_url}/country/{self.country_code}/indicator/{indicator}?date={year}&format=json"
            response = await client.get(url)
            response.raise_for_status()
            return response.json()

    

worldbank_service = WorldBankService()
