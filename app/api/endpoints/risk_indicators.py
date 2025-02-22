from fastapi import APIRouter, HTTPException
from app.core.constants import RiskIndicator
from app.services.worldbank import worldbank_service

router = APIRouter()

@router.get("/financial-inclusion/raw")
async def get_financial_inclusion_raw(year: int = 2021):
    """
    Get raw Financial Inclusion data from World Bank API
    Indicator: FX.OWN.TOTL.ZS - Financial Inclusion & Access to Banking
    """
    try:
        data = await worldbank_service.get_raw_indicator_data(RiskIndicator.FINANCIAL_INCLUSION, year)
        return {
            "indicator": "Financial Inclusion",
            "raw_data": data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching financial inclusion data: {str(e)}"
        )

@router.get("/digital-payments/raw")
async def get_digital_payments_raw(year: int = 2021):
    """
    Get raw Digital Payments data from World Bank API
    Indicator: IT.DP.PAY.GOOD.ZS - Digital Payments Usage
    """
    try:
        data = await worldbank_service.get_raw_indicator_data(RiskIndicator.DIGITAL_PAYMENTS, year)
        return {
            "indicator": "Digital Payments",
            "raw_data": data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching digital payments data: {str(e)}"
        )

@router.get("/money-laundering/raw")
async def get_money_laundering_raw(year: int = 2021):
    """
    Get raw Money Laundering Risk data from World Bank API
    Indicator: BX.TRF.PWKR.DT.GD.ZS - Personal Remittances % of GDP
    """
    try:
        data = await worldbank_service.get_raw_indicator_data(RiskIndicator.MONEY_LAUNDERING, year)
        return {
            "indicator": "Money Laundering Risk",
            "raw_data": data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching money laundering risk data: {str(e)}"
        )

@router.get("/unemployment/raw")
async def get_unemployment_raw(year: int = 2021):
    """
    Get raw Unemployment Rate data from World Bank API
    Indicator: SL.UEM.TOTL.ZS - Unemployment Rate
    """
    try:
        data = await worldbank_service.get_raw_indicator_data(RiskIndicator.UNEMPLOYMENT, year)
        return {
            "indicator": "Unemployment Rate",
            "raw_data": data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching unemployment rate data: {str(e)}"
        )

@router.get("/gdp-growth/raw")
async def get_gdp_growth_raw(year: int = 2021):
    """
    Get raw GDP Growth data from World Bank API
    Indicator: NY.GDP.MKTP.KD.ZG - GDP Growth Rate
    """
    try:
        data = await worldbank_service.get_raw_indicator_data(RiskIndicator.GDP_GROWTH, year)
        return {
            "indicator": "GDP Growth",
            "raw_data": data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching GDP growth data: {str(e)}"
        )

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "OK"}
