# denoising_audio_files

## 🎧 Audio Denoising Autoencoder with TensorFlow

This project is an Audio Denoising Application that leverages a deep learning autoencoder built with TensorFlow. The model is designed to remove noise from audio signals and enhance audio quality.

## 🔍 Key Features
- Trained a 1D Convolutional Autoencoder for audio denoising.
- Hyperparameter tuning using Keras Tuner for optimal performance.
- Preprocessing pipeline for audio normalization, padding/truncation, and reshaping for model input.
- Converts noisy .wav files into clean denoised versions.
- Integrated with a Flask API for easy model serving and deployment (optional).
- Supports inference pipeline with audio preprocessing, model prediction, and saving denoised audio.

## 🛠 Tech Stack
- Python 3.9.6
- TensorFlow & Keras
- Keras Tuner
- Librosa
- SoundFile (for audio I/O)
- Flask (for deployment-ready API)
- Docker

## 📁 Repository Structure


```
flask_app/
├── templates/
│   └── index.html                  # Frontend HTML file
├── audio_denoiser_best_model.h5    # Trained audio denoising model
├── flask_app.py                    # Flask backend application
├── Dockerfile                      # Dockerfile to build the Docker image
├── requirements.txt                # List of Python dependencies
└── DAE.ipynb                       # Notebook for training & tuning the autoencoder model

```

## 🚀 Setting Up the Application with Docker
To containerize and run the Audio Denoising Web Application using Docker, follow these simple steps:

1️⃣ Build the Docker Image

Navigate to the project directory (where the Dockerfile is located) and run:
```
docker build -t audio_denoiser .
```
- docker build : Command to build a Docker image.
- -t audio_denoiser : Tags the image with the name audio_denoiser.
- . : Refers to the current directory as the build context.

2️⃣ Run the Docker Container

Once the image is built, run it using:
```
docker run --rm -it -p 5000:5000 audio_denoiser
```
- docker run : Runs a new container from the image.
- --rm : Automatically removes the container when it stops.
- -it : Runs the container in interactive mode with a terminal.
- -p 5000:5000 : Maps port 5000 inside the container to port 5000 on your host machine.
- audio_denoiser : The name of the image you just built.

The web interface will be available at http://localhost:5000

## 🎯 Usage

Open the application in your browser :

Click on "Choose File" and upload the audio file you wish to denoise.

⚠️ Note: The input file must be in .wav format.

Click on the "Denoise" button to process the file.

After processing, you can listen to the denoised audio directly on the web page.

If desired, click on "Download" to save the denoised audio file locally.








      

