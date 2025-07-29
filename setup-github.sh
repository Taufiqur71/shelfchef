#!/bin/bash

# ShelfChef GitHub Setup Script
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}🍳 ShelfChef GitHub Setup${NC}"
    echo -e "${BLUE}================================${NC}"
    echo ""
}

print_status() {
    echo -e "${GREEN}[✅]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[ℹ️]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[⚠️]${NC} $1"
}

print_error() {
    echo -e "${RED}[❌]${NC} $1"
}

print_step() {
    echo -e "${YELLOW}[STEP]${NC} $1"
}

# Function to prompt for user input
prompt_user() {
    echo -e "${BLUE}$1${NC}"
    read -p "Enter $2: " value
    echo "$value"
}

# Function to prompt for secret input
prompt_secret() {
    echo -e "${BLUE}$1${NC}"
    read -s -p "Enter $2: " value
    echo ""
    echo "$value"
}

print_header

print_step "1. Repository Setup"
print_info "First, let's collect your GitHub repository information"

# Get repository information
GITHUB_USERNAME=$(prompt_user "What's your GitHub username?" "username")
REPO_NAME=$(prompt_user "What do you want to name your repository? (default: shelfchef)" "repository name")
REPO_NAME=${REPO_NAME:-shelfchef}

print_info "Repository will be: https://github.com/$GITHUB_USERNAME/$REPO_NAME"

# Initialize git repository
print_step "2. Initializing Git Repository"
if [ ! -d ".git" ]; then
    git init
    print_status "Git repository initialized"
else
    print_warning "Git repository already exists"
fi

# Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
    cat > .gitignore << EOF
# Environment variables
.env
.env.local
.env.development
.env.production

# Dependencies
node_modules/
backend/venv/
backend/__pycache__/
frontend/build/

# Logs
*.log
logs/

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
coverage/
.nyc_output/

# Temporary files
*.tmp
*.temp
EOF
    print_status "Created .gitignore file"
fi

# Add all files
print_step "3. Adding Files to Git"
git add .
git commit -m "Initial ShelfChef application with CI/CD pipeline"
print_status "Files committed to Git"

# Add remote origin
print_step "4. Adding GitHub Remote"
git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git
git branch -M main
print_status "GitHub remote added"

print_warning "⚠️  Before pushing, make sure you've created the repository on GitHub!"
print_info "Go to https://github.com/new and create a repository named: $REPO_NAME"
read -p "Press Enter when you've created the repository on GitHub..."

# Push to GitHub
print_step "5. Pushing to GitHub"
git push -u origin main
print_status "Code pushed to GitHub successfully!"

print_step "6. Platform Configuration"
print_info "Now let's collect your deployment platform information"

# Vercel setup
print_info "📱 Vercel Setup (Frontend)"
print_info "1. Go to https://vercel.com and sign in with GitHub"
print_info "2. Import your $REPO_NAME repository"
print_info "3. Set Root Directory to: frontend"
print_info "4. Deploy the project"
print_info "5. Go to Settings → General to find your Project ID and Team ID"

read -p "Press Enter when you've set up Vercel..."

VERCEL_TOKEN=$(prompt_secret "Enter your Vercel API token (from https://vercel.com/account/tokens)" "Vercel token")
VERCEL_ORG_ID=$(prompt_user "Enter your Vercel Organization/Team ID" "Vercel Org ID")
VERCEL_PROJECT_ID=$(prompt_user "Enter your Vercel Project ID" "Vercel Project ID")

# Railway setup
print_info "🚂 Railway Setup (Backend)"
print_info "1. Go to https://railway.app and sign in with GitHub"
print_info "2. Create new project from GitHub repo"
print_info "3. Select your $REPO_NAME repository"
print_info "4. Set Root Directory to: backend"
print_info "5. Deploy the project"

read -p "Press Enter when you've set up Railway..."

RAILWAY_TOKEN=$(prompt_secret "Enter your Railway API token (from https://railway.app/account/tokens)" "Railway token")

# MongoDB Atlas setup
print_info "🍃 MongoDB Atlas Setup (Database)"
print_info "1. Go to https://www.mongodb.com/cloud/atlas"
print_info "2. Create a new project: ShelfChef"
print_info "3. Build a cluster (free tier)"
print_info "4. Create database user and get connection string"

read -p "Press Enter when you've set up MongoDB Atlas..."

MONGO_URL=$(prompt_secret "Enter your MongoDB Atlas connection string" "MongoDB URL")

# Create secrets file for reference
print_step "7. Creating Secrets Reference"
cat > github-secrets.txt << EOF
# GitHub Secrets Configuration
# Add these secrets to your GitHub repository:
# Settings → Secrets and variables → Actions → New repository secret

VERCEL_TOKEN=$VERCEL_TOKEN
VERCEL_ORG_ID=$VERCEL_ORG_ID
VERCEL_PROJECT_ID=$VERCEL_PROJECT_ID
RAILWAY_TOKEN=$RAILWAY_TOKEN
MONGO_URL=$MONGO_URL

# Optional:
# SLACK_WEBHOOK=your_slack_webhook_url
# DOCKER_REGISTRY=your_docker_hub_username
EOF

print_status "Secrets saved to github-secrets.txt"
print_warning "⚠️  Keep this file secure and don't commit it to Git!"

print_step "8. GitHub Secrets Setup"
print_info "Now you need to add these secrets to your GitHub repository:"
print_info "1. Go to: https://github.com/$GITHUB_USERNAME/$REPO_NAME/settings/secrets/actions"
print_info "2. Click 'New repository secret' for each secret in github-secrets.txt"
print_info "3. Copy the name and value exactly as shown"

read -p "Press Enter when you've added all secrets to GitHub..."

print_step "9. Testing Deployment"
print_info "Let's test the CI/CD pipeline by making a small change"

# Create a test commit
echo "# 🍳 ShelfChef - Smart Recipe Generator

Transform your ingredients into amazing recipes with AI-powered suggestions!

## Features
- Smart recipe generation
- Beautiful food images
- Recipe saving and management
- Responsive design
- Real-time ingredient matching

## Live Demo
- Frontend: [Coming Soon]
- Backend API: [Coming Soon]

Built with React, FastAPI, and MongoDB." > README.md

git add README.md
git commit -m "Add README and test CI/CD pipeline"
git push origin main

print_status "Test commit pushed! Check GitHub Actions for deployment status."

print_step "10. Verification"
print_info "🔍 Verify your deployment:"
print_info "1. GitHub Actions: https://github.com/$GITHUB_USERNAME/$REPO_NAME/actions"
print_info "2. Vercel Dashboard: https://vercel.com/dashboard"
print_info "3. Railway Dashboard: https://railway.app/dashboard"

print_info "Your application URLs will be:"
print_info "• Frontend: https://$REPO_NAME.vercel.app (or your custom domain)"
print_info "• Backend: https://$REPO_NAME-backend.railway.app (or your custom domain)"
print_info "• API Docs: https://$REPO_NAME-backend.railway.app/docs"

print_header
print_status "🎉 ShelfChef GitHub setup complete!"
print_info "Your application is now automatically deployed with CI/CD!"
print_info "Every push to main branch will trigger automatic deployment."
print_info "Check the GitHub Actions tab to monitor deployments."
echo ""
print_warning "📋 Next steps:"
print_info "1. Wait for initial deployment to complete (5-10 minutes)"
print_info "2. Test your live application"
print_info "3. Update environment variables if needed"
print_info "4. Add custom domain (optional)"
print_info "5. Set up monitoring and analytics"
echo ""
print_status "Happy cooking! 🍳✨"