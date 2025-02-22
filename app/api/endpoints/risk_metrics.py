from fastapi import APIRouter, HTTPException
from app.services.redis_service import redis_service

router = APIRouter()

@router.get("/financial-inclusion")
async def get_financial_inclusion():
    """Get Financial Inclusion data from Redis"""
    try:
        data = await redis_service.get_data("financial_inclusion")
        if data:
            return {"indicator": "financial_inclusion", "data": data}
        else:
            raise HTTPException(status_code=404, detail="Financial Inclusion data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/digital-payments")
async def get_digital_payments():
    """Get Digital Payments data from Redis"""
    try:
        data = await redis_service.get_data("digital_payments")
        if data:
            return {"indicator": "digital_payments", "data": data}
        else:
            raise HTTPException(status_code=404, detail="Digital Payments data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/money-laundering")
async def get_money_laundering():
    """Get Money Laundering data from Redis"""
    try:
        data = await redis_service.get_data("money_laundering")
        if data:
            return {"indicator": "money_laundering", "data": data}
        else:
            raise HTTPException(status_code=404, detail="Money Laundering data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/unemployment")
async def get_unemployment():
    """Get Unemployment data from Redis"""
    try:
        data = await redis_service.get_data("unemployment")
        if data:
            return {"indicator": "unemployment", "data": data}
        else:
            raise HTTPException(status_code=404, detail="Unemployment data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/gdp-growth")
async def get_gdp_growth():
    """Get GDP Growth data from Redis"""
    try:
        data = await redis_service.get_data("gdp_growth")
        if data:
            return {"indicator": "gdp_growth", "data": data}
        else:
            raise HTTPException(status_code=404, detail="GDP Growth data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
