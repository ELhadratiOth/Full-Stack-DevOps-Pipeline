"""Database models using SQLModel"""
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class UserBase(SQLModel):
    """User base model"""
    name: str = Field(index=True)
    email: str = Field(unique=True, index=True)
    active: bool = Field(default=True)


class User(UserBase, table=True):
    """User database model"""
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(SQLModel):
    """User creation schema"""
    name: str
    email: str


class UserRead(UserBase):
    """User read schema"""
    id: int
    created_at: datetime
    updated_at: datetime


class ProductBase(SQLModel):
    """Product base model"""
    name: str = Field(index=True)
    description: str
    price: float = Field(gt=0)
    in_stock: bool = Field(default=True)


class Product(ProductBase, table=True):
    """Product database model"""
    __tablename__ = "products"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ProductCreate(SQLModel):
    """Product creation schema"""
    name: str
    description: str
    price: float


class ProductRead(ProductBase):
    """Product read schema"""
    id: int
    created_at: datetime
    updated_at: datetime
