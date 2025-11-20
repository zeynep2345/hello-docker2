# 1. Python tabanlı bir imaj seç
FROM python:3.10-slim

# 2. Konteyner içinde çalışma dizini oluştur
WORKDIR /app

# 3. Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Uygulama dosyalarını kopyala
COPY . .

# 5. Uygulamayı başlat
CMD ["python", "web_service.py"]
