"""Test product endpoints"""
from app.models.models import Product


def test_list_products(session, client):
    """Test list all products"""
    # Create test data
    product = Product(
        id=1,
        name="Test Product",
        description="A test product",
        price=99.99,
        in_stock=True
    )
    session.add(product)
    session.commit()
    
    response = client.get("/api/v1/products/")
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0

def test_get_product(session, client):
    """Test get a specific product"""
    # Create test data
    product = Product(
        id=1,
        name="Test Product",
        description="A test product",
        price=99.99,
        in_stock=True
    )
    session.add(product)
    session.commit()
    
    response = client.get("/api/v1/products/1")
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1
    assert "name" in product
    assert "price" in product

def test_create_product(client):
    """Test create a new product"""
    new_product = {
        "name": "Test Product",
        "description": "A test product",
        "price": 99.99
    }
    response = client.post("/api/v1/products/", json=new_product)
    assert response.status_code == 201
    created_product = response.json()
    assert created_product["name"] == "Test Product"
    assert created_product["price"] == 99.99

def test_update_product(session, client):
    """Test update a product"""
    # Create test data
    product = Product(
        id=1,
        name="Original Product",
        description="Original description",
        price=99.99,
        in_stock=True
    )
    session.add(product)
    session.commit()
    
    updated_data = {
        "name": "Updated Product",
        "description": "Updated description",
        "price": 149.99
    }
    response = client.put("/api/v1/products/1", json=updated_data)
    assert response.status_code == 200
    updated_product = response.json()
    assert updated_product["name"] == "Updated Product"

def test_delete_product(session, client):
    """Test delete a product"""
    # Create test data
    product = Product(
        id=1,
        name="Product to Delete",
        description="This product will be deleted",
        price=49.99,
        in_stock=True
    )
    session.add(product)
    session.commit()
    
    response = client.delete("/api/v1/products/1")
    assert response.status_code == 204


def test_get_product_not_found(client):
    """Test get product that doesn't exist"""
    response = client.get("/api/v1/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_update_product_not_found(client):
    """Test update product that doesn't exist"""
    updated_data = {
        "name": "Updated Product",
        "description": "Updated description",
        "price": 149.99
    }
    response = client.put("/api/v1/products/999", json=updated_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_delete_product_not_found(client):
    """Test delete product that doesn't exist"""
    response = client.delete("/api/v1/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"
