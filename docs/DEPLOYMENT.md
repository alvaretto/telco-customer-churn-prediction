# 🚀 Deployment Guide

Complete guide for deploying the Telco Customer Churn Prediction system.

## 📋 Overview

This project consists of two main components:
1. **Flask API** - Backend prediction service
2. **Streamlit Dashboard** - Interactive frontend

Both can be deployed independently on free cloud platforms.

---

## 🔧 API Deployment (Render)

### Prerequisites
- GitHub account
- Render account (free tier)
- Git repository with your code

### Step-by-Step Deployment

#### 1. Prepare Your Repository

Ensure your repository has:
```
api/
├── app.py
├── requirements.txt
├── Dockerfile (optional)
└── .dockerignore (optional)
models/
├── churn_model.pkl (Git LFS)
├── preprocessor.pkl (Git LFS)
└── metadata.json
```

#### 2. Create Web Service on Render

1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:

**Settings:**
- **Name**: `telco-churn-api` (or your choice)
- **Region**: Choose closest to your users
- **Branch**: `main`
- **Root Directory**: `api`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 60 app:app`

**Environment Variables:**
- `PORT`: (automatically set by Render)
- `PYTHON_VERSION`: `3.10.0`

5. Click "Create Web Service"

#### 3. Wait for Deployment

- First deployment takes 5-10 minutes
- Watch the logs for any errors
- Once deployed, you'll get a URL like: `https://telco-churn-api.onrender.com`

#### 4. Test the API

```bash
# Health check
curl https://your-app.onrender.com/health

# Model info
curl https://your-app.onrender.com/model_info

# Prediction
curl -X POST https://your-app.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d @sample_customer.json
```

### Render Free Tier Limits
- ✅ 512 MB RAM (sufficient for our 65 MB model)
- ✅ Shared CPU
- ⚠️ Spins down after 15 minutes of inactivity
- ⚠️ 750 hours/month free

---

## 📊 Dashboard Deployment (Streamlit Cloud)

### Prerequisites
- GitHub account
- Streamlit Cloud account (free)
- Git repository with your code

### Step-by-Step Deployment

#### 1. Prepare Your Repository

Ensure your repository has:
```
dashboard/
├── app.py
├── pages/
│   ├── 1_📊_Overview.py
│   ├── 2_🎯_Risk_Analysis.py
│   ├── 3_📈_Model_Metrics.py
│   ├── 4_💰_ROI_Simulator.py
│   └── 5_🔍_Model_Monitoring.py
├── requirements.txt
└── README.md
models/
├── churn_model.pkl (Git LFS)
├── preprocessor.pkl (Git LFS)
└── metadata.json
```

#### 2. Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Configure the app:

**Settings:**
- **Repository**: Select your GitHub repo
- **Branch**: `main`
- **Main file path**: `dashboard/app.py`
- **App URL**: Choose a custom URL (e.g., `telco-churn-dashboard`)

4. Click "Deploy!"

#### 3. Wait for Deployment

- First deployment takes 3-5 minutes
- Watch the logs for any errors
- Once deployed, you'll get a URL like: `https://telco-churn-dashboard.streamlit.app`

#### 4. Test the Dashboard

1. Open the URL in your browser
2. Navigate through all pages
3. Test the Risk Analysis prediction
4. Verify all charts load correctly

### Streamlit Cloud Free Tier Limits
- ✅ 1 GB RAM (sufficient for our model)
- ✅ Shared CPU
- ✅ Up to 3 apps
- ⚠️ Public apps only (code visible on GitHub)

---

## 🐳 Docker Deployment (Alternative)

### Build and Run Locally

```bash
# Build the image
cd api
docker build -t churn-api .

# Run the container
docker run -p 5000:5000 churn-api

# Test
curl http://localhost:5000/health
```

### Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect the Dockerfile
5. Set environment variables if needed
6. Deploy!

**Railway Free Tier:**
- ✅ 8 GB RAM
- ✅ 500 hours/month free
- ✅ No sleep on inactivity

---

## 🔐 Security Considerations

### API Security

1. **Add API Key Authentication** (for production):
```python
from functools import wraps
from flask import request

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != os.environ.get('API_KEY'):
            return jsonify({'error': 'Invalid API key'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/predict', methods=['POST'])
@require_api_key
def predict():
    # ... existing code
```

2. **Add Rate Limiting**:
```bash
pip install flask-limiter
```

3. **Enable HTTPS** (automatic on Render/Railway)

### Dashboard Security

1. **Add Authentication** (Streamlit Cloud):
   - Use Streamlit's built-in authentication
   - Or implement custom auth with `streamlit-authenticator`

2. **Protect Sensitive Data**:
   - Don't display real customer data
   - Use sample/anonymized data for demos

---

## 📊 Monitoring and Maintenance

### API Monitoring

1. **Health Checks**:
   - Set up automated health checks (Render provides this)
   - Monitor response times
   - Track error rates

2. **Logging**:
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    logger.info(f"Prediction request received")
    # ... existing code
```

3. **Metrics**:
   - Track prediction volume
   - Monitor model performance
   - Log prediction latencies

### Dashboard Monitoring

1. **Usage Analytics**:
   - Streamlit Cloud provides basic analytics
   - Track page views and user interactions

2. **Error Tracking**:
   - Monitor Streamlit logs
   - Set up error notifications

---

## 🔄 Updating the Deployment

### Update API

```bash
# Make changes to code
git add .
git commit -m "Update API"
git push origin main

# Render will auto-deploy
```

### Update Dashboard

```bash
# Make changes to code
git add .
git commit -m "Update dashboard"
git push origin main

# Streamlit Cloud will auto-deploy
```

### Update Model

```bash
# Replace model files
git lfs track "*.pkl"
git add models/*.pkl
git commit -m "Update model"
git push origin main

# Both services will auto-deploy with new model
```

---

## 🆘 Troubleshooting

### API Issues

**Problem**: API returns 503
- **Solution**: Check if model files are loaded correctly
- **Check**: Logs for "Model loaded successfully" message

**Problem**: Slow response times
- **Solution**: Increase workers in gunicorn command
- **Alternative**: Upgrade to paid tier for more resources

**Problem**: Out of memory
- **Solution**: Reduce model size or upgrade to paid tier

### Dashboard Issues

**Problem**: Dashboard won't load
- **Solution**: Check requirements.txt has all dependencies
- **Check**: Streamlit logs for errors

**Problem**: Model predictions fail
- **Solution**: Verify model files are in correct path
- **Check**: Git LFS files downloaded correctly

---

## 📞 Support Resources

- **Render Docs**: https://render.com/docs
- **Streamlit Docs**: https://docs.streamlit.io
- **Railway Docs**: https://docs.railway.app
- **Git LFS Docs**: https://git-lfs.github.com

