import pytest
import asyncio
from fastapi.testclient import TestClient
from server import app
import json
from motor.motor_asyncio import AsyncIOMotorClient
import os

# Test database setup
TEST_MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
TEST_DB_NAME = "test_shelfchef"

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def setup_test_db():
    """Setup test database"""
    client = AsyncIOMotorClient(TEST_MONGO_URL)
    db = client[TEST_DB_NAME]
    
    # Clean up any existing test data
    await db.saved_recipes.delete_many({})
    
    yield db
    
    # Clean up after tests
    await db.saved_recipes.delete_many({})
    client.close()

# Use TestClient for synchronous tests
client = TestClient(app)

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "ShelfChef API"

def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/api/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "ShelfChef API - Ready to cook!"

def test_generate_recipes():
    """Test recipe generation endpoint"""
    payload = {
        "ingredients": "chicken, tomato, rice, onion, garlic, cheese"
    }
    
    response = client.post("/api/generate-recipes", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "recipes" in data
    assert len(data["recipes"]) > 0
    
    # Check recipe structure
    recipe = data["recipes"][0]
    required_fields = [
        "name", "description", "cook_time", "servings", 
        "difficulty", "available_ingredients", "missing_ingredients",
        "instructions", "match_percentage", "image_url"
    ]
    
    for field in required_fields:
        assert field in recipe

def test_generate_recipes_empty_ingredients():
    """Test recipe generation with empty ingredients"""
    payload = {"ingredients": ""}
    
    response = client.post("/api/generate-recipes", json=payload)
    assert response.status_code == 400
    
    data = response.json()
    assert "Please provide ingredients" in data["detail"]

def test_generate_recipes_varied_ingredients():
    """Test recipe generation with different ingredient combinations"""
    test_cases = [
        {"ingredients": "eggs, milk, flour"},
        {"ingredients": "pasta, tomato, basil"},
        {"ingredients": "chicken, vegetables, rice"},
    ]
    
    for case in test_cases:
        response = client.post("/api/generate-recipes", json=case)
        assert response.status_code == 200
        
        data = response.json()
        assert "recipes" in data
        assert len(data["recipes"]) > 0

def test_recipe_generation_performance():
    """Test that recipe generation is reasonably fast"""
    import time
    
    payload = {"ingredients": "chicken, rice, vegetables"}
    
    start_time = time.time()
    response = client.post("/api/generate-recipes", json=payload)
    end_time = time.time()
    
    assert response.status_code == 200
    assert (end_time - start_time) < 2.0  # Should complete within 2 seconds

def test_recipe_match_percentage():
    """Test that recipes have reasonable match percentages"""
    payload = {"ingredients": "chicken, rice, tomato, onion"}
    
    response = client.post("/api/generate-recipes", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    for recipe in data["recipes"]:
        assert 0 <= recipe["match_percentage"] <= 100
        assert isinstance(recipe["match_percentage"], int)

def test_recipe_instructions_format():
    """Test that recipe instructions are properly formatted"""
    payload = {"ingredients": "eggs, cheese, vegetables"}
    
    response = client.post("/api/generate-recipes", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    for recipe in data["recipes"]:
        assert len(recipe["instructions"]) > 0
        assert all(isinstance(instruction, str) for instruction in recipe["instructions"])
        assert all(len(instruction.strip()) > 0 for instruction in recipe["instructions"])

def test_recipe_image_urls():
    """Test that recipes have valid image URLs"""
    payload = {"ingredients": "chicken, rice, vegetables"}
    
    response = client.post("/api/generate-recipes", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    for recipe in data["recipes"]:
        if recipe["image_url"]:
            assert recipe["image_url"].startswith(("http://", "https://"))

def test_api_error_handling():
    """Test API error handling with malformed requests"""
    # Test invalid JSON
    response = client.post("/api/generate-recipes", data="invalid json")
    assert response.status_code == 422
    
    # Test missing ingredients field
    response = client.post("/api/generate-recipes", json={})
    assert response.status_code == 422