
# Restaurant Tip Predictor (Dockerized)

This project predicts the tip amount based on restaurant bill details using a machine learning model. The application is built with Python, features an interactive Gradio user interface, and is fully containerized with Docker for seamless deployment.

---
## 📹 Showcase

Here is a demonstration of the project:

<video controls src="DARETNY/MLops_ready/showcase.mp4" title="Tips predict module"></video>
---

## 🚀 Features
- **Tip Prediction**: Predicts tip amount based on inputs like total bill, gender, smoker status, day, time, and party size.
- **User-Friendly Interface**: A simple and interactive interface powered by Gradio.
- **Dockerized**: Easily deployable as a Docker container.

---

## 🛠️ Requirements
- **Docker**: Ensure Docker is installed on your system.

---

## 📦 Setup and Run Instructions

### 1. **Clone the Repository**
Use the following commands to clone the project to your local machine:
```bash
git clone <repository-url>
cd MLops_ready
```

### 2. **Build the Docker Image**
Build the Docker image using the provided `Dockerfile`:
```bash
docker build -t tip-predictor .
```

### 3. **Run the Docker Container**
Run the container and expose the application on port 7860:
```bash
docker run -p 7860:7860 tip-predictor
```

### 4. **Access the Application**
Open your web browser and navigate to:
```
http://localhost:7860
```

You can now use the Gradio interface to predict tips!

---

## 📂 Project Structure
```
MLops_ready/
├── app.py                         # Main application code
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker configuration file
├── tip_predictor_pipeline_improved.joblib  # Pre-trained model file
└── README.md                      # Project documentation
```

---

## 📝 Important Notes
- Ensure the `tip_predictor_pipeline_improved.joblib` file is in the project directory before building the Docker image.
- To share the application publicly, use the `share=True` option in the Gradio interface.

---

## 📜 License
This project is licensed under the MIT License. For more details, please refer to the [LICENSE](./LICENSE) file.

---

## 🛡️ Developer Notes
This project focuses on Dockerization and deployment practices rather than building machine learning models. For details on model training and related code, visit [this link](https://colab.research.google.com/drive/1ZgVoA1G4NipDO0h7NTp77elotmnhcUXU?usp=sharing).

