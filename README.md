# denoising_audio_files

## 🎧 Audio Denoising Autoencoder with TensorFlow

This project is an Audio Denoising Application that leverages a deep learning autoencoder built with TensorFlow. The model is designed to remove noise from audio signals and enhance audio quality.

## 🔍 Key Features
Trained a 1D Convolutional Autoencoder for audio denoising.
Hyperparameter tuning using Keras Tuner for optimal performance.
Preprocessing pipeline for audio normalization, padding/truncation, and reshaping for model input.
Converts noisy .wav files into clean denoised versions.
Integrated with a Flask API for easy model serving and deployment (optional).
Supports inference pipeline with audio preprocessing, model prediction, and saving denoised audio.

## 🛠 Tech Stack
Python 3.9.6
TensorFlow & Keras
Keras Tuner
Librosa
SoundFile (for audio I/O)
Flask (for deployment-ready API)
Docker

## 📁 Repository Structure

📂 flask_app/
├── 📂 templates/
│   └── index.html                # Frontend HTML file
├── audio_denoiser_best_model.h5  # Trained denoising model
├── flask_app.py                  # Flask backend application
├── Dockerfile                    # Dockerfile to containerize the app
├── requirements.txt              # Python dependencies
└── DAE.ipynb                     # Model training and tuning notebook



