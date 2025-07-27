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
from emergentintegrations.llm.chat import LlmChat, UserMessage
import json
import asyncio

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# OpenAI API key
openai_api_key = os.environ.get('OPENAI_API_KEY')

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Define Models
class Recipe(BaseModel):
    name: str
    description: str
    cook_time: str
    servings: str
    difficulty: str
    available_ingredients: List[str]
    missing_ingredients: List[str]
    instructions: List[str]
    match_percentage: int

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

# LLM Integration Functions
async def generate_recipes_with_llm(ingredients: str) -> List[Recipe]:
    """Generate recipes using OpenAI LLM through emergentintegrations"""
    
    # Create a new chat instance for this request
    chat = LlmChat(
        api_key=openai_api_key,
        session_id=f"recipe_generation_{uuid.uuid4()}",
        system_message="""You are a professional chef and recipe assistant. Your task is to generate realistic, delicious recipes based on the ingredients provided by the user.

Rules:
1. Generate exactly 2-3 recipes
2. Each recipe should use most of the provided ingredients
3. Be creative but practical
4. Include estimated cook time, servings, and difficulty level
5. List ingredients the user has vs. ingredients they might need to buy
6. Provide clear, step-by-step instructions
7. Make recipes sound appealing and achievable

Return your response as a JSON array with this exact structure:
[
  {
    "name": "Recipe Name",
    "description": "Brief appetizing description",
    "cook_time": "X mins",
    "servings": "X servings",
    "difficulty": "Easy/Medium/Hard",
    "available_ingredients": ["ingredient1", "ingredient2"],
    "missing_ingredients": ["ingredient3", "ingredient4"],
    "instructions": ["Step 1", "Step 2", "Step 3"],
    "match_percentage": 80
  }
]

The match_percentage should be calculated as: (available_ingredients / total_ingredients_needed) * 100"""
    ).with_model("openai", "gpt-4o")
    
    # Create user message
    user_message = UserMessage(
        text=f"Generate 2-3 realistic recipes using these ingredients: {ingredients}. Make sure to follow the JSON format exactly."
    )
    
    try:
        # Send message to LLM
        response = await chat.send_message(user_message)
        
        # Parse the JSON response
        recipes_data = json.loads(response)
        
        # Convert to Recipe objects
        recipes = []
        for recipe_data in recipes_data:
            recipe = Recipe(
                name=recipe_data['name'],
                description=recipe_data['description'],
                cook_time=recipe_data['cook_time'],
                servings=recipe_data['servings'],
                difficulty=recipe_data['difficulty'],
                available_ingredients=recipe_data['available_ingredients'],
                missing_ingredients=recipe_data['missing_ingredients'],
                instructions=recipe_data['instructions'],
                match_percentage=recipe_data['match_percentage']
            )
            recipes.append(recipe)
        
        return recipes
        
    except json.JSONDecodeError:
        # Fallback if JSON parsing fails
        logging.error(f"Failed to parse JSON response: {response}")
        raise HTTPException(status_code=500, detail="Failed to parse recipe response")
    except Exception as e:
        logging.error(f"Error generating recipes: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate recipes")

# API Routes
@api_router.get("/")
async def root():
    return {"message": "ShelfChef API - Ready to cook!"}

@api_router.post("/generate-recipes", response_model=RecipeGenerationResponse)
async def generate_recipes(request: RecipeGenerationRequest):
    """Generate recipes based on user ingredients"""
    
    if not request.ingredients.strip():
        raise HTTPException(status_code=400, detail="Please provide ingredients")
    
    try:
        # Generate recipes using LLM
        recipes = await generate_recipes_with_llm(request.ingredients)
        
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

# Health check
@api_router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ShelfChef API"}