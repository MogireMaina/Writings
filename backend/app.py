from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import nltk
from nltk.tokenize import sent_tokenize
import json
from datetime import datetime
import io

# Download NLTK data (only needed first time)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# In-memory storage for the current session
current_dataset = None

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
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
    """Process and prepare selected sentences for training"""
    global current_dataset

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

        # Store in memory for download
        current_dataset = training_data

        return jsonify({
            'success': True,
            'selected_count': len(selected_sentences),
            'data': training_data
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/export/json', methods=['GET'])
def export_json():
    """Export current dataset as JSON"""
    try:
        if not current_dataset:
            return jsonify({'error': 'No dataset available. Process sentences first.'}), 404

        # Create JSON file in memory
        json_data = json.dumps(current_dataset, indent=2)

        return jsonify({
            'success': True,
            'data': current_dataset,
            'download_url': '/download/json'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/export/jsonl', methods=['GET'])
def export_jsonl():
    """Export current dataset in JSONL format (one JSON object per line)"""
    try:
        if not current_dataset:
            return jsonify({'error': 'No dataset available. Process sentences first.'}), 404

        sentences = current_dataset.get('sentences', [])

        # Format for fine-tuning: JSONL with {"text": "sentence"}
        training_format = []
        for sentence in sentences:
            training_format.append({
                "text": sentence,
                "metadata": {
                    "source": "custom_upload",
                    "created_at": current_dataset.get('created_at')
                }
            })

        return jsonify({
            'success': True,
            'format': 'jsonl',
            'data': training_format,
            'count': len(training_format),
            'download_url': '/download/jsonl'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/json', methods=['GET'])
def download_json():
    """Download current dataset as JSON file"""
    try:
        if not current_dataset:
            return jsonify({'error': 'No dataset available'}), 404

        # Create JSON string
        json_str = json.dumps(current_dataset, indent=2)

        # Create file in memory
        mem_file = io.BytesIO()
        mem_file.write(json_str.encode('utf-8'))
        mem_file.seek(0)

        # Generate filename with timestamp
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        filename = f'training_data_{timestamp}.json'

        return send_file(
            mem_file,
            mimetype='application/json',
            as_attachment=True,
            download_name=filename
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/jsonl', methods=['GET'])
def download_jsonl():
    """Download current dataset as JSONL file"""
    try:
        if not current_dataset:
            return jsonify({'error': 'No dataset available'}), 404

        sentences = current_dataset.get('sentences', [])

        # Create JSONL format (one JSON per line)
        jsonl_lines = []
        for sentence in sentences:
            line = json.dumps({
                "text": sentence,
                "metadata": {
                    "source": "custom_upload",
                    "created_at": current_dataset.get('created_at')
                }
            })
            jsonl_lines.append(line)

        jsonl_str = '\n'.join(jsonl_lines)

        # Create file in memory
        mem_file = io.BytesIO()
        mem_file.write(jsonl_str.encode('utf-8'))
        mem_file.seek(0)

        # Generate filename with timestamp
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        filename = f'training_data_{timestamp}.jsonl'

        return send_file(
            mem_file,
            mimetype='application/x-ndjson',
            as_attachment=True,
            download_name=filename
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/txt', methods=['GET'])
def download_txt():
    """Download current dataset as plain text file (one sentence per line)"""
    try:
        if not current_dataset:
            return jsonify({'error': 'No dataset available'}), 404

        sentences = current_dataset.get('sentences', [])

        # Create plain text (one sentence per line)
        text_str = '\n'.join(sentences)

        # Create file in memory
        mem_file = io.BytesIO()
        mem_file.write(text_str.encode('utf-8'))
        mem_file.seek(0)

        # Generate filename with timestamp
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        filename = f'training_data_{timestamp}.txt'

        return send_file(
            mem_file,
            mimetype='text/plain',
            as_attachment=True,
            download_name=filename
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("AI Fine-tuning Data Preparation Backend")
    print("=" * 60)
    print(f"Starting server on http://localhost:44445")
    print("=" * 60)
    app.run(host='0.0.0.0', port=44445, debug=True)
