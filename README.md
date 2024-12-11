# Dockerized Classifier Web App 2

This project is a continuation of the [Dockerized Classifier Web App](https://github.com/AzzedineNed/Dockerized-Classifier-Web-App), extending the functionality by incorporating Docker Compose for orchestrating multiple services (frontend and backend). The web app allows users to upload images of cats or dogs, which are classified using a pre-trained ResNet50 model.

## Features

- **Image Upload via Frontend**: Users can upload an image through the frontend web interface.
- **Image Classification in Backend**: The backend service processes the uploaded image using the pre-trained ResNet50 model and returns a classification (cat or dog).
- **Dockerized Multi-Service Application**: The app is divided into two services (frontend and backend) using Docker Compose, making it easier to manage and scale.
- **Docker Network**: The services communicate via an automatically created Docker network, enabling seamless communication between the frontend and backend.

## Requirements

- **Docker**: Ensure Docker is installed on your system.
- **Docker Compose**: To orchestrate the frontend and backend services.

## How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/AzzedineNed/dockerized-classifier-web-app-2.git
cd dockerized-classifier-web-app-2

```

### CD to the repo

```bash
cd dockerized-classifier-web-app-2
```

### Step 2: Build and Run using Docker Compose

```bash
docker-compose up --build
```

This will build both the frontend and backend Docker images and start the services. Docker Compose will automatically create a network so that the services can communicate with each other.

### Step 3: Access the Application

- **Frontend**: Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the upload interface.
- **Backend**: The backend service is connected to the frontend via Docker Compose networking, so there is no need to interact directly with it.

### Step 4: Stop the Services

To stop the running services, use the following command:

```bash
docker-compose down
```

### Key Files

- **backend/predict.py**: This script contains the Flask app that handles image classification using the pre-trained ResNet50 model.
- **frontend/app.py**: The frontend Flask app for managing the image upload interface and sending the image to the backend for classification.
- **docker-compose.yml**: This file defines the Docker services (frontend and backend), the build process, and the shared Docker network.
- **backend/Dockerfile**: This Dockerfile defines the environment for the backend service, installing necessary dependencies and setting up the Flask application.
- **frontend/Dockerfile**: This Dockerfile defines the environment for the frontend service, installing required libraries and preparing the Flask app.
- **requirements.txt**: Defines the dependencies for both the frontend and backend environments.
- **upload.html**: The frontend HTML form for image uploads.
- **result.html**: Displays the classification results (cat or dog) and the confidence score of the prediction.

### How the System Works

- **Frontend (Flask)**: The user interacts with the frontend by uploading an image through the interface.
- **Backend (Flask)**: The frontend sends the uploaded image to the backend, which uses the ResNet50 model to classify the image.
- **Prediction and Result Display**: The backend returns the classification result to the frontend, which displays the prediction along with the confidence score.

### Networking

Docker Compose creates an internal network that allows the frontend and backend services to communicate with each other. This is done without the need for manual network creation, and Docker handles the connections automatically when the services are defined in `docker-compose.yml`.

### Running the Application

To start the application, use the following command in your terminal:

```bash
docker-compose up
```

### Conclusion

This project showcases how to containerize a Flask web application and manage multiple services using Docker Compose. The Dockerized approach simplifies deployment and scaling, while the app demonstrates a basic image classification pipeline using ResNet50.
