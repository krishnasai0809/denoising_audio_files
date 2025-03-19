from flask import Flask, request, render_template, send_file, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
import librosa
import numpy as np
import soundfile as sf
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the model
try:
    model = load_model("audio_denoiser_best_model.h5", custom_objects={'mse': MeanSquaredError()})
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def preprocess_audio(file_path, target_sample_rate=32000):
    audio, sr = librosa.load(file_path, sr=target_sample_rate)
    audio = librosa.util.normalize(audio)
    return audio

def chunk_audio(audio, chunk_size=32000):
    num_chunks = int(np.ceil(len(audio) / chunk_size))
    padded_audio = np.pad(audio, (0, num_chunks * chunk_size - len(audio)), 'constant')
    chunks = np.reshape(padded_audio, (num_chunks, chunk_size))
    return chunks

def denoise_audio(input_file, output_file, model, target_sample_rate=32000):
    # Step 1: Preprocess the noisy input
    audio = preprocess_audio(input_file, target_sample_rate)
    
    # Step 2: Split into 1-sec chunks
    chunks = chunk_audio(audio, chunk_size=32000)
    
    denoised_chunks = []
    for chunk in chunks:
        chunk_input = np.expand_dims(chunk, axis=(0, -1))
        denoised_chunk = model.predict(chunk_input)
        denoised_chunk = denoised_chunk.squeeze()
        denoised_chunks.append(denoised_chunk)
    
    # Step 3: Concatenate all denoised chunks
    denoised_audio = np.concatenate(denoised_chunks)
    denoised_audio = librosa.util.normalize(denoised_audio)
    
    # Step 4: Save the denoised audio
    sf.write(output_file, denoised_audio, target_sample_rate)
    return output_file

@app.route('/', methods=['GET'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error rendering template: {e}")
        return str(e), 500

@app.route('/denoise', methods=['POST'])
def denoise():
    if 'audio' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['audio']
    if file.filename == '':
        return 'No file selected', 400
    
    # Save the uploaded file
    input_filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], input_filename)
    file.save(input_path)
    
    # Generate output filename and path
    output_filename = f'denoised_{input_filename}'
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
    
    # Process the audio
    denoise_audio(input_path, output_path, model)
    
    # Return paths for both original and denoised audio
    return {
        'original': url_for('uploaded_file', filename=input_filename),
        'denoised': url_for('uploaded_file', filename=output_filename)
    }

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

if __name__ == '__main__':
    print("Starting Flask application...")
    print(f"Template folder path: {app.template_folder}")
    app.run(host='0.0.0.0', port=5000)

