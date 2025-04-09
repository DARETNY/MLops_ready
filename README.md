# Restaurant Tip Predictor (Dockerized)

This project predicts the tip amount based on restaurant bill details using a machine learning model. The application is built with Python and uses Gradio for the user interface. It is fully containerized using Docker.

## Features
- Predicts tip amount based on inputs like total bill, gender, smoker status, day, time, and party size.
- Simple and interactive Gradio interface.
- Dockerized for easy deployment.

## Prerequisites
- Docker installed on your system.

## How to Run the Project on Docker

1. **Clone the Repository**  
   Clone this project to your local machine:
   ```bash
   git clone <repository-url>
   cd PyCharmMiscProject
   ```

2. **Build the Docker Image**  
   Build the Docker image using the provided `Dockerfile`:
   ```bash
   docker build -t tip-predictor .
   ```

3. **Run the Docker Container**  
   Run the container and expose the application on port 7860:
   ```bash
   docker run -p 7860:7860 tip-predictor
   ```

4. **Access the Application**  
   Open your browser and navigate to:
   ```
   http://localhost:7860
   ```

   You can now use the Gradio interface to predict tips.

## Notes
- Ensure the `tip_predictor_pipeline_improved.joblib` file is in the project directory before building the Docker image.
- If you want to share the application publicly, you can use the `share=True` option in the Gradio interface.

## File Structure
```
PyCharmMiscProject/
├── app.py                # Main application code
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── tip_predictor_pipeline_improved.joblib  # Pre-trained model file
└── README.md             # Project documentation
```

## License
This project is licensed under the MIT License.
