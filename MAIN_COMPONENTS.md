# 🎨 ShelfChef Main Components

## **File: `frontend/src/components/LandingPage.js`**

```javascript
import React from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "./ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Badge } from "./ui/badge";
import { ChefHat, Sparkles, Clock, Heart, Star, ArrowRight, CheckCircle, Users, TrendingUp } from "lucide-react";

const LandingPage = () => {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate("/app");
  };

  const features = [
    {
      icon: <Sparkles className="w-8 h-8 text-[#66BB6A]" />,
      title: "Smart Recipe Generation",
      description: "Our AI analyzes your ingredients and creates personalized recipes just for you.",
      highlight: "Instant Results"
    },
    {
      icon: <Clock className="w-8 h-8 text-[#FF7043]" />,
      title: "Quick & Easy",
      description: "Get delicious recipe ideas in seconds. No more wondering what to cook tonight!",
      highlight: "Under 30 Seconds"
    },
    {
      icon: <Heart className="w-8 h-8 text-[#E91E63]" />,
      title: "Save Favorites",
      description: "Build your personal recipe collection by saving dishes you love.",
      highlight: "Personal Library"
    }
  ];

  const testimonials = [
    {
      name: "Sarah Johnson",
      role: "Home Chef",
      image: "https://images.unsplash.com/photo-1494790108755-2616b75c130c?w=100&h=100&fit=crop&crop=face",
      quote: "ShelfChef has transformed my cooking! I used to waste so much food, but now I can create amazing meals with whatever I have.",
      rating: 5
    },
    {
      name: "Mike Chen",
      role: "Busy Parent",
      image: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop&crop=face",
      quote: "As a working parent, this app is a lifesaver. Quick, healthy meals using ingredients I already have at home.",
      rating: 5
    },
    {
      name: "Emma Rodriguez",
      role: "Food Enthusiast",
      image: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop&crop=face",
      quote: "I love how creative the recipe suggestions are! It's like having a personal chef who knows my pantry.",
      rating: 5
    }
  ];

  const steps = [
    {
      number: "01",
      title: "List Your Ingredients",
      description: "Simply type in what you have in your kitchen - no need to be precise!"
    },
    {
      number: "02",
      title: "Get Smart Suggestions",
      description: "Our AI instantly generates personalized recipes based on your ingredients."
    },
    {
      number: "03",
      title: "Start Cooking",
      description: "Follow the step-by-step instructions and enjoy your delicious meal!"
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#FAFAFA] to-[#F0F8FF] font-nunito">
      {/* Header */}
      <header className="bg-white shadow-sm sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between max-w-6xl">
          <div className="flex items-center gap-3">
            <ChefHat className="w-8 h-8 text-[#66BB6A]" />
            <h1 className="text-2xl font-bold text-gray-800">ShelfChef</h1>
          </div>
          <Button 
            onClick={handleGetStarted}
            className="bg-[#66BB6A] hover:bg-[#5aa85a] text-white px-6 py-2 rounded-lg font-semibold transition-all duration-300 transform hover:scale-105"
          >
            Try Now
          </Button>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-20 relative overflow-hidden">
        <div className="container mx-auto px-4 text-center max-w-6xl">
          <div className="relative z-10">
            <Badge className="bg-[#66BB6A] text-white px-4 py-2 text-sm font-semibold mb-6 animate-pulse">
              ✨ Smart Recipe Generation
            </Badge>
            
            <h1 className="text-6xl font-bold text-gray-800 mb-6 leading-tight">
              Turn Your 
              <span className="text-[#66BB6A]"> Ingredients</span><br />
              Into Amazing 
              <span className="text-[#FF7043]"> Recipes</span>
            </h1>
            
            <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto leading-relaxed">
              Stop staring at your fridge wondering what to cook. ShelfChef instantly creates personalized recipes based on ingredients you already have at home.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
              <Button 
                onClick={handleGetStarted}
                className="bg-[#66BB6A] hover:bg-[#5aa85a] text-white px-8 py-4 rounded-xl text-lg font-semibold transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl"
              >
                Get Started Free
                <ArrowRight className="ml-2 w-5 h-5" />
              </Button>
              
              <Button 
                variant="outline" 
                className="border-2 border-[#66BB6A] text-[#66BB6A] hover:bg-[#66BB6A] hover:text-white px-8 py-4 rounded-xl text-lg font-semibold transition-all duration-300"
              >
                See How It Works
              </Button>
            </div>
            
            <div className="flex items-center justify-center gap-8 text-gray-600">
              <div className="flex items-center gap-2">
                <CheckCircle className="w-5 h-5 text-green-500" />
                <span className="text-sm">No Registration Required</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckCircle className="w-5 h-5 text-green-500" />
                <span className="text-sm">100% Free</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckCircle className="w-5 h-5 text-green-500" />
                <span className="text-sm">Instant Results</span>
              </div>
            </div>
          </div>
        </div>
        
        {/* Background decorative elements */}
        <div className="absolute top-10 left-10 w-20 h-20 bg-[#66BB6A] rounded-full opacity-10 animate-pulse"></div>
        <div className="absolute bottom-10 right-10 w-32 h-32 bg-[#FF7043] rounded-full opacity-10 animate-pulse"></div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-white">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-800 mb-4">
              Why Choose ShelfChef?
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              We make cooking easier, faster, and more enjoyable with intelligent recipe suggestions.
            </p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <Card key={index} className="bg-white border-0 shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105 rounded-2xl overflow-hidden">
                <CardHeader className="text-center p-8">
                  <div className="mx-auto mb-4 p-4 bg-gray-50 rounded-full w-20 h-20 flex items-center justify-center">
                    {feature.icon}
                  </div>
                  <Badge className="bg-[#66BB6A] text-white px-3 py-1 text-xs font-semibold mb-4">
                    {feature.highlight}
                  </Badge>
                  <CardTitle className="text-xl font-bold text-gray-800 mb-2">
                    {feature.title}
                  </CardTitle>
                  <CardDescription className="text-gray-600 text-base leading-relaxed">
                    {feature.description}
                  </CardDescription>
                </CardHeader>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="py-20 bg-gradient-to-r from-[#66BB6A] to-[#5aa85a]">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-white mb-4">
              How It Works
            </h2>
            <p className="text-xl text-green-100 max-w-2xl mx-auto">
              Three simple steps to transform your ingredients into delicious meals.
            </p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            {steps.map((step, index) => (
              <div key={index} className="text-center relative">
                <div className="bg-white rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-6 shadow-lg">
                  <span className="text-2xl font-bold text-[#66BB6A]">{step.number}</span>
                </div>
                <h3 className="text-xl font-bold text-white mb-4">{step.title}</h3>
                <p className="text-green-100 leading-relaxed">{step.description}</p>
                
                {index < steps.length - 1 && (
                  <div className="hidden md:block absolute top-8 left-full w-full">
                    <ArrowRight className="w-8 h-8 text-green-200 mx-auto" />
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* App Preview Section */}
      <section className="py-20 bg-white">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-800 mb-4">
              See ShelfChef in Action
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Experience the magic of turning everyday ingredients into extraordinary meals.
            </p>
          </div>
          
          <div className="bg-gradient-to-br from-[#66BB6A] to-[#5aa85a] rounded-3xl p-8 shadow-2xl">
            <div className="bg-white rounded-2xl p-8 shadow-xl">
              <div className="text-center mb-8">
                <div className="flex items-center justify-center gap-3 mb-4">
                  <ChefHat className="w-10 h-10 text-[#66BB6A]" />
                  <h3 className="text-3xl font-bold text-gray-800">Try It Now</h3>
                </div>
                <p className="text-gray-600">Enter some ingredients and see the magic happen!</p>
              </div>
              
              <div className="max-w-2xl mx-auto">
                <div className="bg-[#FAFAFA] rounded-xl p-6 mb-6">
                  <label className="block text-lg font-semibold text-gray-700 mb-3">
                    What's in your kitchen?
                  </label>
                  <div className="bg-white rounded-lg p-4 border-2 border-gray-200 min-h-[100px] flex items-center">
                    <span className="text-gray-500 text-lg">
                      e.g., chicken, tomato, rice, onion, garlic, cheese...
                    </span>
                  </div>
                </div>
                
                <Button 
                  onClick={handleGetStarted}
                  className="w-full bg-[#66BB6A] hover:bg-[#5aa85a] text-white font-semibold py-4 px-8 rounded-xl text-lg transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl"
                >
                  Get Recipes Now
                  <ArrowRight className="ml-2 w-5 h-5" />
                </Button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="py-20 bg-[#FAFAFA]">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-800 mb-4">
              What Our Users Say
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Join thousands of happy home cooks who've transformed their cooking experience.
            </p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <Card key={index} className="bg-white border-0 shadow-lg hover:shadow-xl transition-all duration-300 rounded-2xl overflow-hidden">
                <CardHeader className="text-center p-8">
                  <img 
                    src={testimonial.image} 
                    alt={testimonial.name}
                    className="w-16 h-16 rounded-full mx-auto mb-4 object-cover"
                  />
                  <div className="flex justify-center mb-4">
                    {[...Array(testimonial.rating)].map((_, i) => (
                      <Star key={i} className="w-5 h-5 text-yellow-400 fill-current" />
                    ))}
                  </div>
                  <CardDescription className="text-gray-600 text-base leading-relaxed mb-4 italic">
                    "{testimonial.quote}"
                  </CardDescription>
                  <div>
                    <p className="font-semibold text-gray-800">{testimonial.name}</p>
                    <p className="text-sm text-gray-500">{testimonial.role}</p>
                  </div>
                </CardHeader>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-20 bg-white">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="grid md:grid-cols-4 gap-8 text-center">
            <div className="p-6">
              <div className="text-4xl font-bold text-[#66BB6A] mb-2">10K+</div>
              <div className="text-gray-600">Recipes Generated</div>
            </div>
            <div className="p-6">
              <div className="text-4xl font-bold text-[#FF7043] mb-2">5K+</div>
              <div className="text-gray-600">Happy Users</div>
            </div>
            <div className="p-6">
              <div className="text-4xl font-bold text-[#E91E63] mb-2">95%</div>
              <div className="text-gray-600">Success Rate</div>
            </div>
            <div className="p-6">
              <div className="text-4xl font-bold text-[#66BB6A] mb-2">30s</div>
              <div className="text-gray-600">Average Response Time</div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-[#66BB6A] to-[#5aa85a]">
        <div className="container mx-auto px-4 text-center max-w-4xl">
          <h2 className="text-4xl font-bold text-white mb-6">
            Ready to Transform Your Cooking?
          </h2>
          <p className="text-xl text-green-100 mb-8 max-w-2xl mx-auto">
            Join thousands of home cooks who've already discovered the joy of cooking with ShelfChef.
          </p>
          <Button 
            onClick={handleGetStarted}
            className="bg-white text-[#66BB6A] hover:bg-gray-100 px-8 py-4 rounded-xl text-lg font-semibold transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl"
          >
            Start Cooking Now
            <ArrowRight className="ml-2 w-5 h-5" />
          </Button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-800 text-white py-12">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center gap-3 mb-4">
                <ChefHat className="w-8 h-8 text-[#66BB6A]" />
                <h3 className="text-xl font-bold">ShelfChef</h3>
              </div>
              <p className="text-gray-400">
                Turn your ingredients into amazing recipes with AI-powered suggestions.
              </p>
            </div>
            
            <div>
              <h4 className="font-semibold mb-4">Product</h4>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">Features</a></li>
                <li><a href="#" className="hover:text-white transition-colors">How It Works</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Recipes</a></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold mb-4">Support</h4>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">Help Center</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Contact Us</a></li>
                <li><a href="#" className="hover:text-white transition-colors">FAQ</a></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold mb-4">Company</h4>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">About</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Blog</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Privacy</a></li>
              </ul>
            </div>
          </div>
          
          <div className="border-t border-gray-700 mt-8 pt-8 text-center text-gray-400">
            <p>&copy; 2025 ShelfChef. Made with ❤️ by Taufiqur Rahman.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;
```

This is a comprehensive landing page! Would you like me to continue with:

1. **ShelfChef.js** (the main app component)
2. **UI Components** (Button, Card, Badge, etc.)
3. **Recipe Generator** (backend logic)
4. **All at once** (complete remaining files)

Which would you prefer next?