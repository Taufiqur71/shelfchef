import React, { useState, useEffect } from "react";
import { Button } from "./ui/button";
import { Textarea } from "./ui/textarea";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Badge } from "./ui/badge";
import { ChefHat, Clock, Users, Star, Bookmark, Heart } from "lucide-react";
import { useToast } from "../hooks/use-toast";
import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const ShelfChef = () => {
  const [ingredients, setIngredients] = useState("");
  const [recipes, setRecipes] = useState([]);
  const [savedRecipes, setSavedRecipes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [showSavedRecipes, setShowSavedRecipes] = useState(false);
  const { toast } = useToast();

  // Load saved recipes on component mount
  useEffect(() => {
    loadSavedRecipes();
  }, []);

  const loadSavedRecipes = async () => {
    try {
      const response = await axios.get(`${API}/saved-recipes`);
      setSavedRecipes(response.data);
    } catch (error) {
      console.error("Error loading saved recipes:", error);
    }
  };

  const handleGetRecipes = async () => {
    if (!ingredients.trim()) {
      toast({
        title: "Please enter some ingredients",
        description: "Tell us what you have in your kitchen!",
        variant: "destructive",
      });
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post(`${API}/generate-recipes`, {
        ingredients: ingredients.trim()
      });
      
      setRecipes(response.data.recipes);
      setShowSavedRecipes(false);
      
      toast({
        title: "Recipes generated!",
        description: `Found ${response.data.recipes.length} delicious recipes for you.`,
      });
      
    } catch (error) {
      console.error("Error generating recipes:", error);
      toast({
        title: "Error generating recipes",
        description: "Please try again in a moment.",
        variant: "destructive",
      });
    } finally {
      setLoading(false);
    }
  };

  const handleSaveRecipe = async (recipe) => {
    try {
      await axios.post(`${API}/save-recipe`, recipe);
      
      toast({
        title: "Recipe saved!",
        description: `${recipe.name} has been saved to your collection.`,
      });
      
      // Reload saved recipes
      loadSavedRecipes();
      
    } catch (error) {
      console.error("Error saving recipe:", error);
      toast({
        title: "Error saving recipe",
        description: "Please try again.",
        variant: "destructive",
      });
    }
  };

  const handleDeleteRecipe = async (recipeId) => {
    try {
      await axios.delete(`${API}/saved-recipes/${recipeId}`);
      
      toast({
        title: "Recipe deleted",
        description: "Recipe has been removed from your collection.",
      });
      
      // Reload saved recipes
      loadSavedRecipes();
      
    } catch (error) {
      console.error("Error deleting recipe:", error);
      toast({
        title: "Error deleting recipe",
        description: "Please try again.",
        variant: "destructive",
      });
    }
  };

  const toggleSavedRecipes = () => {
    setShowSavedRecipes(!showSavedRecipes);
    if (!showSavedRecipes) {
      loadSavedRecipes();
    }
  };

  const renderRecipeCard = (recipe, index, isSaved = false) => (
    <Card key={index} className="bg-white shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100 rounded-2xl overflow-hidden">
      <CardHeader className="bg-gradient-to-r from-[#66BB6A] to-[#5aa85a] text-white p-6">
        <div className="flex items-center justify-between">
          <div>
            <CardTitle className="text-2xl font-bold mb-2">{recipe.name}</CardTitle>
            <CardDescription className="text-gray-100 text-lg">
              {recipe.description}
            </CardDescription>
          </div>
          <div className="text-right">
            <Badge className="bg-white text-[#66BB6A] font-semibold text-sm px-3 py-1">
              {recipe.match_percentage}% Match
            </Badge>
          </div>
        </div>
      </CardHeader>
      
      <CardContent className="p-6">
        <div className="grid md:grid-cols-2 gap-6">
          {/* Recipe Info */}
          <div className="space-y-4">
            <div className="flex items-center gap-4 text-gray-600">
              <div className="flex items-center gap-1">
                <Clock className="w-4 h-4" />
                <span className="text-sm">{recipe.cook_time}</span>
              </div>
              <div className="flex items-center gap-1">
                <Users className="w-4 h-4" />
                <span className="text-sm">{recipe.servings}</span>
              </div>
              <div className="flex items-center gap-1">
                <Star className="w-4 h-4 text-[#FF7043]" />
                <span className="text-sm">{recipe.difficulty}</span>
              </div>
            </div>

            <div>
              <h4 className="font-semibold text-gray-800 mb-2">Ingredients You Have:</h4>
              <div className="flex flex-wrap gap-2">
                {recipe.available_ingredients.map((ingredient, i) => (
                  <Badge key={i} variant="secondary" className="bg-green-100 text-green-800 border-green-200">
                    {ingredient}
                  </Badge>
                ))}
              </div>
            </div>

            {recipe.missing_ingredients && recipe.missing_ingredients.length > 0 && (
              <div>
                <h4 className="font-semibold text-gray-800 mb-2">You'll Need:</h4>
                <div className="flex flex-wrap gap-2">
                  {recipe.missing_ingredients.map((ingredient, i) => (
                    <Badge key={i} variant="outline" className="border-[#FF7043] text-[#FF7043]">
                      {ingredient}
                    </Badge>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Instructions */}
          <div>
            <h4 className="font-semibold text-gray-800 mb-3">Instructions:</h4>
            <ol className="space-y-2 text-gray-600">
              {recipe.instructions.map((step, i) => (
                <li key={i} className="flex gap-3">
                  <span className="bg-[#66BB6A] text-white rounded-full w-6 h-6 flex items-center justify-center text-sm font-semibold flex-shrink-0">
                    {i + 1}
                  </span>
                  <span className="text-sm leading-relaxed">{step}</span>
                </li>
              ))}
            </ol>
          </div>
        </div>

        <div className="mt-6 pt-4 border-t border-gray-200 flex gap-3">
          {!isSaved ? (
            <Button
              onClick={() => handleSaveRecipe(recipe)}
              className="bg-[#FF7043] hover:bg-[#e85d2f] text-white font-semibold py-2 px-6 rounded-lg transition-all duration-300 transform hover:scale-105"
            >
              <Bookmark className="w-4 h-4 mr-2" />
              Save Recipe
            </Button>
          ) : (
            <Button
              onClick={() => handleDeleteRecipe(recipe.id)}
              variant="destructive"
              className="font-semibold py-2 px-6 rounded-lg transition-all duration-300 transform hover:scale-105"
            >
              <Heart className="w-4 h-4 mr-2" />
              Remove
            </Button>
          )}
        </div>
      </CardContent>
    </Card>
  );

  return (
    <div className="min-h-screen bg-[#FAFAFA] font-nunito">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <ChefHat className="w-10 h-10 text-[#66BB6A]" />
            <h1 className="text-5xl font-bold text-gray-800 tracking-tight">
              ShelfChef
            </h1>
          </div>
          <h2 className="text-3xl font-semibold text-gray-700 mb-2">
            What's in your kitchen?
          </h2>
          <p className="text-gray-600 text-lg max-w-2xl mx-auto">
            Tell us what ingredients you have, and we'll create amazing recipes just for you!
          </p>
        </div>

        {/* Navigation */}
        <div className="flex justify-center mb-8">
          <div className="bg-white rounded-xl shadow-lg p-1 flex">
            <Button
              onClick={() => setShowSavedRecipes(false)}
              variant={!showSavedRecipes ? "default" : "ghost"}
              className={`px-6 py-2 rounded-lg transition-all duration-300 ${
                !showSavedRecipes 
                  ? "bg-[#66BB6A] text-white" 
                  : "text-gray-600 hover:bg-gray-100"
              }`}
            >
              Generate Recipes
            </Button>
            <Button
              onClick={toggleSavedRecipes}
              variant={showSavedRecipes ? "default" : "ghost"}
              className={`px-6 py-2 rounded-lg transition-all duration-300 ${
                showSavedRecipes 
                  ? "bg-[#66BB6A] text-white" 
                  : "text-gray-600 hover:bg-gray-100"
              }`}
            >
              Saved Recipes ({savedRecipes.length})
            </Button>
          </div>
        </div>

        {!showSavedRecipes ? (
          <>
            {/* Input Section */}
            <div className="bg-white rounded-2xl shadow-lg p-8 mb-8 border border-gray-100">
              <div className="space-y-6">
                <div>
                  <label className="block text-lg font-semibold text-gray-700 mb-3">
                    Your Ingredients
                  </label>
                  <Textarea
                    value={ingredients}
                    onChange={(e) => setIngredients(e.target.value)}
                    placeholder="e.g., chicken, tomato, rice, onion, garlic, cheese..."
                    className="min-h-[120px] text-lg p-4 border-2 border-gray-200 focus:border-[#66BB6A] rounded-xl resize-none transition-all duration-300"
                    style={{ fontSize: '16px' }}
                  />
                  <p className="text-sm text-gray-500 mt-2">
                    Separate ingredients with commas for best results
                  </p>
                </div>
                
                <Button
                  onClick={handleGetRecipes}
                  disabled={loading}
                  className="w-full bg-[#66BB6A] hover:bg-[#5aa85a] text-white font-semibold py-4 px-8 rounded-xl text-lg transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl"
                >
                  {loading ? (
                    <div className="flex items-center gap-2">
                      <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                      Creating Recipes...
                    </div>
                  ) : (
                    "Get Recipes"
                  )}
                </Button>
              </div>
            </div>

            {/* Generated Recipes Section */}
            {recipes.length > 0 && (
              <div className="space-y-6">
                <h3 className="text-2xl font-bold text-gray-800 mb-6 text-center">
                  Here are some delicious recipes for you! 🍳
                </h3>
                
                {recipes.map((recipe, index) => renderRecipeCard(recipe, index))}
              </div>
            )}
          </>
        ) : (
          /* Saved Recipes Section */
          <div className="space-y-6">
            <h3 className="text-2xl font-bold text-gray-800 mb-6 text-center">
              Your Saved Recipes 📚
            </h3>
            
            {savedRecipes.length === 0 ? (
              <div className="text-center py-12">
                <Bookmark className="w-16 h-16 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-600 text-lg">
                  No saved recipes yet. Generate some recipes and save your favorites!
                </p>
              </div>
            ) : (
              savedRecipes.map((recipe, index) => renderRecipeCard(recipe, index, true))
            )}
          </div>
        )}

        {/* Logo Section */}
        <div className="mt-16 text-center">
          <div className="inline-block p-6 bg-white rounded-2xl shadow-lg">
            <img
              src="https://customer-assets.emergentagent.com/job_327a38f0-bf23-4d04-bf9d-8a264d3faf2a/artifacts/wqiifq1a_WhatsApp%20Image%202025-07-26%20at%2023.30.30_831d4474.jpg"
              alt="ShelfChef Logo"
              className="w-32 h-32 mx-auto object-contain"
            />
          </div>
          <p className="mt-4 text-gray-600 text-sm">
            Made with ❤️ by ShelfChef
          </p>
        </div>
      </div>
    </div>
  );
};

export default ShelfChef;