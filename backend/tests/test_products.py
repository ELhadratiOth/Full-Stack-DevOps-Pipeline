"""Test product endpoints"""

def test_list_products(client):
    """Test list all products"""
    response = client.get("/api/v1/products/")
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0

def test_get_product(client):
    """Test get a specific product"""
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

def test_update_product(client):
    """Test update a product"""
    updated_data = {
        "name": "Updated Product",
        "description": "Updated description",
        "price": 149.99
    }
    response = client.put("/api/v1/products/1", json=updated_data)
    assert response.status_code == 200
    updated_product = response.json()
    assert updated_product["name"] == "Updated Product"

def test_delete_product(client):
    """Test delete a product"""
    response = client.delete("/api/v1/products/1")
    assert response.status_code == 204
