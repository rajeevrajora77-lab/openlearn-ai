"""OpenLearn AI - Authentication Service

Production-grade authentication service with:
- JWT token generation and validation
- OAuth integration (Google, Microsoft)
- COPPA compliance (age gating, parental consent)
- Rate limiting
- Session management
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator
import logging
import os

from src.config import settings
from src.api import auth, users, health
from src.database import engine, Base

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="OpenLearn AI - Auth Service",
    description="Authentication and authorization service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prometheus metrics
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

# Create database tables
@app.on_event("startup")
async def startup():
    logger.info("Starting auth-service...")
    # In production, use Alembic migrations instead
    # Base.metadata.create_all(bind=engine)
    logger.info("Auth-service started successfully")

@app.on_event("shutdown")
async def shutdown():
    logger.info("Shutting down auth-service...")

# Include routers
app.include_router(health.router, prefix="", tags=["Health"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])

# Root endpoint
@app.get("/")
async def root():
    return {
        "service": "OpenLearn AI - Auth Service",
        "version": "1.0.0",
        "status": "operational",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
