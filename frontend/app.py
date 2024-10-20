from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5001/predict"  # The backend container URL

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['file']
    if not file:
        return "No file uploaded", 400

    # Send the image to the backend for prediction
    response = requests.post(BACKEND_URL, files={'file': file})

    # Handle backend errors
    if response.status_code != 200:
        return "Error from backend", 500

    # Get the JSON response from backend
    result = response.json()

    # Pass the result to the result.html template for rendering
    return render_template('result.html', 
                           predicted_class=result['prediction'], 
                           confidence=result['confidence'], 
                           image_path=url_for('static', filename=f"uploads/{file.filename}"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
