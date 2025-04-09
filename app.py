# app.py
import pandas as pd
import joblib
import gradio as gr
import os

# Modelin bulunduğu yolu belirle
model_filename = os.path.join("tip_predictor_pipeline_improved.joblib")

# Modeli yükle
try:
    loaded_pipeline = joblib.load(model_filename)
    print("Model pipeline loaded successfully.")
except FileNotFoundError:
    print(f"Error: Model file not found at {model_filename}")
    # Burada alternatif bir işlem yapabilir veya çıkabilirsiniz.
    exit()
except Exception as e:
    print(f"Error loading model: {e}")
    exit()


# Tahmin fonksiyonu
def predict_tip_improved(total_bill, sex, smoker, day, time, size):
    loaded_pipeline_improved = joblib.load(model_filename)

    if size is None or size == 0:
        bill_per_person_val = 0
    else:
        bill_per_person_val = total_bill / size

    input_data = pd.DataFrame(
        {
            "total_bill": [total_bill],
            "sex": [sex],
            "smoker": [smoker],
            "day": [day],
            "time": [time],
            "size": [size],
            "bill_per_person": [bill_per_person_val],
        }
    )
    # Sütun sırasının pipeline'ın beklediği sıra ile aynı olması önemli DEĞİL,
    # çünkü ColumnTransformer isimlere göre çalışır.

    # Tahmin yap
    prediction = loaded_pipeline_improved.predict(input_data)

    # Tahmini döndür
    return round(prediction[0], 2)


# Gradio arayüzü
inputs = [
    gr.Number(label="Total Bill ($)"),
    gr.Radio(label="Sex", choices=["Male", "Female"]),
    gr.Radio(label="Smoker", choices=["Yes", "No"]),
    gr.Dropdown(label="Day", choices=["Thur", "Fri", "Sat", "Sun"]),
    gr.Dropdown(label="Time", choices=["Lunch", "Dinner"]),
    gr.Slider(label="Size (Party Size)", minimum=1, maximum=10, step=1)
]
outputs = gr.Number(label="Predicted Tip ($)")

interface = gr.Interface(
    fn=predict_tip_improved,
    inputs=inputs,
    outputs=outputs,
    title="Restaurant Tip Predictor (Dockerized)",
    description="Enter the details to predict the tip amount."
)

# Uygulamayı çalıştır (Docker içinde 0.0.0.0 önemlidir)
print("Starting Gradio interface...")
interface.launch(server_name="0.0.0.0", server_port=7860,share=True, debug=True)  # Docker için port ve host ayarı
