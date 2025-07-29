#!/bin/bash

# ShelfChef Development Setup Script
set -e

echo "🍳 Setting up ShelfChef development environment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running on supported OS
check_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "msys" ]]; then
        OS="windows"
    else
        print_error "Unsupported operating system: $OSTYPE"
        exit 1
    fi
    print_status "Detected OS: $OS"
}

# Install system dependencies
install_dependencies() {
    print_status "Installing system dependencies..."
    
    if [[ "$OS" == "linux" ]]; then
        # Ubuntu/Debian
        if command -v apt-get &> /dev/null; then
            sudo apt-get update
            sudo apt-get install -y curl wget git python3 python3-pip nodejs npm
        # CentOS/RHEL
        elif command -v yum &> /dev/null; then
            sudo yum install -y curl wget git python3 python3-pip nodejs npm
        fi
    elif [[ "$OS" == "macos" ]]; then
        # macOS with Homebrew
        if ! command -v brew &> /dev/null; then
            print_error "Homebrew not found. Please install Homebrew first:"
            print_error "https://brew.sh/"
            exit 1
        fi
        brew install python3 node git
    fi
}

# Install Node.js and Yarn
setup_nodejs() {
    print_status "Setting up Node.js environment..."
    
    # Install yarn if not present
    if ! command -v yarn &> /dev/null; then
        npm install -g yarn
    fi
    
    # Verify versions
    node --version
    yarn --version
}

# Install Python dependencies
setup_python() {
    print_status "Setting up Python environment..."
    
    # Create virtual environment
    if [ ! -d "backend/venv" ]; then
        cd backend
        python3 -m venv venv
        cd ..
    fi
    
    # Activate virtual environment and install dependencies
    cd backend
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install pytest pytest-asyncio httpx  # Development dependencies
    cd ..
}

# Setup MongoDB
setup_mongodb() {
    print_status "Setting up MongoDB..."
    
    if ! command -v mongod &> /dev/null; then
        if [[ "$OS" == "linux" ]]; then
            # Ubuntu/Debian
            wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
            echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
            sudo apt-get update
            sudo apt-get install -y mongodb-org
        elif [[ "$OS" == "macos" ]]; then
            brew tap mongodb/brew
            brew install mongodb-community@5.0
        fi
    fi
    
    # Start MongoDB service
    if [[ "$OS" == "linux" ]]; then
        sudo systemctl start mongod
        sudo systemctl enable mongod
    elif [[ "$OS" == "macos" ]]; then
        brew services start mongodb/brew/mongodb-community
    fi
}

# Setup frontend
setup_frontend() {
    print_status "Setting up frontend..."
    
    cd frontend
    yarn install
    cd ..
}

# Create environment files
setup_environment() {
    print_status "Setting up environment variables..."
    
    # Copy example environment files
    if [ ! -f ".env" ]; then
        cp .env.example .env
        print_warning "Created .env file. Please update the values as needed."
    fi
    
    if [ ! -f "backend/.env" ]; then
        cp .env.example backend/.env
        print_warning "Created backend/.env file. Please update the values as needed."
    fi
    
    if [ ! -f "frontend/.env" ]; then
        echo "REACT_APP_BACKEND_URL=http://localhost:8000" > frontend/.env
        print_status "Created frontend/.env file."
    fi
}

# Setup Git hooks
setup_git_hooks() {
    print_status "Setting up Git hooks..."
    
    # Install pre-commit hooks
    if command -v pre-commit &> /dev/null; then
        pre-commit install
    else
        print_warning "pre-commit not found. Consider installing it for better code quality."
    fi
}

# Test the setup
test_setup() {
    print_status "Testing the setup..."
    
    # Test backend
    cd backend
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        python -m pytest tests/ -v || print_warning "Backend tests failed"
    fi
    cd ..
    
    # Test frontend build
    cd frontend
    yarn build || print_warning "Frontend build failed"
    cd ..
}

# Main setup function
main() {
    print_status "Starting ShelfChef development setup..."
    
    check_os
    install_dependencies
    setup_nodejs
    setup_python
    setup_mongodb
    setup_frontend
    setup_environment
    setup_git_hooks
    test_setup
    
    print_status "🎉 ShelfChef development environment setup complete!"
    print_status ""
    print_status "Next steps:"
    print_status "1. Update .env files with your configuration"
    print_status "2. Start the backend: cd backend && source venv/bin/activate && uvicorn server:app --reload"
    print_status "3. Start the frontend: cd frontend && yarn start"
    print_status "4. Open http://localhost:3000 in your browser"
    print_status ""
    print_status "Happy coding! 🍳"
}

# Run main function
main "$@"