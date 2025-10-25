"""Test health endpoints"""

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_readiness_check(client):
    """Test readiness check endpoint"""
    response = client.get("/readiness")
    assert response.status_code == 200
    assert response.json()["ready"] is True

def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
