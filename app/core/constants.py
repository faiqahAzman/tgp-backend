from enum import Enum

class RiskIndicator(str, Enum):
    FINANCIAL_INCLUSION = "FX.OWN.TOTL.ZS"
    DIGITAL_PAYMENTS = "IT.DP.PAY.GOOD.ZS"
    MONEY_LAUNDERING = "BX.TRF.PWKR.DT.GD.ZS"
    UNEMPLOYMENT = "SL.UEM.TOTL.ZS"
    GDP_GROWTH = "NY.GDP.MKTP.KD.ZG"

INDICATOR_DESCRIPTIONS = {
    RiskIndicator.FINANCIAL_INCLUSION: "Financial Inclusion & Access to Banking [Fraud Risk Indicator]",
    RiskIndicator.DIGITAL_PAYMENTS: "Digital Payments Usage [Fraud Risk in Online Transactions]",
    RiskIndicator.MONEY_LAUNDERING: "Money Laundering Risk [Personal Remittances % of GDP]",
    RiskIndicator.UNEMPLOYMENT: "Unemployment Rate [Fraud Risk Due to Economic Pressure]",
    RiskIndicator.GDP_GROWTH: "GDP Growth [Fraud Risk During Economic Downturns]"
}

# Risk level thresholds (these are example values, adjust based on your requirements)
RISK_THRESHOLDS = {
    RiskIndicator.FINANCIAL_INCLUSION: {"low": 70, "medium": 50, "high": 0},
    RiskIndicator.DIGITAL_PAYMENTS: {"low": 60, "medium": 40, "high": 0},
    RiskIndicator.MONEY_LAUNDERING: {"low": 5, "medium": 10, "high": 15},
    RiskIndicator.UNEMPLOYMENT: {"low": 5, "medium": 10, "high": 15},
    RiskIndicator.GDP_GROWTH: {"low": 3, "medium": 1, "high": -1}
}

# Kafka topics
def get_kafka_topic(indicator: RiskIndicator) -> str:
    return f"risk-indicators.{indicator.lower()}"
