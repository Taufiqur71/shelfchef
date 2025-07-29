# 🍳 ShelfChef - Smart Recipe Generator

Transform your ingredients into amazing recipes with AI-powered suggestions!

![ShelfChef](https://img.shields.io/badge/ShelfChef-Smart%20Recipe%20Generator-66BB6A?style=for-the-badge)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-5.0-47A248?style=for-the-badge&logo=mongodb)

ShelfChef is a modern web application that transforms your available ingredients into delicious recipes using intelligent algorithms. Built with React, FastAPI, and MongoDB.

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
   git clone https://github.com/yourusername/shelfchef.git
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

## 🔧 Production Deployment

### Automated Deployment (CI/CD)

1. **Fork this repository**
2. **Set up deployment secrets in GitHub**:
   - `VERCEL_TOKEN`: Your Vercel API token
   - `VERCEL_ORG_ID`: Your Vercel organization ID
   - `VERCEL_PROJECT_ID`: Your Vercel project ID
   - `RAILWAY_TOKEN`: Your Railway API token
   - `DOCKER_REGISTRY`: Your Docker registry URL
   - `SLACK_WEBHOOK`: (Optional) Slack webhook for notifications

3. **Push to main branch**
   ```bash
   git push origin main
   ```

4. **Automatic deployment will trigger**:
   - Tests run automatically
   - Frontend deploys to Vercel
   - Backend deploys to Railway
   - Database sets up on MongoDB Atlas

### Manual Deployment

1. **Using the deployment script**:
   ```bash
   chmod +x deploy/deploy.sh
   ./deploy/deploy.sh
   ```

2. **Using Docker**:
   ```bash
   cd backend
   docker build -t shelfchef-backend .
   docker run -p 8000:8000 shelfchef-backend
   ```

3. **Using Docker Compose**:
   ```bash
   cd backend
   docker-compose up -d
   ```

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
yarn test
```

### End-to-End Tests
```bash
yarn test:e2e
```

## 📁 Project Structure

```
shelfchef/
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── hooks/          # Custom hooks
│   │   └── mock/           # Mock data
│   ├── public/             # Static assets
│   └── vercel.json         # Vercel configuration
├── backend/                # FastAPI backend
│   ├── server.py           # Main server file
│   ├── recipe_generator.py # Recipe generation logic
│   ├── tests/              # Backend tests
│   ├── Dockerfile          # Docker configuration
│   └── requirements.txt    # Python dependencies
├── .github/workflows/      # CI/CD workflows
├── deploy/                 # Deployment scripts
└── README.md              # This file
```

## 🌐 API Endpoints

### Recipe Generation
- `POST /api/generate-recipes` - Generate recipes from ingredients
- `GET /api/saved-recipes` - Get saved recipes
- `POST /api/save-recipe` - Save a recipe
- `DELETE /api/saved-recipes/{id}` - Delete a recipe

### Utility
- `GET /api/health` - Health check
- `GET /api/` - API status

## 🔒 Environment Variables

Create a `.env` file in both frontend and backend directories:

```bash
# Backend (.env)
MONGO_URL=mongodb://localhost:27017
DB_NAME=shelfchef

# Frontend (.env)
REACT_APP_BACKEND_URL=http://localhost:8000
```

## 🚀 Deployment Platforms

### Supported Platforms
- **Frontend**: Vercel, Netlify, AWS S3 + CloudFront
- **Backend**: Railway, Heroku, AWS ECS, Google Cloud Run
- **Database**: MongoDB Atlas, AWS DocumentDB

### Platform-Specific Guides
- [Vercel Deployment](docs/vercel-deployment.md)
- [Railway Deployment](docs/railway-deployment.md)
- [AWS Deployment](docs/aws-deployment.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Monitoring & Analytics

### Health Checks
- Backend: `GET /api/health`
- Frontend: Built-in Vercel monitoring

### Logging
- Backend: FastAPI structured logging
- Frontend: Console logging in development

### Performance Monitoring
- Vercel Analytics for frontend
- Railway metrics for backend

## 🛠️ Development Tools

### Recommended VSCode Extensions
- Python
- ES7+ React/Redux/React-Native snippets
- Thunder Client (API testing)
- Docker
- GitLens

### Code Quality
- ESLint + Prettier for frontend
- Black + isort for backend
- Pre-commit hooks (optional)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Food images from Unsplash and Pexels
- Icons from Lucide React
- UI components from shadcn/ui
- Built with ❤️ using React, FastAPI, and MongoDB

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/shelfchef/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/shelfchef/discussions)
- **Email**: support@shelfchef.com

---

Made with ❤️ by the ShelfChef team. Happy cooking! 🍳