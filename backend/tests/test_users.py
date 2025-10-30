"""Test user endpoints"""
from app.models.models import User

def test_list_users(client, session):
    """Test list all users"""
    # Create test users
    user1 = User(name="Test User 1", email="test1@example.com")
    user2 = User(name="Test User 2", email="test2@example.com")
    session.add(user1)
    session.add(user2)
    session.commit()
    
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 2

def test_get_user(client, session):
    """Test get a specific user"""
    # Create test user
    user = User(id=1, name="Test User", email="test@example.com")
    session.add(user)
    session.commit()
    
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["id"] == 1
    assert user_data["name"] == "Test User"
    assert user_data["email"] == "test@example.com"

def test_create_user(client):
    """Test create a new user"""
    new_user = {
        "name": "New Test User",
        "email": "newtest@example.com"
    }
    response = client.post("/api/v1/users/", json=new_user)
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["name"] == "New Test User"
    assert created_user["email"] == "newtest@example.com"
    assert "id" in created_user

def test_update_user(client, session):
    """Test update a user"""
    # Create test user
    user = User(id=1, name="Original Name", email="original@example.com")
    session.add(user)
    session.commit()
    
    updated_data = {
        "name": "Updated User",
        "email": "updated@example.com"
    }
    response = client.put("/api/v1/users/1", json=updated_data)
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["name"] == "Updated User"
    assert updated_user["email"] == "updated@example.com"

def test_delete_user(client, session):
    """Test delete a user"""
    # Create test user
    user = User(id=1, name="To Delete", email="delete@example.com")
    session.add(user)
    session.commit()
    
    response = client.delete("/api/v1/users/1")
    assert response.status_code == 204


def test_get_user_not_found(client):
    """Test get user that doesn't exist"""
    response = client.get("/api/v1/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_create_user_duplicate_email(client, session):
    """Test create user with duplicate email"""
    # Create first user
    user = User(name="Existing User", email="duplicate@example.com")
    session.add(user)
    session.commit()
    
    # Try to create another user with same email
    new_user = {
        "name": "Another User",
        "email": "duplicate@example.com"
    }
    response = client.post("/api/v1/users/", json=new_user)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_update_user_not_found(client):
    """Test update user that doesn't exist"""
    updated_data = {
        "name": "Updated Name",
        "email": "updated@example.com"
    }
    response = client.put("/api/v1/users/999", json=updated_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_delete_user_not_found(client):
    """Test delete user that doesn't exist"""
    response = client.delete("/api/v1/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
