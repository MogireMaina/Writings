from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import nltk
from nltk.tokenize import sent_tokenize
import os
import json
from datetime import datetime

# Download NLTK data (only needed first time)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Firebase initialization
db = None

def initialize_firebase():
    """Initialize Firebase with credentials"""
    global db
    try:
        if not firebase_admin._apps:
            # Check if firebase config exists
            if os.path.exists('firebase-key.json'):
                cred = credentials.Certificate('firebase-key.json')
                firebase_admin.initialize_app(cred)
                db = firestore.client()
                print("✓ Firebase initialized successfully")
            else:
                print("⚠ Warning: firebase-key.json not found. Firebase features disabled.")
                print("  Download your service account key from Firebase Console")
    except Exception as e:
        print(f"⚠ Firebase initialization error: {e}")

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'firebase_connected': db is not None,
        'port': 44445
    })

@app.route('/upload', methods=['POST'])
def upload_text():
    """Upload and process text file"""
    try:
        # Get file from request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Read file content
        content = file.read().decode('utf-8')

        # Extract sentences
        sentences = sent_tokenize(content)

        return jsonify({
            'success': True,
            'total_sentences': len(sentences),
            'sentences': sentences,
            'character_count': len(content),
            'word_count': len(content.split())
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/process', methods=['POST'])
def process_sentences():
    """Process and save selected sentences to Firebase"""
    try:
        data = request.json
        sentences = data.get('sentences', [])
        count = data.get('count', len(sentences))

        # Select the specified number of sentences
        selected_sentences = sentences[:count]

        # Prepare training data
        training_data = {
            'sentences': selected_sentences,
            'count': len(selected_sentences),
            'created_at': datetime.utcnow().isoformat(),
            'metadata': {
                'total_available': len(sentences),
                'selected_count': count
            }
        }

        # Save to Firebase if available
        doc_id = None
        if db:
            doc_ref = db.collection('training_data').add(training_data)
            doc_id = doc_ref[1].id
            training_data['id'] = doc_id

        return jsonify({
            'success': True,
            'selected_count': len(selected_sentences),
            'firebase_saved': db is not None,
            'document_id': doc_id,
            'data': training_data
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/datasets', methods=['GET'])
def get_datasets():
    """Get all saved datasets from Firebase"""
    try:
        if not db:
            return jsonify({'error': 'Firebase not initialized'}), 500

        datasets = []
        docs = db.collection('training_data').order_by('created_at', direction=firestore.Query.DESCENDING).limit(50).stream()

        for doc in docs:
            data = doc.to_dict()
            data['id'] = doc.id
            # Don't send full sentences list, just metadata
            data['sentences'] = f"{len(data.get('sentences', []))} sentences"
            datasets.append(data)

        return jsonify({
            'success': True,
            'datasets': datasets
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/dataset/<dataset_id>', methods=['GET'])
def get_dataset(dataset_id):
    """Get a specific dataset by ID"""
    try:
        if not db:
            return jsonify({'error': 'Firebase not initialized'}), 500

        doc = db.collection('training_data').document(dataset_id).get()

        if not doc.exists:
            return jsonify({'error': 'Dataset not found'}), 404

        data = doc.to_dict()
        data['id'] = doc.id

        return jsonify({
            'success': True,
            'dataset': data
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/export/<dataset_id>', methods=['GET'])
def export_dataset(dataset_id):
    """Export dataset in training format (JSONL)"""
    try:
        if not db:
            return jsonify({'error': 'Firebase not initialized'}), 500

        doc = db.collection('training_data').document(dataset_id).get()

        if not doc.exists:
            return jsonify({'error': 'Dataset not found'}), 404

        data = doc.to_dict()
        sentences = data.get('sentences', [])

        # Format for fine-tuning (adjust based on your model)
        # Common formats: JSONL with {"text": "sentence"}
        training_format = []
        for sentence in sentences:
            training_format.append({
                "text": sentence,
                "metadata": {
                    "source": "custom_upload",
                    "created_at": data.get('created_at')
                }
            })

        return jsonify({
            'success': True,
            'format': 'jsonl',
            'data': training_format,
            'count': len(training_format)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("AI Fine-tuning Data Preparation Backend")
    print("=" * 60)
    initialize_firebase()
    print(f"Starting server on http://localhost:44445")
    print("=" * 60)
    app.run(host='0.0.0.0', port=44445, debug=True)
