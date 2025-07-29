// MongoDB initialization script for production
db = db.getSiblingDB('shelfchef');

// Create collections with proper indexes
db.createCollection('saved_recipes');
db.createCollection('recipe_analytics');

// Create indexes for better performance
db.saved_recipes.createIndex({ "id": 1 }, { unique: true });
db.saved_recipes.createIndex({ "saved_at": -1 });
db.saved_recipes.createIndex({ "name": "text", "description": "text" });
db.saved_recipes.createIndex({ "match_percentage": -1 });

// Create analytics collection indexes
db.recipe_analytics.createIndex({ "timestamp": -1 });
db.recipe_analytics.createIndex({ "recipe_id": 1 });
db.recipe_analytics.createIndex({ "user_id": 1 });

// Insert sample data (optional)
db.saved_recipes.insertMany([
    {
        id: "sample_recipe_1",
        name: "Welcome Recipe",
        description: "A sample recipe to get you started",
        cook_time: "5 mins",
        servings: "1 serving",
        difficulty: "Easy",
        available_ingredients: ["sample"],
        missing_ingredients: [],
        instructions: ["This is a sample recipe", "Feel free to delete it"],
        match_percentage: 100,
        image_url: "",
        saved_at: new Date()
    }
]);

print("Database initialized successfully!");
print("Collections created: saved_recipes, recipe_analytics");
print("Indexes created for optimal performance");
print("Sample data inserted");