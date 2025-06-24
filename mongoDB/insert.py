from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import json

# Funkcja pomocnicza do konwersji pól specjalnych ($oid, $date)
def normalize_document(doc):
    # Obsługa ObjectId
    if "production_companies_ids" in doc:
        for i, obj in enumerate(doc["production_companies_ids"]):
            if "$oid" in obj:
                doc["production_companies_ids"][i] = ObjectId(obj["$oid"])

    # Konwersja daty
    if "release_date" in doc:
        date_field = doc["release_date"]
        if isinstance(date_field, dict) and "$date" in date_field:
            date_str = date_field["$date"]
            if isinstance(date_str, str):
                doc["release_date"] = datetime.fromisoformat(date_str.replace("Z", "+00:00"))

    return doc


def main():
    # Połączenie z MongoDB
    client = MongoClient("mongodb://localhost:27017/?directConnection=true")

    db = client["moviesDB"]
    collection = db["moviesCollection"]

    with open("movies.json", "r", encoding="utf-8") as file:
        movies = json.load(file)
    
    # Przekształć dokumenty
    normalized_movies = [normalize_document(m) for m in movies]

    # Wstaw dane
    if normalized_movies:
        collection.insert_many(normalized_movies)
        #collection.insert_one(normalized_movies[0])  # Wstaw tylko pierwszy dokument dla testu
        print(f"Wstawiono {len(normalized_movies)} filmów.")
    else:
        print("Brak danych do wstawienia.")

    # Zamknij połączenie
    client.close()

if __name__ == "__main__":
    main()