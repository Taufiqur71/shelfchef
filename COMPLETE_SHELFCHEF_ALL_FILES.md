# 🍳 Complete ShelfChef Application - All Files

## 📱 Main React Components

### **File: `frontend/src/components/ShelfChef.js`**

```javascript
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
      {/* Recipe Image */}
      {recipe.image_url && (
        <div className="relative h-48 overflow-hidden">
          <img
            src={recipe.image_url}
            alt={recipe.name}
            className="w-full h-full object-cover transition-transform duration-300 hover:scale-105"
            onError={(e) => {
              e.target.style.display = 'none';
            }}
          />
          <div className="absolute top-4 right-4">
            <Badge className="bg-white text-[#66BB6A] font-semibold text-sm px-3 py-1 shadow-md">
              {recipe.match_percentage}% Match
            </Badge>
          </div>
        </div>
      )}
      
      <CardHeader className="bg-gradient-to-r from-[#66BB6A] to-[#5aa85a] text-white p-6">
        <div className="flex items-center justify-between">
          <div>
            <CardTitle className="text-2xl font-bold mb-2">{recipe.name}</CardTitle>
            <CardDescription className="text-gray-100 text-lg">
              {recipe.description}
            </CardDescription>
          </div>
          {!recipe.image_url && (
            <div className="text-right">
              <Badge className="bg-white text-[#66BB6A] font-semibold text-sm px-3 py-1">
                {recipe.match_percentage}% Match
              </Badge>
            </div>
          )}
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
            <ChefHat className="w-32 h-32 mx-auto text-[#66BB6A]" />
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
```

## 🎨 UI Components

### **File: `frontend/src/components/ui/button.jsx`**

```javascript
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva } from "class-variance-authority"

import { cn } from "../../lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline:
          "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

const Button = React.forwardRef(({ className, variant, size, asChild = false, ...props }, ref) => {
  const Comp = asChild ? Slot : "button"
  return (
    <Comp
      className={cn(buttonVariants({ variant, size, className }))}
      ref={ref}
      {...props}
    />
  )
})
Button.displayName = "Button"

export { Button, buttonVariants }
```

### **File: `frontend/src/components/ui/card.jsx`**

```javascript
import * as React from "react"

import { cn } from "../../lib/utils"

const Card = React.forwardRef(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-lg border bg-card text-card-foreground shadow-sm",
      className
    )}
    {...props}
  />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef(({ className, ...props }, ref) => (
  <h3
    ref={ref}
    className={cn(
      "text-2xl font-semibold leading-none tracking-tight",
      className
    )}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef(({ className, ...props }, ref) => (
  <p
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex items-center p-6 pt-0", className)}
    {...props}
  />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }
```

### **File: `frontend/src/components/ui/badge.jsx`**

```javascript
import * as React from "react"
import { cva } from "class-variance-authority"

import { cn } from "../../lib/utils"

const badgeVariants = cva(
  "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default:
          "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
        secondary:
          "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
        destructive:
          "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
        outline: "text-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

function Badge({ className, variant, ...props }) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  )
}

export { Badge, badgeVariants }
```

### **File: `frontend/src/components/ui/textarea.jsx`**

```javascript
import * as React from "react"

import { cn } from "../../lib/utils"

const Textarea = React.forwardRef(({ className, ...props }, ref) => {
  return (
    <textarea
      className={cn(
        "flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      ref={ref}
      {...props}
    />
  )
})
Textarea.displayName = "Textarea"

export { Textarea }
```

### **File: `frontend/src/components/ui/toaster.jsx`**

```javascript
import { useToast } from "../../hooks/use-toast"
import {
  Toast,
  ToastClose,
  ToastDescription,
  ToastProvider,
  ToastTitle,
  ToastViewport,
} from "./toast"

export function Toaster() {
  const { toasts } = useToast()

  return (
    <ToastProvider>
      {toasts.map(function ({ id, title, description, action, ...props }) {
        return (
          <Toast key={id} {...props}>
            <div className="grid gap-1">
              {title && <ToastTitle>{title}</ToastTitle>}
              {description && (
                <ToastDescription>{description}</ToastDescription>
              )}
            </div>
            {action}
            <ToastClose />
          </Toast>
        )
      })}
      <ToastViewport />
    </ToastProvider>
  )
}
```

### **File: `frontend/src/components/ui/toast.jsx`**

```javascript
import * as React from "react"
import * as ToastPrimitives from "@radix-ui/react-toast"
import { cva } from "class-variance-authority"
import { X } from "lucide-react"

import { cn } from "../../lib/utils"

const ToastProvider = ToastPrimitives.Provider

const ToastViewport = React.forwardRef(({ className, ...props }, ref) => (
  <ToastPrimitives.Viewport
    ref={ref}
    className={cn(
      "fixed top-0 z-[100] flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-0 sm:right-0 sm:top-auto sm:flex-col md:max-w-[420px]",
      className
    )}
    {...props}
  />
))
ToastViewport.displayName = ToastPrimitives.Viewport.displayName

const toastVariants = cva(
  "group pointer-events-auto relative flex w-full items-center justify-between space-x-4 overflow-hidden rounded-md border p-6 pr-8 shadow-lg transition-all data-[swipe=cancel]:translate-x-0 data-[swipe=end]:translate-x-[var(--radix-toast-swipe-end-x)] data-[swipe=move]:translate-x-[var(--radix-toast-swipe-move-x)] data-[swipe=move]:transition-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[swipe=end]:animate-out data-[state=closed]:fade-out-80 data-[state=closed]:slide-out-to-right-full data-[state=open]:slide-in-from-top-full data-[state=open]:sm:slide-in-from-bottom-full",
  {
    variants: {
      variant: {
        default: "border bg-background text-foreground",
        destructive:
          "destructive border-destructive bg-destructive text-destructive-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

const Toast = React.forwardRef(({ className, variant, ...props }, ref) => {
  return (
    <ToastPrimitives.Root
      ref={ref}
      className={cn(toastVariants({ variant }), className)}
      {...props}
    />
  )
})
Toast.displayName = ToastPrimitives.Root.displayName

const ToastAction = React.forwardRef(({ className, ...props }, ref) => (
  <ToastPrimitives.Action
    ref={ref}
    className={cn(
      "inline-flex h-8 shrink-0 items-center justify-center rounded-md border bg-transparent px-3 text-sm font-medium ring-offset-background transition-colors hover:bg-secondary focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 group-[.destructive]:border-muted/40 group-[.destructive]:hover:border-destructive/30 group-[.destructive]:hover:bg-destructive group-[.destructive]:hover:text-destructive-foreground group-[.destructive]:focus:ring-destructive",
      className
    )}
    {...props}
  />
))
ToastAction.displayName = ToastPrimitives.Action.displayName

const ToastClose = React.forwardRef(({ className, ...props }, ref) => (
  <ToastPrimitives.Close
    ref={ref}
    className={cn(
      "absolute right-2 top-2 rounded-md p-1 text-foreground/50 opacity-0 transition-opacity hover:text-foreground focus:opacity-100 focus:outline-none focus:ring-2 group-hover:opacity-100 group-[.destructive]:text-red-300 group-[.destructive]:hover:text-red-50 group-[.destructive]:focus:ring-red-400 group-[.destructive]:focus:ring-offset-red-600",
      className
    )}
    toast-close=""
    {...props}
  >
    <X className="h-4 w-4" />
  </ToastPrimitives.Close>
))
ToastClose.displayName = ToastPrimitives.Close.displayName

const ToastTitle = React.forwardRef(({ className, ...props }, ref) => (
  <ToastPrimitives.Title
    ref={ref}
    className={cn("text-sm font-semibold", className)}
    {...props}
  />
))
ToastTitle.displayName = ToastPrimitives.Title.displayName

const ToastDescription = React.forwardRef(({ className, ...props }, ref) => (
  <ToastPrimitives.Description
    ref={ref}
    className={cn("text-sm opacity-90", className)}
    {...props}
  />
))
ToastDescription.displayName = ToastPrimitives.Description.displayName

export {
  ToastProvider,
  ToastViewport,
  Toast,
  ToastTitle,
  ToastDescription,
  ToastClose,
  ToastAction,
}
```

### **File: `frontend/src/hooks/use-toast.js`**

```javascript
"use client";
// Inspired by react-hot-toast library
import * as React from "react"

const TOAST_LIMIT = 1
const TOAST_REMOVE_DELAY = 1000000

const actionTypes = {
  ADD_TOAST: "ADD_TOAST",
  UPDATE_TOAST: "UPDATE_TOAST",
  DISMISS_TOAST: "DISMISS_TOAST",
  REMOVE_TOAST: "REMOVE_TOAST"
}

let count = 0

function genId() {
  count = (count + 1) % Number.MAX_SAFE_INTEGER
  return count.toString();
}

const toastTimeouts = new Map()

const addToRemoveQueue = (toastId) => {
  if (toastTimeouts.has(toastId)) {
    return
  }

  const timeout = setTimeout(() => {
    toastTimeouts.delete(toastId)
    dispatch({
      type: "REMOVE_TOAST",
      toastId: toastId,
    })
  }, TOAST_REMOVE_DELAY)

  toastTimeouts.set(toastId, timeout)
}

export const reducer = (state, action) => {
  switch (action.type) {
    case "ADD_TOAST":
      return {
        ...state,
        toasts: [action.toast, ...state.toasts].slice(0, TOAST_LIMIT),
      };

    case "UPDATE_TOAST":
      return {
        ...state,
        toasts: state.toasts.map((t) =>
          t.id === action.toast.id ? { ...t, ...action.toast } : t),
      };

    case "DISMISS_TOAST": {
      const { toastId } = action

      if (toastId) {
        addToRemoveQueue(toastId)
      } else {
        state.toasts.forEach((toast) => {
          addToRemoveQueue(toast.id)
        })
      }

      return {
        ...state,
        toasts: state.toasts.map((t) =>
          t.id === toastId || toastId === undefined
            ? {
                ...t,
                open: false,
              }
            : t),
      };
    }
    case "REMOVE_TOAST":
      if (action.toastId === undefined) {
        return {
          ...state,
          toasts: [],
        }
      }
      return {
        ...state,
        toasts: state.toasts.filter((t) => t.id !== action.toastId),
      };
  }
}

const listeners = []

let memoryState = { toasts: [] }

function dispatch(action) {
  memoryState = reducer(memoryState, action)
  listeners.forEach((listener) => {
    listener(memoryState)
  })
}

function toast({
  ...props
}) {
  const id = genId()

  const update = (props) =>
    dispatch({
      type: "UPDATE_TOAST",
      toast: { ...props, id },
    })
  const dismiss = () => dispatch({ type: "DISMISS_TOAST", toastId: id })

  dispatch({
    type: "ADD_TOAST",
    toast: {
      ...props,
      id,
      open: true,
      onOpenChange: (open) => {
        if (!open) dismiss()
      },
    },
  })

  return {
    id: id,
    dismiss,
    update,
  }
}

function useToast() {
  const [state, setState] = React.useState(memoryState)

  React.useEffect(() => {
    listeners.push(setState)
    return () => {
      const index = listeners.indexOf(setState)
      if (index > -1) {
        listeners.splice(index, 1)
      }
    };
  }, [state])

  return {
    ...state,
    toast,
    dismiss: (toastId) => dispatch({ type: "DISMISS_TOAST", toastId }),
  };
}

export { useToast, toast }
```

### **File: `frontend/src/lib/utils.js`**

```javascript
import { clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs) {
  return twMerge(clsx(inputs))
}
```

## 🧠 Backend Recipe Generator

### **File: `backend/recipe_generator.py`**

```python
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
    image_url: str = ""

class RecipeTemplate:
    def __init__(self, name: str, description: str, primary_ingredients: List[str], 
                 optional_ingredients: List[str], cook_time: str, servings: str, 
                 difficulty: str, instructions_template: List[str], category: str = "main",
                 image_url: str = ""):
        self.name = name
        self.description = description
        self.primary_ingredients = primary_ingredients
        self.optional_ingredients = optional_ingredients
        self.cook_time = cook_time
        self.servings = servings
        self.difficulty = difficulty
        self.instructions_template = instructions_template
        self.category = category
        self.image_url = image_url

class SmartRecipeGenerator:
    def __init__(self):
        self.recipe_templates = self._create_recipe_templates()
        self.ingredient_substitutions = self._create_ingredient_substitutions()
        
    def _create_recipe_templates(self) -> List[RecipeTemplate]:
        """Create a comprehensive database of recipe templates with food images"""
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
                    "Beat 2-3 eggs in a bowl and season with salt and pepper",
                    "Heat butter in a non-stick pan over medium heat",
                    "Pour beaten eggs into the pan and let set for 2-3 minutes",
                    "Add your choice of fillings to one half of the omelet",
                    "Fold omelet in half and slide onto plate",
                    "Serve immediately while hot"
                ],
                category="breakfast",
                image_url="https://images.unsplash.com/photo-1482049016688-2d3e1b311543?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzR8MHwxfHNlYXJjaHwxfHxmb29kfGVufDB8fHx8MTc1Mzc2NzU5MXww&ixlib=rb-4.1.0&q=85"
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
                    "Add protein of choice and cook until done, remove and set aside",
                    "Add onion and garlic and stir-fry for 1-2 minutes",
                    "Add cold rice and stir-fry, breaking up any clumps",
                    "Return protein to pan and add seasonings",
                    "Stir-fry for 3-4 minutes until heated through",
                    "Garnish and serve hot"
                ],
                category="main",
                image_url="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzR8MHwxfHNlYXJjaHwyfHxmb29kfGVufDB8fHx8MTc1Mzc2NzU5MXww&ixlib=rb-4.1.0&q=85"
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
                    "Add desired toppings if desired",
                    "Bake for 8-10 minutes until golden and crispy",
                    "Serve warm"
                ],
                category="side",
                image_url="https://images.unsplash.com/photo-1504674900247-0877df9cc836?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzR8MHwxfHNlYXJjaHw0fHxmb29kfGVufDB8fHx8MTc1Mzc2NzU5MXww&ixlib=rb-4.1.0&q=85"
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
                    "Add onion and garlic and sauté for 2-3 minutes",
                    "Add your choice of vegetables and cook until tender",
                    "Toss cooked pasta with vegetable mixture",
                    "Add cheese and seasonings",
                    "Serve immediately with extra cheese if desired"
                ],
                category="main",
                image_url="https://images.pexels.com/photos/376464/pexels-photo-376464.jpeg"
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
                    "Add onion and garlic and stir-fry for 1 minute",
                    "Add your choice of vegetables and cook until crisp-tender",
                    "Return chicken to pan and add sauce",
                    "Stir-fry for 2-3 minutes until heated through"
                ],
                category="main",
                image_url="https://images.unsplash.com/photo-1507048331197-7d4ac70811cf?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHw0fHxjb29raW5nfGVufDB8fHx8MTc1MzcwMzQwNnww&ixlib=rb-4.1.0&q=85"
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
                    "Add desired toppings and top with cheese",
                    "Bake for 3-5 minutes until cheese melts",
                    "Serve hot"
                ],
                category="snack",
                image_url="https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg"
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
                    "Add onion and garlic and sauté until fragrant",
                    "Add carrots and celery and cook for 5 minutes",
                    "Add broth and bring to a boil",
                    "Add tomatoes and leafy greens and simmer for 20 minutes",
                    "Season with salt and pepper to taste",
                    "Serve hot with bread if desired"
                ],
                category="soup",
                image_url="https://images.unsplash.com/photo-1511690656952-34342bb7c2f2?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzR8MHwxfHNlYXJjaHwzfHxmb29kfGVufDB8fHx8MTc1Mzc2NzU5MXww&ixlib=rb-4.1.0&q=85"
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
                    "Add desired fillings if desired",
                    "Heat pan over medium heat",
                    "Cook sandwich for 3-4 minutes per side",
                    "Cook until golden brown and cheese melts",
                    "Cut and serve hot"
                ],
                category="main",
                image_url="https://images.unsplash.com/photo-1466637574441-749b8f19452f?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwzfHxjb29raW5nfGVufDB8fHx8MTc1MzcwMzQwNnww&ixlib=rb-4.1.0&q=85"
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
                instructions=template.instructions_template,
                match_percentage=final_match,
                image_url=template.image_url
            )
            
            recipes.append(recipe)
        
        return recipes
```

## 🧪 Backend Tests

### **File: `backend/tests/test_main.py`**

```python
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
```

### **File: `backend/tests/__init__.py`**

```python
# Tests package for ShelfChef backend
```

## 🔄 GitHub Actions CI/CD

### **File: `.github/workflows/deploy.yml`**

```yaml
name: Deploy ShelfChef

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

env:
  NODE_VERSION: '18'
  PYTHON_VERSION: '3.9'

jobs:
  test-frontend:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./frontend
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: ${{ env.NODE_VERSION }}
        cache: 'npm'
        cache-dependency-path: frontend/package-lock.json
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test -- --coverage --watchAll=false
    
    - name: Build application
      run: npm run build
    
    - name: Upload build artifacts
      uses: actions/upload-artifact@v3
      with:
        name: frontend-build
        path: frontend/build

  test-backend:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./backend
    
    services:
      mongodb:
        image: mongo:5.0
        ports:
          - 27017:27017
        options: >-
          --health-cmd "mongo --eval 'db.runCommand({ ping: 1 })'"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ env.PYTHON_VERSION }}
        cache: 'pip'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-asyncio httpx
    
    - name: Run tests
      env:
        MONGO_URL: mongodb://localhost:27017
        DB_NAME: test_shelfchef
      run: |
        python -m pytest tests/ -v --tb=short
    
    - name: Test API health
      env:
        MONGO_URL: mongodb://localhost:27017
        DB_NAME: test_shelfchef
      run: |
        python -m uvicorn server:app --host 0.0.0.0 --port 8000 &
        sleep 5
        curl -f http://localhost:8000/api/health || exit 1

  deploy-frontend:
    needs: [test-frontend, test-backend]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/master'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Download build artifacts
      uses: actions/download-artifact@v3
      with:
        name: frontend-build
        path: ./frontend/build
    
    - name: Deploy to Vercel
      uses: amondnet/vercel-action@v25
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
        vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
        working-directory: ./frontend
        vercel-args: '--prod'

  deploy-backend:
    needs: [test-frontend, test-backend]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/master'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to Railway
      uses: railwayapp/railway-deploy@v2
      with:
        railway-token: ${{ secrets.RAILWAY_TOKEN }}
        service: shelfchef-backend
        detach: true
```

## 🐳 Docker Configuration

### **File: `backend/Dockerfile`**

```dockerfile
# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 shelfchef && chown -R shelfchef:shelfchef /app
USER shelfchef

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/api/health || exit 1

# Run the application
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🚀 Quick Setup Instructions

1. **Create all these files in your cloned repository**
2. **Install dependencies**:

```bash
# Frontend
cd frontend
npm install
npm start

# Backend  
cd backend
pip install -r requirements.txt
uvicorn server:app --reload
```

3. **Push to GitHub**:
```bash
git add .
git commit -m "Complete ShelfChef application with all features"
git push origin main
```

4. **Set up deployment platforms and add GitHub secrets**

Your complete ShelfChef application is now ready! 🍳✨
```