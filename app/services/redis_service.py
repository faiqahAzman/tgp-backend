import asyncio
from typing import Dict, Any

class RedisService:
    def __init__(self):
        pass

    async def get_data(self, indicator: str) -> Dict[str, Any]:
        """Simulate getting data from Redis"""
        await asyncio.sleep(0.1)  # Simulate network latency

        dummy_data = {
            "financial_inclusion": {
                "source": "financial-service",
                "value": 85.3,
                "risk_level": "low",
                "timestamp": "2024-02-22T15:38:50",
                "metadata": {
                    "region": "Malaysia",
                    "service_version": "1.0.0",
                    "data_source": "internal-metrics"
                }
            },
            "digital_payments": {
                "source": "payments-service",
                "value": 62.1,
                "risk_level": "medium",
                "timestamp": "2024-02-22T15:38:50",
                "metadata": {
                    "region": "Malaysia",
                    "service_version": "1.1.0",
                    "data_source": "transaction-logs"
                }
            },
            "money_laundering": {
                "source": "aml-service",
                "value": 7.5,
                "risk_level": "medium",
                "timestamp": "2024-02-22T15:38:50",
                "metadata": {
                    "region": "Malaysia",
                    "service_version": "0.9.0",
                    "data_source": "regulatory-reports"
                }
            },
            "unemployment": {
                "source": "economic-service",
                "value": 4.2,
                "risk_level": "low",
                "timestamp": "2024-02-22T15:38:50",
                "metadata": {
                    "region": "Malaysia",
                    "service_version": "1.2.0",
                    "data_source": "labor-statistics"
                }
            },
            "gdp_growth": {
                "source": "gdp-service",
                "value": 3.8,
                "risk_level": "low",
                "timestamp": "2024-02-22T15:38:50",
                "metadata": {
                    "region": "Malaysia",
                    "service_version": "1.0.1",
                    "data_source": "economic-forecasts"
                }
            }
        }

        return dummy_data.get(indicator)

redis_service = RedisService()
