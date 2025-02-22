from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.endpoints import risk_indicators, risk_metrics

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    risk_indicators.router,
    prefix=f"{settings.API_V1_STR}/risk-indicators",
    tags=["risk-indicators"]
)

app.include_router(
    risk_metrics.router,
    prefix=f"{settings.API_V1_STR}/risk-metrics",
    tags=["risk-metrics"]
)

# @app.on_event("shutdown")
# async def shutdown_event():
#     """Clean up resources on shutdown"""
#     from app.services.kafka_producer import kafka_service
#     kafka_service.close()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "TGP Backend API",
        "docs_url": "/docs",
        "openapi_url": f"{settings.API_V1_STR}/openapi.json"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
