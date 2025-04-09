# Dockerfile

# Temel Python imajını kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# requirements.txt dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu ve model dosyasını kopyala
# saved_model klasörünü ve içindekileri de kopyala
COPY . .

# Gradio'nun çalıştığı portu dışarı aç (varsayılan 7860)
EXPOSE 7860

# Uygulamayı başlatmak için komut
# server_name="0.0.0.0" ile tüm interfacelerde dinlemesini sağlıyoruz
CMD ["python", "app.py"]