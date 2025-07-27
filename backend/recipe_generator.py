"""
Smart Recipe Generator - Fallback solution for generating recipes without external APIs
"""
import random
from typing import List, Dict, Tuple
from pydantic import BaseModel

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

class RecipeTemplate:
    def __init__(self, name: str, description: str, primary_ingredients: List[str], 
                 optional_ingredients: List[str], cook_time: str, servings: str, 
                 difficulty: str, instructions_template: List[str], category: str = "main"):
        self.name = name
        self.description = description
        self.primary_ingredients = primary_ingredients
        self.optional_ingredients = optional_ingredients
        self.cook_time = cook_time
        self.servings = servings
        self.difficulty = difficulty
        self.instructions_template = instructions_template
        self.category = category

class SmartRecipeGenerator:
    def __init__(self):
        self.recipe_templates = self._create_recipe_templates()
        self.ingredient_substitutions = self._create_ingredient_substitutions()
        self.cooking_methods = {
            "sauté": "Heat oil in a pan over medium heat",
            "boil": "Bring water to a boil",
            "bake": "Preheat oven to {temp}°F",
            "grill": "Heat grill to medium-high heat",
            "steam": "Set up steamer over boiling water"
        }
        
    def _create_recipe_templates(self) -> List[RecipeTemplate]:
        """Create a comprehensive database of recipe templates"""
        return [
            RecipeTemplate(
                name="Classic Omelet",
                description="A fluffy omelet with fresh ingredients",
                primary_ingredients=["eggs"],
                optional_ingredients=["cheese", "tomato", "onion", "spinach", "mushrooms", "bell pepper"],
                cook_time="8-10 mins",
                servings="2 servings",
                difficulty="Easy",
                instructions_template=[
                    "Beat {eggs_count} eggs in a bowl and season with salt and pepper",
                    "Heat butter in a non-stick pan over medium heat",
                    "Pour beaten eggs into the pan and let set for 2-3 minutes",
                    "Add {fillings} to one half of the omelet",
                    "Fold omelet in half and slide onto plate",
                    "Serve immediately while hot"
                ],
                category="breakfast"
            ),
            RecipeTemplate(
                name="Fried Rice",
                description="A satisfying stir-fried rice dish with vegetables and protein",
                primary_ingredients=["rice"],
                optional_ingredients=["chicken", "eggs", "onion", "garlic", "soy sauce", "vegetables"],
                cook_time="15-20 mins",
                servings="4 servings",
                difficulty="Medium",
                instructions_template=[
                    "Cook rice according to package instructions and let cool",
                    "Heat oil in a large wok or pan over high heat",
                    "Add {protein} and cook until done, remove and set aside",
                    "Add {aromatics} and stir-fry for 1-2 minutes",
                    "Add cold rice and stir-fry, breaking up any clumps",
                    "Return {protein} to pan and add {seasonings}",
                    "Stir-fry for 3-4 minutes until heated through",
                    "Garnish and serve hot"
                ],
                category="main"
            ),
            RecipeTemplate(
                name="Garlic Bread",
                description="Crispy bread with aromatic garlic butter",
                primary_ingredients=["bread", "garlic"],
                optional_ingredients=["butter", "cheese", "parsley", "olive oil"],
                cook_time="10-12 mins",
                servings="4 servings",
                difficulty="Easy",
                instructions_template=[
                    "Preheat oven to 375°F",
                    "Slice bread into thick pieces",
                    "Mix minced garlic with softened butter",
                    "Spread garlic butter mixture on bread slices",
                    "Add {toppings} if desired",
                    "Bake for 8-10 minutes until golden and crispy",
                    "Serve warm"
                ],
                category="side"
            ),
            RecipeTemplate(
                name="Pasta Primavera",
                description="Fresh pasta with seasonal vegetables",
                primary_ingredients=["pasta"],
                optional_ingredients=["tomato", "onion", "garlic", "bell pepper", "mushrooms", "cheese"],
                cook_time="20-25 mins",
                servings="4 servings",
                difficulty="Medium",
                instructions_template=[
                    "Cook pasta according to package directions until al dente",
                    "Heat olive oil in a large pan over medium heat",
                    "Add {aromatics} and sauté for 2-3 minutes",
                    "Add {vegetables} and cook until tender",
                    "Toss cooked pasta with vegetable mixture",
                    "Add {cheese} and seasonings",
                    "Serve immediately with extra cheese if desired"
                ],
                category="main"
            ),
            RecipeTemplate(
                name="Chicken Stir-fry",
                description="Quick and healthy chicken with vegetables",
                primary_ingredients=["chicken"],
                optional_ingredients=["onion", "garlic", "bell pepper", "broccoli", "soy sauce", "ginger"],
                cook_time="15-18 mins",
                servings="3 servings",
                difficulty="Medium",
                instructions_template=[
                    "Cut chicken into bite-sized pieces",
                    "Heat oil in a wok or large pan over high heat",
                    "Add chicken and cook until golden brown",
                    "Remove chicken and set aside",
                    "Add {aromatics} and stir-fry for 1 minute",
                    "Add {vegetables} and cook until crisp-tender",
                    "Return chicken to pan and add sauce",
                    "Stir-fry for 2-3 minutes until heated through"
                ],
                category="main"
            ),
            RecipeTemplate(
                name="Cheese Toast",
                description="Melted cheese on toasted bread",
                primary_ingredients=["bread", "cheese"],
                optional_ingredients=["butter", "tomato", "onion", "herbs"],
                cook_time="5-8 mins",
                servings="2 servings",
                difficulty="Easy",
                instructions_template=[
                    "Preheat oven to 400°F or use a toaster oven",
                    "Toast bread slices lightly",
                    "Spread butter on toast if desired",
                    "Add {toppings} and top with cheese",
                    "Bake for 3-5 minutes until cheese melts",
                    "Serve hot"
                ],
                category="snack"
            ),
            RecipeTemplate(
                name="Vegetable Soup",
                description="Hearty soup with fresh vegetables",
                primary_ingredients=["vegetables"],
                optional_ingredients=["onion", "garlic", "tomato", "carrot", "celery", "potato"],
                cook_time="30-40 mins",
                servings="6 servings",
                difficulty="Easy",
                instructions_template=[
                    "Heat oil in a large pot over medium heat",
                    "Add {aromatics} and sauté until fragrant",
                    "Add {hard_vegetables} and cook for 5 minutes",
                    "Add broth and bring to a boil",
                    "Add {soft_vegetables} and simmer for 20 minutes",
                    "Season with salt and pepper to taste",
                    "Serve hot with bread if desired"
                ],
                category="soup"
            ),
            RecipeTemplate(
                name="Grilled Cheese Sandwich",
                description="Classic comfort food sandwich",
                primary_ingredients=["bread", "cheese"],
                optional_ingredients=["butter", "tomato", "onion"],
                cook_time="6-8 mins",
                servings="2 servings",
                difficulty="Easy",
                instructions_template=[
                    "Butter one side of each bread slice",
                    "Place cheese between bread slices, butter-side out",
                    "Add {fillings} if desired",
                    "Heat pan over medium heat",
                    "Cook sandwich for 3-4 minutes per side",
                    "Cook until golden brown and cheese melts",
                    "Cut and serve hot"
                ],
                category="main"
            )
        ]
    
    def _create_ingredient_substitutions(self) -> Dict[str, List[str]]:
        """Create ingredient substitution mapping"""
        return {
            "chicken": ["turkey", "beef", "pork", "tofu"],
            "rice": ["quinoa", "pasta", "noodles", "couscous"],
            "onion": ["shallot", "green onion", "leek"],
            "garlic": ["garlic powder", "shallot"],
            "tomato": ["tomato paste", "canned tomatoes", "cherry tomatoes"],
            "cheese": ["mozzarella", "cheddar", "parmesan", "swiss"],
            "butter": ["olive oil", "vegetable oil", "margarine"],
            "bread": ["baguette", "sourdough", "whole wheat bread"],
            "pasta": ["spaghetti", "penne", "fettuccine", "linguine"],
            "bell pepper": ["jalapeño", "poblano", "sweet pepper"],
            "mushrooms": ["shiitake", "portobello", "button mushrooms"],
            "spinach": ["kale", "arugula", "lettuce"],
            "herbs": ["basil", "oregano", "thyme", "parsley"]
        }
    
    def normalize_ingredient(self, ingredient: str) -> str:
        """Normalize ingredient names for better matching"""
        ingredient = ingredient.lower().strip()
        
        # Common normalizations
        normalizations = {
            "tomatoes": "tomato",
            "onions": "onion", 
            "eggs": "egg",
            "chickens": "chicken",
            "cheeses": "cheese",
            "mushroom": "mushrooms",
            "bell peppers": "bell pepper",
            "green onions": "green onion",
            "scallions": "green onion"
        }
        
        return normalizations.get(ingredient, ingredient)
    
    def calculate_match_percentage(self, user_ingredients: List[str], recipe_ingredients: List[str]) -> int:
        """Calculate how well user ingredients match recipe requirements"""
        if not recipe_ingredients:
            return 100
            
        normalized_user = [self.normalize_ingredient(ing) for ing in user_ingredients]
        normalized_recipe = [self.normalize_ingredient(ing) for ing in recipe_ingredients]
        
        matches = 0
        for recipe_ing in normalized_recipe:
            if recipe_ing in normalized_user:
                matches += 1
            else:
                # Check substitutions
                for user_ing in normalized_user:
                    if user_ing in self.ingredient_substitutions.get(recipe_ing, []):
                        matches += 1
                        break
        
        return min(100, int((matches / len(recipe_ingredients)) * 100))
    
    def find_available_ingredients(self, user_ingredients: List[str], recipe_ingredients: List[str]) -> List[str]:
        """Find which recipe ingredients the user has"""
        available = []
        normalized_user = [self.normalize_ingredient(ing) for ing in user_ingredients]
        
        for recipe_ing in recipe_ingredients:
            normalized_recipe_ing = self.normalize_ingredient(recipe_ing)
            
            if normalized_recipe_ing in normalized_user:
                available.append(recipe_ing)
            else:
                # Check substitutions
                for user_ing in user_ingredients:
                    if self.normalize_ingredient(user_ing) in self.ingredient_substitutions.get(normalized_recipe_ing, []):
                        available.append(user_ing)
                        break
        
        return available
    
    def generate_missing_ingredients(self, recipe_template: RecipeTemplate, available_ingredients: List[str]) -> List[str]:
        """Generate list of missing ingredients for a recipe"""
        all_recipe_ingredients = recipe_template.primary_ingredients + recipe_template.optional_ingredients
        available_normalized = [self.normalize_ingredient(ing) for ing in available_ingredients]
        
        missing = []
        for ing in all_recipe_ingredients:
            if self.normalize_ingredient(ing) not in available_normalized:
                # Check if we have a substitution
                has_substitute = False
                for avail_ing in available_normalized:
                    if avail_ing in self.ingredient_substitutions.get(self.normalize_ingredient(ing), []):
                        has_substitute = True
                        break
                
                if not has_substitute:
                    missing.append(ing)
        
        # Add common basic ingredients that are often needed
        basic_ingredients = ["salt", "pepper", "oil", "butter"]
        for basic in basic_ingredients:
            if basic not in [self.normalize_ingredient(ing) for ing in available_ingredients]:
                if basic not in missing:
                    missing.append(basic)
        
        return missing[:4]  # Limit to 4 missing ingredients
    
    def customize_instructions(self, template: RecipeTemplate, available_ingredients: List[str]) -> List[str]:
        """Customize recipe instructions based on available ingredients"""
        instructions = []
        
        for instruction in template.instructions_template:
            customized = instruction
            
            # Replace placeholders with actual ingredients
            if "{eggs_count}" in customized:
                customized = customized.replace("{eggs_count}", "2-3")
            
            if "{fillings}" in customized:
                fillings = [ing for ing in available_ingredients if ing.lower() in ["cheese", "tomato", "onion", "spinach", "mushrooms"]]
                if fillings:
                    customized = customized.replace("{fillings}", ", ".join(fillings))
                else:
                    customized = customized.replace("{fillings}", "your choice of fillings")
            
            if "{protein}" in customized:
                proteins = [ing for ing in available_ingredients if ing.lower() in ["chicken", "beef", "eggs", "tofu"]]
                if proteins:
                    customized = customized.replace("{protein}", proteins[0])
                else:
                    customized = customized.replace("{protein}", "protein of choice")
            
            if "{aromatics}" in customized:
                aromatics = [ing for ing in available_ingredients if ing.lower() in ["onion", "garlic", "ginger"]]
                if aromatics:
                    customized = customized.replace("{aromatics}", ", ".join(aromatics))
                else:
                    customized = customized.replace("{aromatics}", "onion and garlic")
            
            if "{vegetables}" in customized:
                vegetables = [ing for ing in available_ingredients if ing.lower() in ["tomato", "bell pepper", "mushrooms", "spinach", "carrot"]]
                if vegetables:
                    customized = customized.replace("{vegetables}", ", ".join(vegetables))
                else:
                    customized = customized.replace("{vegetables}", "your choice of vegetables")
            
            if "{toppings}" in customized:
                toppings = [ing for ing in available_ingredients if ing.lower() in ["cheese", "herbs", "tomato"]]
                if toppings:
                    customized = customized.replace("{toppings}", ", ".join(toppings))
                else:
                    customized = customized.replace("{toppings}", "desired toppings")
            
            if "{seasonings}" in customized:
                customized = customized.replace("{seasonings}", "salt, pepper, and seasonings to taste")
            
            if "{hard_vegetables}" in customized:
                hard_veg = [ing for ing in available_ingredients if ing.lower() in ["carrot", "potato", "celery", "onion"]]
                if hard_veg:
                    customized = customized.replace("{hard_vegetables}", ", ".join(hard_veg))
                else:
                    customized = customized.replace("{hard_vegetables}", "carrots and celery")
            
            if "{soft_vegetables}" in customized:
                soft_veg = [ing for ing in available_ingredients if ing.lower() in ["tomato", "spinach", "mushrooms"]]
                if soft_veg:
                    customized = customized.replace("{soft_vegetables}", ", ".join(soft_veg))
                else:
                    customized = customized.replace("{soft_vegetables}", "tomatoes and leafy greens")
            
            instructions.append(customized)
        
        return instructions
    
    def generate_recipes(self, ingredients_input: str, max_recipes: int = 3) -> List[Recipe]:
        """Generate recipes based on user ingredients"""
        # Parse ingredients
        user_ingredients = [ing.strip() for ing in ingredients_input.split(',') if ing.strip()]
        
        if not user_ingredients:
            return []
        
        # Find matching recipes
        recipe_matches = []
        
        for template in self.recipe_templates:
            # Calculate match for primary ingredients
            primary_match = self.calculate_match_percentage(user_ingredients, template.primary_ingredients)
            
            # Calculate match for all ingredients
            all_ingredients = template.primary_ingredients + template.optional_ingredients
            overall_match = self.calculate_match_percentage(user_ingredients, all_ingredients)
            
            # Only include recipes where we have at least one primary ingredient
            if primary_match > 0:
                recipe_matches.append((template, overall_match, primary_match))
        
        # Sort by match percentage (overall first, then primary)
        recipe_matches.sort(key=lambda x: (x[1], x[2]), reverse=True)
        
        # Generate top recipes
        recipes = []
        for i, (template, overall_match, primary_match) in enumerate(recipe_matches[:max_recipes]):
            available_ingredients = self.find_available_ingredients(user_ingredients, 
                                                                   template.primary_ingredients + template.optional_ingredients)
            missing_ingredients = self.generate_missing_ingredients(template, available_ingredients)
            instructions = self.customize_instructions(template, available_ingredients)
            
            # Add some variation to the match percentage
            final_match = max(40, min(95, overall_match + random.randint(-5, 10)))
            
            recipe = Recipe(
                name=template.name,
                description=template.description,
                cook_time=template.cook_time,
                servings=template.servings,
                difficulty=template.difficulty,
                available_ingredients=available_ingredients,
                missing_ingredients=missing_ingredients,
                instructions=instructions,
                match_percentage=final_match
            )
            
            recipes.append(recipe)
        
        return recipes