from fastapi import APIRouter, HTTPException
from app.core.constants import RiskIndicator
from app.services.worldbank import worldbank_service

router = APIRouter()

@router.get("/financial-inclusion")
async def get_financial_inclusion_enhanced(year: int = 2021):
    """
    Get Financial Inclusion data with risk metrics
    Includes risk level assessment and recommendations
    """
    try:
        data = await worldbank_service.get_enhanced_data(RiskIndicator.FINANCIAL_INCLUSION, year)
        return {
            "indicator": "Financial Inclusion",
            **data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching enhanced financial inclusion data: {str(e)}"
        )

@router.get("/digital-payments")
async def get_digital_payments_enhanced(year: int = 2021):
    """
    Get Digital Payments data with risk metrics
    Includes risk level assessment and recommendations
    """
    try:
        data = await worldbank_service.get_enhanced_data(RiskIndicator.DIGITAL_PAYMENTS, year)
        return {
            "indicator": "Digital Payments",
            **data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching enhanced digital payments data: {str(e)}"
        )

@router.get("/money-laundering")
async def get_money_laundering_enhanced(year: int = 2021):
    """
    Get Money Laundering Risk data with risk metrics
    Includes risk level assessment and recommendations
    """
    try:
        data = await worldbank_service.get_enhanced_data(RiskIndicator.MONEY_LAUNDERING, year)
        return {
            "indicator": "Money Laundering Risk",
            **data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching enhanced money laundering risk data: {str(e)}"
        )

@router.get("/unemployment")
async def get_unemployment_enhanced(year: int = 2021):
    """
    Get Unemployment Rate data with risk metrics
    Includes risk level assessment and recommendations
    """
    try:
        data = await worldbank_service.get_enhanced_data(RiskIndicator.UNEMPLOYMENT, year)
        return {
            "indicator": "Unemployment Rate",
            **data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching enhanced unemployment rate data: {str(e)}"
        )

@router.get("/gdp-growth")
async def get_gdp_growth_enhanced(year: int = 2021):
    """
    Get GDP Growth data with risk metrics
    Includes risk level assessment and recommendations
    """
    try:
        data = await worldbank_service.get_enhanced_data(RiskIndicator.GDP_GROWTH, year)
        return {
            "indicator": "GDP Growth",
            **data
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching enhanced GDP growth data: {str(e)}"
        )
