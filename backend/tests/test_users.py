"""Test user endpoints"""

def test_list_users(client):
    """Test list all users"""
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0

def test_get_user(client):
    """Test get a specific user"""
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "name" in user
    assert "email" in user

def test_create_user(client):
    """Test create a new user"""
    new_user = {
        "name": "Test User",
        "email": "test@example.com"
    }
    response = client.post("/api/v1/users/", json=new_user)
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["name"] == "Test User"
    assert created_user["email"] == "test@example.com"

def test_update_user(client):
    """Test update a user"""
    updated_data = {
        "name": "Updated User",
        "email": "updated@example.com"
    }
    response = client.put("/api/v1/users/1", json=updated_data)
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["name"] == "Updated User"

def test_delete_user(client):
    """Test delete a user"""
    response = client.delete("/api/v1/users/1")
    assert response.status_code == 204
