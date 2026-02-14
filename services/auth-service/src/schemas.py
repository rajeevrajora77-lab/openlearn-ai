"""Pydantic schemas for request/response validation"""

from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime, date
import uuid

class UserCreate(BaseModel):
    """Schema for user registration"""
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str = Field(..., min_length=2, max_length=200)
    date_of_birth: date
    phone: Optional[str] = None
    
    @validator('password')
    def validate_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        return v

class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str

class Token(BaseModel):
    """Schema for JWT token response"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int  # seconds

class TokenData(BaseModel):
    """Schema for decoded token data"""
    user_id: uuid.UUID
    email: str
    role: str

class UserResponse(BaseModel):
    """Schema for user response"""
    id: uuid.UUID
    email: str
    full_name: str
    role: str
    subscription_tier: str
    is_email_verified: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
