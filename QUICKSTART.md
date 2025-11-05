# Quick Start Guide

Get up and running in 2 minutes!

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
3. **Click "Process Data"**
4. **Download** in your preferred format (JSON, JSONL, or TXT)

## 📥 Export Formats

- **JSON**: Full dataset with metadata
- **JSONL**: JSON Lines (standard for AI training)
- **TXT**: Plain text, one sentence per line

## 🐛 Troubleshooting

**Backend won't start?**
```bash
pip install Flask flask-cors nltk
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
3. Process: Extract and prepare data
4. Download: JSONL format for your AI model
```

## 📦 Ports

- Backend: `44445`
- Frontend: Open `index.html` directly

## ⚡ Features

- No database required
- No cloud services needed
- Runs 100% locally
- Simple and fast
- Multiple export formats

Happy fine-tuning! 🤖
