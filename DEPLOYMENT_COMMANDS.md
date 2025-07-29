# 🚀 ShelfChef Deployment Commands for Taufiqur71

## Step 1: Create GitHub Repository
1. Go to: https://github.com/new
2. Repository name: `shelfchef`
3. Description: `Smart Recipe Generator - Transform your ingredients into amazing recipes`
4. Make it **Public**
5. **Don't initialize** with README, .gitignore, or license
6. Click **"Create repository"**

## Step 2: Clone and Set Up Repository
Run these commands in your terminal:

```bash
# Clone the repository you just created
git clone https://github.com/Taufiqur71/shelfchef.git
cd shelfchef

# The repository will be empty, so we'll add all the ShelfChef files
```

## Step 3: Download ShelfChef Files
Since you're working in a development environment, you'll need to download the complete ShelfChef application files.

**Option A: Download individual files**
I'll provide you with the key files you need to create.

**Option B: Copy from current environment**
If you have access to the current environment, copy all files from `/app/` to your local `shelfchef` directory.

## Step 4: Essential Files to Create

### Create package.json for frontend:
```bash
mkdir -p frontend
cd frontend
```

Create `package.json`:
```json
{
  "name": "shelfchef-frontend",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@radix-ui/react-avatar": "^1.1.7",
    "@radix-ui/react-dialog": "^1.1.11",
    "@radix-ui/react-dropdown-menu": "^2.1.12",
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
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
  },
  "devDependencies": {
    "@craco/craco": "^7.1.0",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.17"
  }
}
```

### Create requirements.txt for backend:
```bash
cd ../backend
```

Create `requirements.txt`:
```txt
fastapi==0.110.1
uvicorn==0.25.0
motor==3.3.1
pydantic>=2.6.4
python-dotenv>=1.0.1
python-multipart>=0.0.9
starlette>=0.36.0
```

## Step 5: Push to GitHub
After creating all the files:

```bash
# Go back to root directory
cd ..

# Add all files
git add .

# Commit
git commit -m "Initial ShelfChef application with CI/CD pipeline"

# Push to GitHub
git push -u origin main
```

## Step 6: Set Up Deployment Platforms

### Vercel Setup (Frontend)
1. Go to https://vercel.com
2. Sign in with GitHub
3. Import your `shelfchef` repository
4. Configure:
   - Framework: Create React App
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `build`
5. Deploy

### Railway Setup (Backend)
1. Go to https://railway.app
2. Sign in with GitHub
3. Create new project from GitHub
4. Select your `shelfchef` repository
5. Configure:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn server:app --host 0.0.0.0 --port $PORT`
6. Deploy

### MongoDB Atlas Setup
1. Go to https://mongodb.com/cloud/atlas
2. Create free cluster
3. Get connection string
4. Add to Railway environment variables

## Step 7: Configure GitHub Secrets
Add these secrets to your GitHub repository:
- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`
- `RAILWAY_TOKEN`
- `MONGO_URL`

## Need Help?
If you need the complete files, let me know and I can provide them individually or guide you through the process step by step.

Repository URL: https://github.com/Taufiqur71/shelfchef