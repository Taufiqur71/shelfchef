from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from datetime import datetime
from recipe_generator import SmartRecipeGenerator, Recipe

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Initialize the smart recipe generator
recipe_generator = SmartRecipeGenerator()

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Define Models
class RecipeGenerationRequest(BaseModel):
    ingredients: str

class RecipeGenerationResponse(BaseModel):
    recipes: List[Recipe]

class SavedRecipe(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    cook_time: str
    servings: str
    difficulty: str
    available_ingredients: List[str]
    missing_ingredients: List[str]
    instructions: List[str]
    match_percentage: int
    saved_at: datetime = Field(default_factory=datetime.utcnow)

class SavedRecipeCreate(BaseModel):
    name: str
    description: str
    cook_time: str
    servings: str
    difficulty: str
    available_ingredients: List[str]
    missing_ingredients: List[str]
    instructions: List[str]
    match_percentage: int

# API Routes
@api_router.get("/")
async def root():
    return {"message": "ShelfChef API - Ready to cook!"}

@api_router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ShelfChef API", "generator": "Smart Recipe Generator"}

@api_router.post("/generate-recipes", response_model=RecipeGenerationResponse)
async def generate_recipes(request: RecipeGenerationRequest):
    """Generate recipes based on user ingredients using smart algorithm"""
    
    if not request.ingredients.strip():
        raise HTTPException(status_code=400, detail="Please provide ingredients")
    
    try:
        # Generate recipes using smart algorithm
        recipes = recipe_generator.generate_recipes(request.ingredients, max_recipes=3)
        
        if not recipes:
            raise HTTPException(status_code=404, detail="No recipes found for the given ingredients")
        
        return RecipeGenerationResponse(recipes=recipes)
        
    except Exception as e:
        logging.error(f"Error in generate_recipes: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate recipes")

@api_router.post("/save-recipe", response_model=SavedRecipe)
async def save_recipe(recipe_data: SavedRecipeCreate):
    """Save a recipe to the database"""
    
    saved_recipe = SavedRecipe(**recipe_data.dict())
    
    try:
        # Insert into MongoDB
        await db.saved_recipes.insert_one(saved_recipe.dict())
        return saved_recipe
        
    except Exception as e:
        logging.error(f"Error saving recipe: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to save recipe")

@api_router.get("/saved-recipes", response_model=List[SavedRecipe])
async def get_saved_recipes():
    """Get all saved recipes"""
    
    try:
        saved_recipes = await db.saved_recipes.find().to_list(1000)
        return [SavedRecipe(**recipe) for recipe in saved_recipes]
        
    except Exception as e:
        logging.error(f"Error retrieving saved recipes: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve saved recipes")

@api_router.delete("/saved-recipes/{recipe_id}")
async def delete_saved_recipe(recipe_id: str):
    """Delete a saved recipe"""
    
    try:
        result = await db.saved_recipes.delete_one({"id": recipe_id})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Recipe not found")
            
        return {"message": "Recipe deleted successfully"}
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error deleting recipe: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete recipe")

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()