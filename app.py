# Flask application entry point
from flask import Flask, render_template, request, jsonify
import torch
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'data/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # TODO: Call prediction function from predict.py
        # Example: result = predict(file_path, timeseries_path=None)
        return jsonify({
            'disease': 'Healthy',  # Placeholder
            'confidence': 0.92,    # Placeholder
            'recommendations': 'No treatment needed. Continue regular monitoring.'
        })
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/forecast', methods=['GET'])
def forecast():
    # TODO: Call time series prediction function from predict.py
    return jsonify({
        'current_risk': 'Low',       # Placeholder
        'next_week': 'Moderate',     # Placeholder
        'two_weeks': 'High',         # Placeholder
        'peak_risk': '18 days'       # Placeholder
    })

if __name__ == '__main__':
    app.run(debug=True)
