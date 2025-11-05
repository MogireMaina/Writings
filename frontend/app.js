// Configuration
const API_URL = 'http://localhost:44445';

// State
let currentSentences = [];
let currentStats = {};

// DOM Elements
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const fileInfo = document.getElementById('fileInfo');
const uploadSection = document.getElementById('upload-section');
const configSection = document.getElementById('config-section');
const resultsSection = document.getElementById('results-section');
const stats = document.getElementById('stats');
const sentenceCount = document.getElementById('sentenceCount');
const sentenceSlider = document.getElementById('sentenceSlider');
const sliderValue = document.getElementById('sliderValue');
const processBtn = document.getElementById('processBtn');
const results = document.getElementById('results');
const newUploadBtn = document.getElementById('newUploadBtn');
const backendStatus = document.getElementById('backendStatus');
const statusDiv = document.getElementById('status');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    checkBackendHealth();
    setupEventListeners();
});

// Check backend health
async function checkBackendHealth() {
    try {
        const response = await fetch(`${API_URL}/health`);
        const data = await response.json();

        if (data.status === 'healthy') {
            backendStatus.textContent = `Online (Port ${data.port})`;
            backendStatus.classList.add('online');
        }
    } catch (error) {
        backendStatus.textContent = 'Offline';
        backendStatus.classList.add('offline');
        showStatus('Backend server not running. Start it with: cd backend && ./start.sh', 'error');
    }
}

// Setup event listeners
function setupEventListeners() {
    // Drag and drop
    dropZone.addEventListener('click', () => fileInput.click());
    dropZone.addEventListener('dragover', handleDragOver);
    dropZone.addEventListener('dragleave', handleDragLeave);
    dropZone.addEventListener('drop', handleDrop);
    fileInput.addEventListener('change', handleFileSelect);

    // Slider sync
    sentenceSlider.addEventListener('input', (e) => {
        const value = e.target.value;
        sentenceCount.value = value;
        sliderValue.textContent = value;
    });

    sentenceCount.addEventListener('input', (e) => {
        const value = Math.min(Math.max(1, e.target.value), currentSentences.length);
        sentenceSlider.value = value;
        sliderValue.textContent = value;
    });

    // Buttons
    processBtn.addEventListener('click', processData);
    newUploadBtn.addEventListener('click', resetApp);
}

// Drag and drop handlers
function handleDragOver(e) {
    e.preventDefault();
    dropZone.classList.add('drag-over');
}

function handleDragLeave(e) {
    e.preventDefault();
    dropZone.classList.remove('drag-over');
}

function handleDrop(e) {
    e.preventDefault();
    dropZone.classList.remove('drag-over');

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
}

function handleFileSelect(e) {
    const files = e.target.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
}

// Handle file upload
async function handleFile(file) {
    if (!file.name.match(/\.(txt|md|text)$/)) {
        showStatus('Please upload a .txt, .md, or .text file', 'error');
        return;
    }

    showStatus('Uploading and processing...', 'info');

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch(`${API_URL}/upload`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            currentSentences = data.sentences;
            currentStats = {
                totalSentences: data.total_sentences,
                characters: data.character_count,
                words: data.word_count
            };

            showStatus('File processed successfully!', 'success');
            showFileInfo(file, data);
            showConfigSection();
        } else {
            showStatus(`Error: ${data.error}`, 'error');
        }
    } catch (error) {
        showStatus(`Error: ${error.message}`, 'error');
    }
}

// Show file info
function showFileInfo(file, data) {
    fileInfo.style.display = 'block';
    fileInfo.innerHTML = `
        <strong>File loaded:</strong> ${file.name} (${formatBytes(file.size)})
        <br>
        <strong>Extracted:</strong> ${data.total_sentences.toLocaleString()} sentences,
        ${data.word_count.toLocaleString()} words,
        ${data.character_count.toLocaleString()} characters
    `;
}

// Show configuration section
function showConfigSection() {
    configSection.style.display = 'block';

    // Update stats
    stats.innerHTML = `
        <div class="stat-item">
            <div class="stat-label">Total Sentences</div>
            <div class="stat-value">${currentStats.totalSentences.toLocaleString()}</div>
        </div>
        <div class="stat-item">
            <div class="stat-label">Words</div>
            <div class="stat-value">${currentStats.words.toLocaleString()}</div>
        </div>
        <div class="stat-item">
            <div class="stat-label">Characters</div>
            <div class="stat-value">${currentStats.characters.toLocaleString()}</div>
        </div>
    `;

    // Set slider max
    sentenceSlider.max = currentStats.totalSentences;

    // Set default count (min of 1000 or total sentences)
    const defaultCount = Math.min(1000, currentStats.totalSentences);
    sentenceCount.value = defaultCount;
    sentenceSlider.value = defaultCount;
    sliderValue.textContent = defaultCount;

    // Scroll to config section
    configSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Process data
async function processData() {
    const count = parseInt(sentenceCount.value);

    if (count > currentSentences.length) {
        showStatus(`Cannot select ${count} sentences. Only ${currentSentences.length} available.`, 'error');
        return;
    }

    processBtn.disabled = true;
    processBtn.innerHTML = '<span class="spinner"></span> Processing...';

    try {
        const response = await fetch(`${API_URL}/process`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                sentences: currentSentences,
                count: count
            })
        });

        const data = await response.json();

        if (data.success) {
            showStatus('Training data prepared successfully!', 'success');
            showResults(data);
        } else {
            showStatus(`Error: ${data.error}`, 'error');
            processBtn.disabled = false;
            processBtn.textContent = 'Process Data';
        }
    } catch (error) {
        showStatus(`Error: ${error.message}`, 'error');
        processBtn.disabled = false;
        processBtn.textContent = 'Process Data';
    }
}

// Show results
function showResults(data) {
    resultsSection.style.display = 'block';

    results.innerHTML = `
        <div class="results-card">
            <h3>✓ Training Data Ready</h3>
            <p><strong>Selected Sentences:</strong> ${data.selected_count.toLocaleString()}</p>
            <p><strong>Created:</strong> ${new Date(data.data.created_at).toLocaleString()}</p>

            <h4 style="margin-top: 1.5rem;">Sample (First 3 sentences):</h4>
            <pre>${JSON.stringify(data.data.sentences.slice(0, 3), null, 2)}</pre>

            <h4 style="margin-top: 1.5rem;">Download Options:</h4>
            <div class="download-buttons">
                <button class="btn btn-download" onclick="downloadJSON()">
                    📥 Download JSON
                </button>
                <button class="btn btn-download" onclick="downloadJSONL()">
                    📥 Download JSONL
                </button>
                <button class="btn btn-download" onclick="downloadTXT()">
                    📥 Download TXT
                </button>
            </div>

            <div class="format-info">
                <p><strong>JSON:</strong> Full dataset with metadata</p>
                <p><strong>JSONL:</strong> JSON Lines format (common for AI training)</p>
                <p><strong>TXT:</strong> Plain text, one sentence per line</p>
            </div>
        </div>
    `;

    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Download functions
function downloadJSON() {
    window.location.href = `${API_URL}/download/json`;
}

function downloadJSONL() {
    window.location.href = `${API_URL}/download/jsonl`;
}

function downloadTXT() {
    window.location.href = `${API_URL}/download/txt`;
}

// Reset app
function resetApp() {
    uploadSection.style.display = 'block';
    configSection.style.display = 'none';
    resultsSection.style.display = 'none';
    fileInfo.style.display = 'none';
    fileInput.value = '';
    currentSentences = [];
    currentStats = {};
    processBtn.disabled = false;
    processBtn.textContent = 'Process Data';
    statusDiv.innerHTML = '';
    uploadSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Show status message
function showStatus(message, type) {
    statusDiv.textContent = message;
    statusDiv.className = `status ${type}`;
}

// Format bytes
function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}
