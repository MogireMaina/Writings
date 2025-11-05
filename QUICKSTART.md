# Quick Start Guide

Get up and running in 3 minutes!

## 🚀 Quick Setup

### 1. Start the Backend

```bash
cd backend
./start.sh
```

Or manually:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### 2. Open the Frontend

```bash
# Just open the HTML file in your browser
open frontend/index.html
```

That's it! 🎉

## 📝 Quick Usage

1. **Drop a text file** (100 pages of text!)
2. **Select number of sentences** (e.g., 1000)
3. **Click "Process & Save"**
4. **Done!** Your training data is ready

## 🔥 Firebase Setup (Optional)

Want to save your datasets? Add Firebase:

1. Go to https://console.firebase.google.com/
2. Create project → Settings → Service Accounts
3. Click "Generate New Private Key"
4. Save as `backend/firebase-key.json`
5. Restart backend

## 🐛 Troubleshooting

**Backend won't start?**
```bash
pip install Flask flask-cors firebase-admin nltk
```

**Frontend shows offline?**
- Make sure backend is running (check terminal)
- Visit http://localhost:44445/health in browser

**Need help?**
- Check README.md for detailed docs
- Open a GitHub issue

## 🎯 Example Use Case

```
1. Upload: 100-page research paper (10,000 sentences)
2. Select: 1,000 sentences for training
3. Save: To Firebase for later use
4. Export: In JSONL format for your AI model
```

## 📦 Ports

- Backend: `44445`
- Frontend: Open `index.html` directly (or use any port with HTTP server)

Happy fine-tuning! 🤖
