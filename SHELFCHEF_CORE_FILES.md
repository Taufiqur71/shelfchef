# 🍳 ShelfChef Core Files - Complete Download Structure

## 📋 Priority Files (Create these first)

### 1. **frontend/src/App.js**
```javascript
import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./components/LandingPage";
import ShelfChef from "./components/ShelfChef";
import { Toaster } from "./components/ui/toaster";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/app" element={<ShelfChef />} />
        </Routes>
      </BrowserRouter>
      <Toaster />
    </div>
  );
}

export default App;
```

### 2. **frontend/src/index.css**
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto",
        "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans",
        "Helvetica Neue", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

code {
    font-family: source-code-pro, Menlo, Monaco, Consolas, "Courier New",
        monospace;
}

@layer base {
  :root {
        --background: 0 0% 100%;
        --foreground: 0 0% 3.9%;
        --card: 0 0% 100%;
        --card-foreground: 0 0% 3.9%;
        --popover: 0 0% 100%;
        --popover-foreground: 0 0% 3.9%;
        --primary: 0 0% 9%;
        --primary-foreground: 0 0% 98%;
        --secondary: 0 0% 96.1%;
        --secondary-foreground: 0 0% 9%;
        --muted: 0 0% 96.1%;
        --muted-foreground: 0 0% 45.1%;
        --accent: 0 0% 96.1%;
        --accent-foreground: 0 0% 9%;
        --destructive: 0 84.2% 60.2%;
        --destructive-foreground: 0 0% 98%;
        --border: 0 0% 89.8%;
        --input: 0 0% 89.8%;
        --ring: 0 0% 3.9%;
        --chart-1: 12 76% 61%;
        --chart-2: 173 58% 39%;
        --chart-3: 197 37% 24%;
        --chart-4: 43 74% 66%;
        --chart-5: 27 87% 67%;
        --radius: 0.5rem;
    }
  .dark {
        --background: 0 0% 3.9%;
        --foreground: 0 0% 98%;
        --card: 0 0% 3.9%;
        --card-foreground: 0 0% 98%;
        --popover: 0 0% 3.9%;
        --popover-foreground: 0 0% 98%;
        --primary: 0 0% 98%;
        --primary-foreground: 0 0% 9%;
        --secondary: 0 0% 14.9%;
        --secondary-foreground: 0 0% 98%;
        --muted: 0 0% 14.9%;
        --muted-foreground: 0 0% 63.9%;
        --accent: 0 0% 14.9%;
        --accent-foreground: 0 0% 98%;
        --destructive: 0 62.8% 30.6%;
        --destructive-foreground: 0 0% 98%;
        --border: 0 0% 14.9%;
        --input: 0 0% 14.9%;
        --ring: 0 0% 83.1%;
        --chart-1: 220 70% 50%;
        --chart-2: 160 60% 45%;
        --chart-3: 30 80% 55%;
        --chart-4: 280 65% 60%;
        --chart-5: 340 75% 55%;
    }
}

@layer base {
  * {
    @apply border-border;
    }
  body {
    @apply bg-background text-foreground;
    }
}
```

### 3. **frontend/src/App.css**
```css
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700;800;900&display=swap');

.font-nunito {
  font-family: 'Nunito', sans-serif;
}

.App {
  min-height: 100vh;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: #66BB6A;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: #5aa85a;
}

/* Smooth transitions */
* {
  transition: all 0.3s ease;
}

/* Button animations */
.transform {
  transition: transform 0.3s ease;
}

.hover\:scale-105:hover {
  transform: scale(1.05);
}

/* Input focus animations */
.focus\:border-\[\#66BB6A\]:focus {
  border-color: #66BB6A;
  box-shadow: 0 0 0 3px rgba(102, 187, 106, 0.1);
}

/* Card hover effects */
.hover\:shadow-xl:hover {
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
}

/* Loading animation */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

/* Entrance animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeInUp {
  animation: fadeInUp 0.6s ease-out;
}

/* Responsive design enhancements */
@media (max-width: 768px) {
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }
  
  .text-5xl {
    font-size: 2.5rem;
  }
  
  .text-3xl {
    font-size: 1.875rem;
  }
}
```

### 4. **backend/server.py**
```python
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
    image_url: str = ""
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
    image_url: str = ""

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
    
    saved_recipe = SavedRecipe(**recipe_data.model_dump())
    
    try:
        # Insert into MongoDB
        await db.saved_recipes.insert_one(saved_recipe.model_dump())
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
```

### 5. **frontend/.env**
```env
REACT_APP_BACKEND_URL=http://localhost:8000
```

### 6. **backend/.env**
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=shelfchef
```

### 7. **frontend/vercel.json**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "build"
      }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "headers": {
        "cache-control": "public, max-age=31536000, immutable"
      }
    },
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ],
  "env": {
    "REACT_APP_BACKEND_URL": "@backend_url"
  },
  "build": {
    "env": {
      "REACT_APP_BACKEND_URL": "@backend_url"
    }
  }
}
```

## 🚀 Quick Setup Instructions

1. **Create GitHub repository**: https://github.com/new (name: `shelfchef`)

2. **Clone and setup**:
```bash
git clone https://github.com/Taufiqur71/shelfchef.git
cd shelfchef

# Create all the files above
# Then:

git add .
git commit -m "Initial ShelfChef application"
git push -u origin main
```

3. **Setup frontend**:
```bash
cd frontend
npm install
npm start
```

4. **Setup backend**:
```bash
cd backend
pip install -r requirements.txt
uvicorn server:app --reload
```

## 📁 Remaining Files

I have 15+ more essential files including:
- All UI components (Button, Card, Badge, etc.)
- LandingPage.js and ShelfChef.js (main components)
- Recipe generator logic
- GitHub Actions workflows
- Docker configurations

Would you like me to:
1. **Continue with the UI components**
2. **Provide the main page components (LandingPage & ShelfChef)**
3. **Show the recipe generator logic**
4. **Focus on deployment files**

**What's your priority?** I'll provide the next set based on what you need most!