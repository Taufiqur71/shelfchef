#!/bin/bash

# ShelfChef Deployment Script
set -e

echo "🚀 Starting ShelfChef deployment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
FRONTEND_DIR="./frontend"
BACKEND_DIR="./backend"
DOCKER_IMAGE="shelfchef-backend"

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if required tools are installed
check_dependencies() {
    print_status "Checking dependencies..."
    
    if ! command -v node &> /dev/null; then
        print_error "Node.js is not installed"
        exit 1
    fi
    
    if ! command -v yarn &> /dev/null; then
        print_error "Yarn is not installed"
        exit 1
    fi
    
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed"
        exit 1
    fi
    
    print_status "All dependencies found ✓"
}

# Deploy frontend
deploy_frontend() {
    print_status "Deploying frontend..."
    
    cd $FRONTEND_DIR
    
    # Install dependencies
    print_status "Installing frontend dependencies..."
    yarn install --frozen-lockfile
    
    # Build application
    print_status "Building frontend..."
    yarn build
    
    # Deploy to Vercel (if configured)
    if command -v vercel &> /dev/null; then
        print_status "Deploying to Vercel..."
        vercel --prod --yes
    else
        print_warning "Vercel CLI not found. Skipping Vercel deployment."
        print_status "Build artifacts available in: $FRONTEND_DIR/build"
    fi
    
    cd ..
}

# Deploy backend
deploy_backend() {
    print_status "Deploying backend..."
    
    cd $BACKEND_DIR
    
    # Build Docker image
    print_status "Building Docker image..."
    docker build -t $DOCKER_IMAGE .
    
    # Tag for registry (if configured)
    if [ ! -z "$DOCKER_REGISTRY" ]; then
        print_status "Tagging for registry..."
        docker tag $DOCKER_IMAGE $DOCKER_REGISTRY/$DOCKER_IMAGE:latest
        docker tag $DOCKER_IMAGE $DOCKER_REGISTRY/$DOCKER_IMAGE:$(git rev-parse --short HEAD)
        
        # Push to registry
        print_status "Pushing to registry..."
        docker push $DOCKER_REGISTRY/$DOCKER_IMAGE:latest
        docker push $DOCKER_REGISTRY/$DOCKER_IMAGE:$(git rev-parse --short HEAD)
    fi
    
    # Deploy to Railway (if configured)
    if command -v railway &> /dev/null; then
        print_status "Deploying to Railway..."
        railway up
    else
        print_warning "Railway CLI not found. Skipping Railway deployment."
    fi
    
    cd ..
}

# Run tests
run_tests() {
    print_status "Running tests..."
    
    # Backend tests
    cd $BACKEND_DIR
    if [ -f "requirements.txt" ]; then
        print_status "Running backend tests..."
        python -m pytest tests/ -v
    fi
    cd ..
    
    # Frontend tests
    cd $FRONTEND_DIR
    if [ -f "package.json" ]; then
        print_status "Running frontend tests..."
        yarn test --coverage --watchAll=false
    fi
    cd ..
}

# Main deployment function
main() {
    print_status "ShelfChef Deployment Started 🍳"
    
    check_dependencies
    
    # Run tests first
    if [ "$1" != "--skip-tests" ]; then
        run_tests
    fi
    
    # Deploy components
    deploy_frontend
    deploy_backend
    
    print_status "🎉 ShelfChef deployment completed successfully!"
    print_status "Frontend: Check your Vercel dashboard"
    print_status "Backend: Check your Railway dashboard"
    print_status "Monitor logs and health checks for any issues"
}

# Run main function
main "$@"