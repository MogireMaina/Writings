# AI Model Fine-tuning Data Preparation Tool

A simple web-based application for preparing training data for AI model fine-tuning. Upload large text documents (100+ pages), extract sentences, and download formatted datasets ready for training.

## Features

- **Drag & Drop Interface**: Easy file uploads with modern UI
- **Text Processing**: Automatic sentence extraction using NLTK
- **Flexible Selection**: Choose exactly how many sentences to use (e.g., 1000 from 10,000)
- **Multiple Export Formats**: Download as JSON, JSONL, or plain text
- **Statistics**: View word count, sentence count, and character count
- **No Database Required**: Simple, lightweight, runs entirely locally

## Architecture

- **Backend**: Python Flask (Port 44445)
  - Text processing with NLTK
  - In-memory data storage
  - RESTful API
  - File download endpoints

- **Frontend**: HTML/CSS/JavaScript
  - Modern, responsive UI
  - Real-time updates
  - Drag-and-drop file upload

## Prerequisites

- Python 3.8+
- Modern web browser

That's it! No database or cloud services needed.

## Quick Start

### 1. Start the Backend

```bash
cd backend
./start.sh
```

### 2. Open the Frontend

Simply open `frontend/index.html` in your browser:

```bash
# Mac
open frontend/index.html

# Linux
xdg-open frontend/index.html

# Windows
start frontend/index.html
```

That's it! 🎉

## Detailed Setup

### Backend Setup

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

You should see:
```
============================================================
AI Fine-tuning Data Preparation Backend
============================================================
Starting server on http://localhost:44445
============================================================
```

## Usage

### Step 1: Upload Text

1. Open `frontend/index.html` in your browser
2. Drag and drop a `.txt` file (or click to browse)
3. The system will automatically extract all sentences

### Step 2: Configure Training Data

1. View statistics (total sentences, words, characters)
2. Use the slider or input field to select how many sentences to use
3. Click "Process Data"

### Step 3: Download

Choose your preferred format:
- **JSON**: Full dataset with metadata
- **JSONL**: JSON Lines format (common for AI training)
- **TXT**: Plain text, one sentence per line

## API Endpoints

### Health Check
```
GET /health
Response: {"status": "healthy", "port": 44445}
```

### Upload Text
```
POST /upload
Content-Type: multipart/form-data
Body: file (text file)

Response: {
  "success": true,
  "total_sentences": 5000,
  "sentences": ["...", "..."],
  "character_count": 50000,
  "word_count": 10000
}
```

### Process Sentences
```
POST /process
Content-Type: application/json
Body: {
  "sentences": ["sentence 1", "sentence 2", ...],
  "count": 1000
}

Response: {
  "success": true,
  "selected_count": 1000,
  "data": {...}
}
```

### Download Files
```
GET /download/json   - Download as JSON
GET /download/jsonl  - Download as JSONL
GET /download/txt    - Download as plain text
```

## Project Structure

```
/home/user/Writings/
├── backend/
│   ├── app.py               # Flask application
│   ├── requirements.txt     # Python dependencies
│   ├── start.sh            # Startup script
│   └── venv/               # Virtual environment (created)
├── frontend/
│   ├── index.html          # Main HTML page
│   ├── style.css           # Styling
│   └── app.js              # Frontend logic
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── QUICKSTART.md           # Quick start guide
```

## Export Formats

### JSON Format
Full dataset with metadata:
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

### JSONL Format
One JSON object per line (common for ML training):
```jsonl
{"text": "sentence 1", "metadata": {"source": "custom_upload", "created_at": "..."}}
{"text": "sentence 2", "metadata": {"source": "custom_upload", "created_at": "..."}}
```

### TXT Format
Plain text, one sentence per line:
```
sentence 1
sentence 2
sentence 3
```

## Troubleshooting

### Backend won't start
- Make sure virtual environment is activated
- Check if port 44445 is available: `lsof -i :44445` (Linux/Mac)
- Install dependencies: `pip install -r requirements.txt`

### Frontend shows "Backend Offline"
- Ensure backend is running on port 44445
- Check browser console for CORS errors
- Verify `API_URL` in `frontend/app.js` is correct

### NLTK errors
The app will automatically download required NLTK data on first run. If you encounter issues:
```python
import nltk
nltk.download('punkt')
```

## Example Use Case

```
1. Upload: 100-page research paper (10,000 sentences)
2. Select: 1,000 sentences for training
3. Download: As JSONL for your AI model
4. Use: Feed directly into your fine-tuning pipeline
```

## Dependencies

- **Flask 3.0.0**: Web framework
- **flask-cors 4.0.0**: CORS support
- **nltk 3.8.1**: Natural language processing
- **gunicorn 21.2.0**: Production server (optional)

## Future Features

- [ ] Support for multiple file formats (PDF, DOCX)
- [ ] Advanced filtering (by length, keywords, etc.)
- [ ] Data augmentation options
- [ ] Batch processing multiple files
- [ ] Data quality metrics
- [ ] Custom tokenization options

## Contributing

This is a GitHub project. Feel free to fork, modify, and submit pull requests!

## License

MIT License

## Support

For issues or questions, please open a GitHub issue.
