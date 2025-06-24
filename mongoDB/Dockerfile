# Wybieramy obraz bazowy Pythona
FROM python:3.12.9

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki aplikacji z lokalnego katalogu ./app do kontenera
COPY app/ .

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Uruchamiamy aplikację
CMD ["python", "MongoDB_App.py"]
