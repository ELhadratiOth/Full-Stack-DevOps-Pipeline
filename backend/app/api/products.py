"""Product endpoints with database integration"""
from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session, select
from app.models.models import Product, ProductCreate, ProductRead
from app.database import get_session
from typing import List

router = APIRouter()


@router.get("/", response_model=List[ProductRead])
def list_products(session: Session = Depends(get_session)):
    """
    Get all products from database
    """
    statement = select(Product)
    products = session.exec(statement).all()
    return products


@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, session: Session = Depends(get_session)):
    """
    Get a specific product by ID from database
    """
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    """
    Create a new product in database
    """
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, product: ProductCreate, session: Session = Depends(get_session)):
    """
    Update a product in database
    """
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, session: Session = Depends(get_session)):
    """
    Delete a product from database
    """
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    session.delete(db_product)
    session.commit()
    return None
