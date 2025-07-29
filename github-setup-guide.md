# 🚀 ShelfChef GitHub Repository Setup Guide

## Step 1: Create GitHub Repository

### 1.1 Create New Repository
1. Go to [GitHub](https://github.com) and sign in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name:** `shelfchef`
   - **Description:** `Smart Recipe Generator - Transform your ingredients into amazing recipes`
   - **Visibility:** Public (or Private if you prefer)
   - **Initialize with:** Don't check any boxes (we'll add our code)
5. Click **"Create repository"**

### 1.2 Clone and Push Your Code
```bash
# Navigate to your ShelfChef directory
cd /app

# Initialize git repository
git init

# Add all files
git add .

# Commit the initial code
git commit -m "Initial ShelfChef application with CI/CD pipeline"

# Add your GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/shelfchef.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 2: Set Up Deployment Platforms

### 2.1 Vercel Setup (Frontend)
1. Go to [Vercel](https://vercel.com) and sign in with GitHub
2. Click **"New Project"**
3. Import your `shelfchef` repository
4. Configure project settings:
   - **Framework Preset:** Create React App
   - **Root Directory:** `frontend`
   - **Build Command:** `yarn build`
   - **Output Directory:** `build`
   - **Install Command:** `yarn install`
5. Click **"Deploy"**
6. After deployment, go to **Settings → General** and note down:
   - **Project ID** (in URL or settings)
   - **Team ID** (in team settings)

### 2.2 Get Vercel API Token
1. Go to [Vercel Account Settings](https://vercel.com/account/tokens)
2. Click **"Create Token"**
3. Name it: `ShelfChef Deployment`
4. Set expiration as needed
5. Copy the token (save it securely)

### 2.3 Railway Setup (Backend)
1. Go to [Railway](https://railway.app) and sign in with GitHub
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your `shelfchef` repository
5. Configure deployment:
   - **Root Directory:** `backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn server:app --host 0.0.0.0 --port $PORT`
6. Add environment variables:
   - `MONGO_URL`: `mongodb://localhost:27017` (we'll update this later)
   - `DB_NAME`: `shelfchef`
   - `PORT`: `8000`
7. Deploy and note the deployment URL

### 2.4 Get Railway API Token
1. Go to [Railway Account Settings](https://railway.app/account/tokens)
2. Click **"New Token"**
3. Name it: `ShelfChef Deployment`
4. Copy the token (save it securely)

### 2.5 MongoDB Atlas Setup (Database)
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create account
2. Create a new project: `ShelfChef`
3. Build a cluster (choose the free tier)
4. Create database user:
   - Username: `shelfchef`
   - Password: Generate strong password
5. Add IP addresses to whitelist: `0.0.0.0/0` (allow all - or restrict as needed)
6. Get connection string:
   - Click **"Connect"** → **"Connect your application"**
   - Copy connection string, replace `<password>` with your password

## Step 3: Configure GitHub Secrets

### 3.1 Add Repository Secrets
1. Go to your GitHub repository
2. Click **"Settings"** tab
3. Click **"Secrets and variables"** → **"Actions"**
4. Click **"New repository secret"** for each:

### 3.2 Required Secrets

#### Frontend (Vercel):
```
Name: VERCEL_TOKEN
Value: [Your Vercel API token from step 2.2]

Name: VERCEL_ORG_ID
Value: [Your Vercel Team ID from step 2.1]

Name: VERCEL_PROJECT_ID
Value: [Your Vercel Project ID from step 2.1]
```

#### Backend (Railway):
```
Name: RAILWAY_TOKEN
Value: [Your Railway API token from step 2.4]

Name: DOCKER_REGISTRY
Value: [Your Docker Hub username]/shelfchef (optional)
```

#### Database:
```
Name: MONGO_URL
Value: [Your MongoDB Atlas connection string from step 2.5]
```

#### Optional (Notifications):
```
Name: SLACK_WEBHOOK
Value: [Your Slack webhook URL - optional]
```

## Step 4: Update Environment Variables

### 4.1 Update Railway Environment Variables
1. Go to your Railway project dashboard
2. Click on your backend service
3. Go to **"Variables"** tab
4. Update the `MONGO_URL` with your MongoDB Atlas connection string

### 4.2 Update Vercel Environment Variables
1. Go to your Vercel project dashboard
2. Go to **"Settings"** → **"Environment Variables"**
3. Add:
   ```
   REACT_APP_BACKEND_URL = [Your Railway backend URL]
   ```

## Step 5: Test the Deployment Pipeline

### 5.1 Trigger Deployment
```bash
# Make a small change to test the pipeline
echo "# ShelfChef - Smart Recipe Generator" > README.md
git add README.md
git commit -m "Test CI/CD pipeline"
git push origin main
```

### 5.2 Monitor Deployment
1. Go to GitHub → Your repository → **"Actions"** tab
2. Watch the deployment workflow run
3. Check the logs for any errors
4. Verify deployment status in Vercel and Railway dashboards

## Step 6: Verify Deployment

### 6.1 Check Frontend
1. Visit your Vercel deployment URL
2. Test the landing page
3. Test navigation to the app
4. Test recipe generation functionality

### 6.2 Check Backend
1. Visit your Railway deployment URL + `/api/health`
2. Should return: `{"status": "healthy", "service": "ShelfChef API"}`
3. Test API endpoints:
   - `GET /api/` - Should return welcome message
   - `POST /api/generate-recipes` - Test recipe generation

### 6.3 Test Full Application
1. Go to your live frontend URL
2. Enter ingredients: "chicken, tomato, rice, onion"
3. Click "Get Recipes"
4. Verify recipes are generated with food images
5. Test saving recipes
6. Test saved recipes view

## Step 7: Custom Domain (Optional)

### 7.1 Frontend Custom Domain
1. In Vercel dashboard, go to **"Settings"** → **"Domains"**
2. Add your custom domain (e.g., `shelfchef.com`)
3. Follow DNS setup instructions

### 7.2 Backend Custom Domain
1. In Railway dashboard, go to **"Settings"** → **"Domains"**
2. Add your custom domain (e.g., `api.shelfchef.com`)
3. Update frontend environment variable to use new domain

## 🎉 Deployment URLs

After successful setup, your application will be available at:

### Live URLs:
- **Frontend:** `https://shelfchef.vercel.app` (or your custom domain)
- **Backend API:** `https://shelfchef-backend.railway.app` (or your custom domain)
- **API Documentation:** `https://shelfchef-backend.railway.app/docs`

### GitHub Actions Status:
- **Workflow Status:** GitHub → Actions tab
- **Deploy Status:** ✅ Success badges in README

## 🛠️ Troubleshooting

### Common Issues:

1. **Build Fails:**
   - Check GitHub Actions logs
   - Verify all secrets are set correctly
   - Check environment variables

2. **API Connection Issues:**
   - Verify `REACT_APP_BACKEND_URL` in Vercel
   - Check CORS settings
   - Verify Railway deployment is running

3. **Database Connection:**
   - Check MongoDB Atlas connection string
   - Verify IP whitelist settings
   - Check database user permissions

### Debug Commands:
```bash
# Check deployment status
curl -f https://your-backend-url.railway.app/api/health

# Test recipe generation
curl -X POST https://your-backend-url.railway.app/api/generate-recipes \
  -H "Content-Type: application/json" \
  -d '{"ingredients": "chicken, rice"}'
```

## 🔄 Future Updates

To deploy updates:
```bash
# Make changes to your code
git add .
git commit -m "Add new feature"
git push origin main

# GitHub Actions will automatically:
# 1. Run tests
# 2. Build applications
# 3. Deploy to production
# 4. Send notifications
```

---

**Your ShelfChef application is now live and automatically deployed! 🍳✨**

**Need help with any step? Let me know and I'll guide you through it!**