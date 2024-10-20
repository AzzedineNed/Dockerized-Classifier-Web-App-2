import os
import numpy as np
import random
import cv2
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.applications.resnet50 import preprocess_input
import json
import time

# Set up the Flask application
app = Flask(__name__)

# Set seeds for reproducibility
os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(42)
random.seed(42)

# Load ResNet50 model without the top classification layer
base_model = ResNet50(weights='imagenet', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(2, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)

# Freeze the layers
for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Preprocessing function
def load_and_preprocess_image(image):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

# Predict function
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file'].read()
    img = load_and_preprocess_image(file)

    preds = model.predict(img)
    class_idx = np.argmax(preds[0])
    class_names = ['Cat', 'Dog']
    predicted_class = class_names[class_idx]
    confidence = preds[0][class_idx]

    # Log the prediction to a JSON file
    log_prediction(file_name=request.files['file'].filename, prediction=predicted_class, confidence=float(confidence))

    # Return JSON response to frontend
    return jsonify({'prediction': predicted_class, 'confidence': float(confidence)})


def log_prediction(file_name, prediction, confidence):
    log_data = {
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        'file_name': file_name,
        'prediction': prediction,
        'confidence': confidence
    }
    with open('predictions_log.json', 'a') as log_file:
        json.dump(log_data, log_file)
        log_file.write('\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
