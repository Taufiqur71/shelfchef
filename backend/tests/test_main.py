import pytest
from fastapi.testclient import TestClient
from server import app
import json

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

def test_save_recipe():
    """Test saving a recipe"""
    recipe_data = {
        "name": "Test Recipe",
        "description": "A test recipe",
        "cook_time": "10 mins",
        "servings": "2 servings",
        "difficulty": "Easy",
        "available_ingredients": ["chicken", "rice"],
        "missing_ingredients": ["salt", "pepper"],
        "instructions": ["Cook chicken", "Add rice", "Season to taste"],
        "match_percentage": 75,
        "image_url": "https://example.com/image.jpg"
    }
    
    response = client.post("/api/save-recipe", json=recipe_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["name"] == recipe_data["name"]
    assert "id" in data
    assert "saved_at" in data

def test_get_saved_recipes():
    """Test retrieving saved recipes"""
    response = client.get("/api/saved-recipes")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)

def test_delete_saved_recipe():
    """Test deleting a saved recipe"""
    # First save a recipe
    recipe_data = {
        "name": "Recipe to Delete",
        "description": "A recipe to be deleted",
        "cook_time": "5 mins",
        "servings": "1 serving",
        "difficulty": "Easy",
        "available_ingredients": ["bread"],
        "missing_ingredients": ["butter"],
        "instructions": ["Toast bread"],
        "match_percentage": 50,
        "image_url": ""
    }
    
    save_response = client.post("/api/save-recipe", json=recipe_data)
    assert save_response.status_code == 200
    
    recipe_id = save_response.json()["id"]
    
    # Delete the recipe
    delete_response = client.delete(f"/api/saved-recipes/{recipe_id}")
    assert delete_response.status_code == 200
    
    data = delete_response.json()
    assert data["message"] == "Recipe deleted successfully"

def test_delete_nonexistent_recipe():
    """Test deleting a non-existent recipe"""
    fake_id = "nonexistent_id"
    
    response = client.delete(f"/api/saved-recipes/{fake_id}")
    assert response.status_code == 404
    
    data = response.json()
    assert data["detail"] == "Recipe not found"