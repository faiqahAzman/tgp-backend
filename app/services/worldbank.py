import httpx
from typing import Optional, Dict, Any
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

    async def get_enhanced_data(self, indicator: RiskIndicator, year: int = 2021) -> Dict[str, Any]:
        """Get data with risk metrics"""
        raw_data = await self.get_raw_indicator_data(indicator, year)
        risk_metrics = self.calculate_risk_metrics(raw_data, indicator)
        
        return {
            "raw_data": raw_data,
            "risk_metrics": risk_metrics
        }

    def calculate_risk_metrics(self, raw_data: dict, indicator: RiskIndicator) -> Dict[str, Any]:
        """Calculate risk metrics from raw World Bank data"""
        # Extract value from World Bank response
        value = raw_data[1][0].get("value") if raw_data[1] and len(raw_data[1]) > 0 else None
        
        if value is None:
            return {
                "value": None,
                "risk_level": "unknown",
                "analysis": "No data available for risk assessment",
                "recommendations": ["Gather more data for accurate risk assessment"]
            }

        # Calculate risk level based on indicator-specific thresholds
        risk_level = self._get_risk_level(value, indicator)
        analysis = self._get_risk_analysis(value, risk_level, indicator)
        recommendations = self._get_recommendations(risk_level, indicator)

        return {
            "value": value,
            "risk_level": risk_level,
            "analysis": analysis,
            "recommendations": recommendations
        }

    def _get_risk_level(self, value: float, indicator: RiskIndicator) -> str:
        """Determine risk level based on indicator-specific thresholds"""
        if indicator == RiskIndicator.FINANCIAL_INCLUSION:
            # Higher financial inclusion = lower risk
            if value >= 70: return "low"
            if value >= 50: return "medium"
            return "high"
            
        elif indicator == RiskIndicator.DIGITAL_PAYMENTS:
            # Higher digital payments usage = lower risk
            if value >= 60: return "low"
            if value >= 40: return "medium"
            return "high"
            
        elif indicator == RiskIndicator.MONEY_LAUNDERING:
            # Higher remittances % = higher risk
            if value <= 5: return "low"
            if value <= 10: return "medium"
            return "high"
            
        elif indicator == RiskIndicator.UNEMPLOYMENT:
            # Higher unemployment = higher risk
            if value <= 5: return "low"
            if value <= 10: return "medium"
            return "high"
            
        elif indicator == RiskIndicator.GDP_GROWTH:
            # Higher GDP growth = lower risk
            if value >= 3: return "low"
            if value >= 1: return "medium"
            return "high"

    def _get_risk_analysis(self, value: float, risk_level: str, indicator: RiskIndicator) -> str:
        """Generate risk analysis based on indicator and risk level"""
        if indicator == RiskIndicator.FINANCIAL_INCLUSION:
            return f"Financial inclusion rate of {value}% indicates {risk_level} fraud risk. {'Higher' if risk_level == 'high' else 'Lower'} risk due to {'limited' if risk_level == 'high' else 'widespread'} access to banking services."
            
        elif indicator == RiskIndicator.DIGITAL_PAYMENTS:
            return f"Digital payments adoption rate of {value}% suggests {risk_level} fraud risk in online transactions. {'Higher' if risk_level == 'high' else 'Lower'} risk due to {'limited' if risk_level == 'high' else 'widespread'} digital payment usage."
            
        elif indicator == RiskIndicator.MONEY_LAUNDERING:
            return f"Personal remittances at {value}% of GDP indicates {risk_level} money laundering risk. {'Higher' if risk_level == 'high' else 'Lower'} risk due to {'high' if risk_level == 'high' else 'moderate to low'} remittance volumes."
            
        elif indicator == RiskIndicator.UNEMPLOYMENT:
            return f"Unemployment rate of {value}% suggests {risk_level} fraud risk due to economic pressure. {'Higher' if risk_level == 'high' else 'Lower'} risk due to {'high' if risk_level == 'high' else 'moderate to low'} unemployment levels."
            
        elif indicator == RiskIndicator.GDP_GROWTH:
            return f"GDP growth rate of {value}% indicates {risk_level} fraud risk during economic {'downturn' if value < 0 else 'growth'}. {'Higher' if risk_level == 'high' else 'Lower'} risk due to {'weak' if risk_level == 'high' else 'strong'} economic conditions."

    def _get_recommendations(self, risk_level: str, indicator: RiskIndicator) -> list[str]:
        """Generate recommendations based on risk level and indicator"""
        base_recommendations = {
            "low": [
                "Maintain current risk controls",
                "Monitor for changes in risk patterns",
                "Regular review of security measures"
            ],
            "medium": [
                "Enhance monitoring frequency",
                "Review and update risk controls",
                "Consider additional verification steps"
            ],
            "high": [
                "Implement stricter verification measures",
                "Increase manual review frequency",
                "Deploy additional fraud detection tools"
            ]
        }

        indicator_specific = {
            RiskIndicator.FINANCIAL_INCLUSION: {
                "high": ["Focus on basic financial education", "Implement simplified due diligence"],
                "medium": ["Enhance digital banking security", "Promote financial literacy"],
                "low": ["Optimize digital service delivery", "Maintain strong KYC processes"]
            },
            RiskIndicator.DIGITAL_PAYMENTS: {
                "high": ["Strengthen transaction monitoring", "Implement additional authentication layers"],
                "medium": ["Enhance fraud detection systems", "Review transaction limits"],
                "low": ["Optimize payment flows", "Monitor for emerging threats"]
            }
        }

        recommendations = base_recommendations[risk_level]
        if indicator in indicator_specific and risk_level in indicator_specific[indicator]:
            recommendations.extend(indicator_specific[indicator][risk_level])
        
        return recommendations

worldbank_service = WorldBankService()
