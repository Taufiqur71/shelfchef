# ✅ ShelfChef Deployment Checklist

## Pre-Deployment Setup

### 📋 Required Accounts
- [ ] GitHub account with repository access
- [ ] Vercel account (free tier available)
- [ ] Railway account (free tier available)
- [ ] MongoDB Atlas account (free tier available)

### 🔑 Required Information
- [ ] GitHub username
- [ ] Repository name (suggest: `shelfchef`)
- [ ] Vercel API token
- [ ] Vercel Organization ID
- [ ] Vercel Project ID
- [ ] Railway API token
- [ ] MongoDB Atlas connection string

## Step-by-Step Deployment

### Step 1: GitHub Repository Setup
- [ ] Create new repository on GitHub
- [ ] Name it `shelfchef`
- [ ] Keep it public (or private if preferred)
- [ ] Don't initialize with README (we have our own)

### Step 2: Push Code to GitHub
```bash
# Run this from your /app directory
cd /app
git init
git add .
git commit -m "Initial ShelfChef application with CI/CD pipeline"
git remote add origin https://github.com/YOUR_USERNAME/shelfchef.git
git branch -M main
git push -u origin main
```
- [ ] Code successfully pushed to GitHub
- [ ] Repository contains all ShelfChef files

### Step 3: Vercel Setup (Frontend)
- [ ] Go to [vercel.com](https://vercel.com) and sign in with GitHub
- [ ] Click "New Project"
- [ ] Import your `shelfchef` repository
- [ ] Configure settings:
  - [ ] Framework: Create React App
  - [ ] Root Directory: `frontend`
  - [ ] Build Command: `yarn build`
  - [ ] Output Directory: `build`
  - [ ] Install Command: `yarn install`
- [ ] Deploy the project
- [ ] Note your deployment URL
- [ ] Go to Settings → General and copy:
  - [ ] Project ID
  - [ ] Team/Organization ID

### Step 4: Get Vercel API Token
- [ ] Go to [vercel.com/account/tokens](https://vercel.com/account/tokens)
- [ ] Click "Create Token"
- [ ] Name: `ShelfChef Deployment`
- [ ] Copy the token (save securely)

### Step 5: Railway Setup (Backend)
- [ ] Go to [railway.app](https://railway.app) and sign in with GitHub
- [ ] Click "New Project"
- [ ] Select "Deploy from GitHub repo"
- [ ] Choose your `shelfchef` repository
- [ ] Configure deployment:
  - [ ] Root Directory: `backend`
  - [ ] Build Command: `pip install -r requirements.txt`
  - [ ] Start Command: `uvicorn server:app --host 0.0.0.0 --port $PORT`
- [ ] Deploy and note the URL
- [ ] Go to Variables tab and add:
  - [ ] `DB_NAME`: `shelfchef`
  - [ ] `PORT`: `8000`

### Step 6: Get Railway API Token
- [ ] Go to [railway.app/account/tokens](https://railway.app/account/tokens)
- [ ] Click "New Token"
- [ ] Name: `ShelfChef Deployment`
- [ ] Copy the token (save securely)

### Step 7: MongoDB Atlas Setup
- [ ] Go to [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
- [ ] Create account and new project: `ShelfChef`
- [ ] Build a cluster (select free tier)
- [ ] Create database user:
  - [ ] Username: `shelfchef`
  - [ ] Password: (generate strong password)
- [ ] Network Access: Add IP `0.0.0.0/0` (or restrict as needed)
- [ ] Get connection string:
  - [ ] Click "Connect" → "Connect your application"
  - [ ] Copy connection string
  - [ ] Replace `<password>` with your password

### Step 8: GitHub Secrets Configuration
Go to: `https://github.com/YOUR_USERNAME/shelfchef/settings/secrets/actions`

Add these secrets (click "New repository secret" for each):

#### Required Secrets:
- [ ] `VERCEL_TOKEN` - Your Vercel API token
- [ ] `VERCEL_ORG_ID` - Your Vercel Organization ID
- [ ] `VERCEL_PROJECT_ID` - Your Vercel Project ID
- [ ] `RAILWAY_TOKEN` - Your Railway API token
- [ ] `MONGO_URL` - Your MongoDB Atlas connection string

#### Optional Secrets:
- [ ] `SLACK_WEBHOOK` - Slack webhook for notifications
- [ ] `DOCKER_REGISTRY` - Docker Hub username (for custom registry)

### Step 9: Update Environment Variables

#### Update Railway Environment Variables:
- [ ] Go to Railway project dashboard
- [ ] Click on backend service
- [ ] Go to "Variables" tab
- [ ] Update `MONGO_URL` with your MongoDB Atlas connection string

#### Update Vercel Environment Variables:
- [ ] Go to Vercel project dashboard
- [ ] Go to "Settings" → "Environment Variables"
- [ ] Add: `REACT_APP_BACKEND_URL` = `[Your Railway backend URL]`

### Step 10: Test Deployment Pipeline
```bash
# Make a small change to trigger deployment
echo "# ShelfChef - Smart Recipe Generator" > README.md
git add README.md
git commit -m "Test CI/CD pipeline"
git push origin main
```

- [ ] GitHub Actions workflow triggered
- [ ] All tests passed
- [ ] Frontend deployed to Vercel
- [ ] Backend deployed to Railway
- [ ] No errors in deployment logs

## Verification Checklist

### ✅ Frontend Verification
- [ ] Visit your Vercel deployment URL
- [ ] Landing page loads correctly
- [ ] Navigation to app works
- [ ] App interface loads without errors
- [ ] Responsive design works on mobile

### ✅ Backend Verification
- [ ] Visit `[Railway URL]/api/health` returns healthy status
- [ ] Visit `[Railway URL]/api/` returns welcome message
- [ ] API documentation accessible at `[Railway URL]/docs`
- [ ] No 500 errors in logs

### ✅ Full Application Testing
- [ ] Open frontend URL
- [ ] Enter test ingredients: "chicken, tomato, rice, onion"
- [ ] Click "Get Recipes"
- [ ] Recipes generate successfully
- [ ] Food images display correctly
- [ ] Recipe cards show ingredient matches
- [ ] Save recipe functionality works
- [ ] Saved recipes view works
- [ ] All animations and transitions smooth

### ✅ Database Verification
- [ ] Recipes save to MongoDB Atlas
- [ ] Saved recipes retrieve correctly
- [ ] Recipe deletion works
- [ ] No database connection errors

## Post-Deployment Setup

### 🌐 Custom Domain (Optional)
- [ ] Purchase domain name
- [ ] Configure DNS settings
- [ ] Add domain to Vercel (frontend)
- [ ] Add domain to Railway (backend)
- [ ] Update environment variables
- [ ] Test with custom domain

### 📊 Monitoring Setup
- [ ] Set up Vercel Analytics
- [ ] Configure Railway metrics
- [ ] Set up error tracking
- [ ] Configure uptime monitoring
- [ ] Set up performance monitoring

### 🔔 Notifications
- [ ] Set up Slack notifications (if desired)
- [ ] Configure email alerts
- [ ] Set up deployment status badges

## Troubleshooting

### Common Issues:
- [ ] **Build Fails**: Check GitHub Actions logs, verify secrets
- [ ] **API Connection**: Verify CORS settings and backend URL
- [ ] **Database Issues**: Check MongoDB connection string and IP whitelist
- [ ] **Environment Variables**: Ensure all variables are set correctly

### Debug Commands:
```bash
# Test backend health
curl https://your-backend-url.railway.app/api/health

# Test recipe generation
curl -X POST https://your-backend-url.railway.app/api/generate-recipes \
  -H "Content-Type: application/json" \
  -d '{"ingredients": "chicken, rice"}'
```

## Success Metrics

### ✅ Deployment Success:
- [ ] GitHub Actions shows ✅ green checkmarks
- [ ] Vercel shows "Ready" status
- [ ] Railway shows "Active" status
- [ ] MongoDB Atlas shows "Connected"

### ✅ Application Performance:
- [ ] Frontend loads < 3 seconds
- [ ] Recipe generation < 2 seconds
- [ ] API response time < 500ms
- [ ] No console errors
- [ ] 100% uptime

### ✅ User Experience:
- [ ] Intuitive interface
- [ ] Fast recipe generation
- [ ] Beautiful food images
- [ ] Smooth animations
- [ ] Mobile responsive

## 🎉 Completion

When all items are checked:
- [ ] **Application is live and functional**
- [ ] **CI/CD pipeline is working**
- [ ] **Automated deployments configured**
- [ ] **Monitoring is in place**
- [ ] **Documentation is complete**

## 📱 Your Live URLs:
- **Frontend**: `https://shelfchef.vercel.app`
- **Backend**: `https://shelfchef-backend.railway.app`
- **API Docs**: `https://shelfchef-backend.railway.app/docs`

**🍳 Congratulations! ShelfChef is now live and automatically deployed! ✨**