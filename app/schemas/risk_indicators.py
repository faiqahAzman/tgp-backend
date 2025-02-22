from typing import Optional, Literal, Any
from pydantic import BaseModel, Field
from datetime import datetime
from app.core.constants import RiskIndicator

class RiskIndicatorResponse(BaseModel):
    status: str = "success"
    data: dict[str, Any] = Field(..., description="Risk indicator data")
    country: str = "Malaysia"
    indicator: str = Field(..., description="Risk indicator name")
    indicator_code: RiskIndicator
    description: str = Field(..., description="Detailed description of the indicator")
    value: Optional[float] = Field(None, description="Indicator value")
    year: int = Field(..., description="Year of the data")
    risk_level: Literal["low", "medium", "high", "unknown"] = Field(..., description="Calculated risk level")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "data": {
                    "country": "Malaysia",
                    "indicator": "Financial Inclusion",
                    "indicator_code": "FX.OWN.TOTL.ZS",
                    "description": "Financial Inclusion & Access to Banking [Fraud Risk Indicator]",
                    "value": 85.3,
                    "year": 2021,
                    "risk_level": "low"
                },
                "timestamp": "2024-02-22T14:17:00Z"
            }
        }

class ErrorResponse(BaseModel):
    status: str = "error"
    message: str = Field(..., description="Error message")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
