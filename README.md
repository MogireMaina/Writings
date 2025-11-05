# AI Model Fine-tuning Data Preparation Tool

A web-based application for preparing training data for AI model fine-tuning. Upload large text documents, extract sentences, and prepare datasets for training.

## Features

- **Drag & Drop Interface**: Easy file uploads with modern UI
- **Text Processing**: Automatic sentence extraction using NLTK
- **Flexible Selection**: Choose exactly how many sentences to use (e.g., 1000 from 10,000)
- **Firebase Integration**: Store and manage training datasets
- **Export Ready**: Data formatted for AI model fine-tuning
- **Statistics**: View word count, sentence count, and character count
- **Dataset Management**: View and track all your prepared datasets

## Architecture

- **Backend**: Python Flask (Port 44445)
  - Text processing with NLTK
  - Firebase Firestore integration
  - RESTful API

- **Frontend**: HTML/CSS/JavaScript
  - Modern, responsive UI
  - Real-time updates
  - Drag-and-drop file upload

## Prerequisites

- Python 3.8+
- Firebase account (optional, but recommended)
- Modern web browser

## Setup Instructions

### 1. Clone the Repository

```bash
cd /home/user/Writings
```

### 2. Set Up Python Backend

```bash
# Create virtual environment
cd backend
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Firebase (Optional but Recommended)

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project or use existing one
3. Go to Project Settings → Service Accounts
4. Click "Generate New Private Key"
5. Save the JSON file as `backend/firebase-key.json`

**Important**: Never commit `firebase-key.json` to git (it's already in .gitignore)

If you skip this step, the app will still work but won't save data to Firebase.

### 4. Run the Backend

```bash
cd backend
source venv/bin/activate  # If not already activated
python app.py
```

You should see:
```
============================================================
AI Fine-tuning Data Preparation Backend
============================================================
✓ Firebase initialized successfully
Starting server on http://localhost:44445
============================================================
```

### 5. Open the Frontend

Simply open `frontend/index.html` in your web browser:

```bash
# Option 1: Direct file open
open frontend/index.html  # Mac
xdg-open frontend/index.html  # Linux
start frontend/index.html  # Windows

# Option 2: Use a simple HTTP server (optional)
cd frontend
python3 -m http.server 44444
# Then visit: http://localhost:44444
```

## Usage

### Step 1: Upload Text

1. Open the frontend in your browser
2. Drag and drop a `.txt` file (or click to browse)
3. The system will automatically extract all sentences

### Step 2: Configure Training Data

1. View statistics (total sentences, words, characters)
2. Use the slider or input field to select how many sentences to use
3. Click "Process & Save to Firebase"

### Step 3: View Results

- See the dataset details
- View sample sentences
- Check Firebase save status
- View all saved datasets

## API Endpoints

### Health Check
```
GET /health
```

### Upload Text
```
POST /upload
Content-Type: multipart/form-data
Body: file (text file)
```

### Process Sentences
```
POST /process
Content-Type: application/json
Body: {
  "sentences": ["sentence 1", "sentence 2", ...],
  "count": 1000
}
```

### Get All Datasets
```
GET /datasets
```

### Get Specific Dataset
```
GET /dataset/<dataset_id>
```

### Export Dataset
```
GET /export/<dataset_id>
```

## Project Structure

```
/home/user/Writings/
├── backend/
│   ├── app.py                    # Flask application
│   ├── requirements.txt          # Python dependencies
│   ├── firebase-key.json.example # Firebase config template
│   └── venv/                     # Virtual environment (created)
├── frontend/
│   ├── index.html                # Main HTML page
│   ├── style.css                 # Styling
│   └── app.js                    # Frontend logic
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## Troubleshooting

### Backend won't start
- Make sure virtual environment is activated
- Check if port 44445 is available: `lsof -i :44445`
- Install dependencies: `pip install -r requirements.txt`

### Frontend shows "Backend Offline"
- Ensure backend is running on port 44445
- Check browser console for CORS errors
- Verify API_URL in `frontend/app.js` is correct

### Firebase warnings
- If you see "Firebase not configured", download your service account key
- Save it as `backend/firebase-key.json`
- Restart the backend

### NLTK errors
The app will automatically download required NLTK data on first run. If you encounter issues:
```python
import nltk
nltk.download('punkt')
```

## Data Format

Training data is stored in Firebase with this structure:

```json
{
  "sentences": ["sentence 1", "sentence 2", "..."],
  "count": 1000,
  "created_at": "2025-11-05T12:00:00.000Z",
  "metadata": {
    "total_available": 5000,
    "selected_count": 1000
  }
}
```

Export format (JSONL):
```json
{"text": "sentence 1", "metadata": {"source": "custom_upload", "created_at": "..."}}
{"text": "sentence 2", "metadata": {"source": "custom_upload", "created_at": "..."}}
```

## Next Steps / Future Features

- [ ] Support for multiple file formats (PDF, DOCX)
- [ ] Advanced filtering (by length, keywords, etc.)
- [ ] Data augmentation options
- [ ] Direct export to popular fine-tuning formats
- [ ] Batch processing
- [ ] Data quality metrics

## License

MIT License

## Contributing

This is a GitHub project. Feel free to fork, modify, and submit pull requests!

## Support

For issues or questions, please open a GitHub issue.
