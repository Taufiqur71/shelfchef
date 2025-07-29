# 🍳 Complete ShelfChef File Structure

## 📁 Directory Structure
```
shelfchef/
├── .gitignore
├── README.md
├── .env.example
├── package.json (root)
├── .github/
│   └── workflows/
│       ├── deploy.yml
│       ├── test.yml
│       └── lint.yml
├── frontend/
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── index.css
│   │   ├── components/
│   │   │   ├── LandingPage.js
│   │   │   ├── ShelfChef.js
│   │   │   └── ui/
│   │   │       ├── button.jsx
│   │   │       ├── card.jsx
│   │   │       ├── badge.jsx
│   │   │       ├── textarea.jsx
│   │   │       └── toaster.jsx
│   │   └── hooks/
│   │       └── use-toast.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── vercel.json
├── backend/
│   ├── requirements.txt
│   ├── server.py
│   ├── recipe_generator.py
│   ├── Dockerfile
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_main.py
│   └── .env (create from .env.example)
├── deploy/
│   ├── deploy.sh
│   ├── docker-compose.yml
│   └── railway.toml
└── scripts/
    └── setup-dev.sh
```

## 🔧 Step-by-Step File Creation Guide

### 1. Root Directory Files

#### `.gitignore`
```gitignore
# Dependencies
node_modules/
backend/venv/
backend/__pycache__/

# Environment variables
.env
.env.local
.env.development
.env.production

# Build outputs
frontend/build/
dist/

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# System files
.DS_Store
*.pem

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
coverage/
.nyc_output/

# Deployment
.vercel

# Python
*.pyc
__pycache__/
*.pyo
*.pyd
.Python
build/
develop-eggs/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
.venv/
ENV/
env/
```

#### `README.md`
```markdown
# 🍳 ShelfChef - Smart Recipe Generator

Transform your ingredients into amazing recipes with AI-powered suggestions!

![ShelfChef](https://img.shields.io/badge/ShelfChef-Smart%20Recipe%20Generator-66BB6A?style=for-the-badge)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-5.0-47A248?style=for-the-badge&logo=mongodb)

## 🌟 Features

- **Smart Recipe Generation**: AI-powered recipe suggestions based on your ingredients
- **Beautiful Food Images**: High-quality images for each recipe
- **Recipe Management**: Save and manage your favorite recipes
- **Responsive Design**: Works perfectly on all devices
- **Real-time Matching**: See how well your ingredients match each recipe

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.9+
- MongoDB
- Yarn

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Taufiqur71/shelfchef.git
   cd shelfchef
   ```

2. **Setup Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   cp ../.env.example .env
   uvicorn server:app --reload
   ```

3. **Setup Frontend**
   ```bash
   cd frontend
   yarn install
   yarn start
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 🌐 Live Demo

- **Frontend**: https://shelfchef.vercel.app
- **Backend API**: https://shelfchef-backend.railway.app
- **API Documentation**: https://shelfchef-backend.railway.app/docs

## 🔧 Technologies Used

- **Frontend**: React 19, Tailwind CSS, Lucide Icons
- **Backend**: FastAPI, Python 3.9
- **Database**: MongoDB
- **Deployment**: Vercel (Frontend), Railway (Backend)
- **CI/CD**: GitHub Actions

## 📱 Application Features

### Landing Page
Beautiful landing page with features showcase and call-to-action.

### Smart Recipe Generation
- Enter ingredients you have at home
- Get 2-3 personalized recipe suggestions
- See ingredient match percentages
- View beautiful food images

### Recipe Management
- Save your favorite recipes
- View saved recipes collection
- Delete recipes you no longer want

### Modern UI/UX
- Responsive design for all devices
- Smooth animations and transitions
- Professional color scheme
- Intuitive navigation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Food images from Unsplash and Pexels
- Icons from Lucide React
- UI components inspired by shadcn/ui
- Built with ❤️ using React, FastAPI, and MongoDB

---

Made with ❤️ by [Taufiqur Rahman](https://github.com/Taufiqur71). Happy cooking! 🍳
```

#### `.env.example`
```env
# ShelfChef Environment Variables

# Database Configuration
MONGO_URL=mongodb://localhost:27017
DB_NAME=shelfchef

# Backend Configuration
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

# Frontend Configuration
REACT_APP_BACKEND_URL=http://localhost:8000

# Production URLs (update these for deployment)
REACT_APP_BACKEND_URL_PROD=https://your-backend-url.railway.app
FRONTEND_URL_PROD=https://your-frontend-url.vercel.app

# CI/CD Secrets (set these in GitHub repository secrets)
# VERCEL_TOKEN=your_vercel_token
# VERCEL_ORG_ID=your_vercel_org_id
# VERCEL_PROJECT_ID=your_vercel_project_id
# RAILWAY_TOKEN=your_railway_token
# DOCKER_REGISTRY=your_docker_registry
# SLACK_WEBHOOK=your_slack_webhook_url
```

### 2. Frontend Files

#### `frontend/package.json`
```json
{
  "name": "shelfchef-frontend",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@radix-ui/react-avatar": "^1.1.7",
    "@radix-ui/react-dialog": "^1.1.11",
    "@radix-ui/react-label": "^2.1.4",
    "@radix-ui/react-popover": "^1.1.11",
    "@radix-ui/react-select": "^2.2.2",
    "@radix-ui/react-separator": "^1.1.4",
    "@radix-ui/react-slot": "^1.2.0",
    "@radix-ui/react-toast": "^1.2.11",
    "axios": "^1.8.4",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.507.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-router-dom": "^7.5.1",
    "react-scripts": "5.0.1",
    "tailwind-merge": "^3.2.0",
    "tailwindcss-animate": "^1.0.7"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.17"
  }
}
```

#### `frontend/public/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#66BB6A" />
    <meta name="description" content="Transform your ingredients into amazing recipes with ShelfChef" />
    <title>ShelfChef - Smart Recipe Generator</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700;800;900&display=swap" rel="stylesheet">
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
```

#### `frontend/src/index.js`
```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

#### `frontend/tailwind.config.js`
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)'
      },
      colors: {
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))'
        },
        popover: {
          DEFAULT: 'hsl(var(--popover))',
          foreground: 'hsl(var(--popover-foreground))'
        },
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))'
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))'
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))'
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))'
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))'
        },
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        chart: {
          '1': 'hsl(var(--chart-1))',
          '2': 'hsl(var(--chart-2))',
          '3': 'hsl(var(--chart-3))',
          '4': 'hsl(var(--chart-4))',
          '5': 'hsl(var(--chart-5))'
        }
      },
      keyframes: {
        'accordion-down': {
          from: {
            height: '0'
          },
          to: {
            height: 'var(--radix-accordion-content-height)'
          }
        },
        'accordion-up': {
          from: {
            height: 'var(--radix-accordion-content-height)'
          },
          to: {
            height: '0'
          }
        }
      },
      animation: {
        'accordion-down': 'accordion-down 0.2s ease-out',
        'accordion-up': 'accordion-up 0.2s ease-out'
      }
    }
  },
  plugins: [require("tailwindcss-animate")],
};
```

#### `frontend/postcss.config.js`
```javascript
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

### 3. Backend Files

#### `backend/requirements.txt`
```txt
fastapi==0.110.1
uvicorn==0.25.0
motor==3.3.1
pydantic>=2.6.4
python-dotenv>=1.0.1
python-multipart>=0.0.9
starlette>=0.36.0
```

### 4. CI/CD Files

#### `.github/workflows/deploy.yml`
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

## 🚀 Quick Setup Commands

After creating all files, run these commands:

```bash
# Initialize repository
git init
git add .
git commit -m "Initial ShelfChef application with CI/CD pipeline"

# Add GitHub remote (replace with your repository)
git remote add origin https://github.com/Taufiqur71/shelfchef.git

# Push to GitHub
git branch -M main
git push -u origin main

# Setup frontend
cd frontend
npm install
npm start

# Setup backend (in another terminal)
cd backend
pip install -r requirements.txt
uvicorn server:app --reload
```

## 🔧 Deployment Platforms Setup

1. **Vercel** (Frontend): https://vercel.com
   - Import GitHub repository
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `build`

2. **Railway** (Backend): https://railway.app
   - Import GitHub repository
   - Root Directory: `backend`
   - Start Command: `uvicorn server:app --host 0.0.0.0 --port $PORT`

3. **MongoDB Atlas** (Database): https://mongodb.com/cloud/atlas
   - Create free cluster
   - Get connection string
   - Add to environment variables

## 🔐 GitHub Secrets Required

Add these to your GitHub repository secrets:
- `VERCEL_TOKEN`
- `VERCEL_ORG_ID` 
- `VERCEL_PROJECT_ID`
- `RAILWAY_TOKEN`
- `MONGO_URL`

Your ShelfChef application will be live at:
- **Frontend**: https://shelfchef.vercel.app
- **Backend**: https://shelfchef-backend.railway.app

🍳 Happy cooking with ShelfChef! ✨
```