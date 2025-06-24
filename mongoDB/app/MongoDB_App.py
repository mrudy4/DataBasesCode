from pymongo import MongoClient

# Połączenie z MongoDB
#client = MongoClient("mongodb://localhost:27017/?directConnection=true")
client = MongoClient('mongodb://mongo1:27017,mongo2:27017,mongo3:27017/moviesDB?replicaSet=rs0')
db = client["moviesDB"]
collection = db["moviesCollection"]
# # Wywołanie isMaster, by sprawdzić status węzła
# node_status = client.admin.command('isMaster')
# print("Szczegóły statusu węzła:", node_status)
# # Wyświetlenie informacji o węźle
# if node_status['ismaster']:
#     print("Jesteś połączony z węzłem PRIMARY.")
# else:
#     print(f"Jesteś połączony z węzłem SECONDARY. Węzeł: {node_status['primary']}")

def add_movie():
    title = input("Podaj tytuł filmu: ")
    budget = int(input("Podaj budżet (liczba): "))
    revenue = int(input("Podaj przychód (liczba): "))
    
    actors = []
    while True:
        actor = input("Podaj nazwisko aktora (lub ENTER, aby zakończyć): ")
        if not actor:
            break
        character = input(f"Podaj postać graną przez {actor}: ")
        actors.append({"Actor": actor, "Character": character})

    movie = {
        "title": title,
        "budget": { "Amount": budget },
        "revenue": { "Amount": revenue },
        "starring": actors
    }

    collection.insert_one(movie)
    print("✅ Film dodany.")

def delete_movie():
    title = input("Podaj tytuł filmu do usunięcia: ")
    result = collection.delete_one({ "title": title })
    if result.deleted_count:
        print("🗑️ Film usunięty.")
    else:
        print("⚠️ Nie znaleziono filmu.")

def edit_movie():
    title = input("Podaj tytuł filmu do edycji: ")
    movie = collection.find_one({ "title": title })
    if not movie:
        print("⚠️ Nie znaleziono filmu.")
        return

    new_title = input(f"Nowy tytuł (ENTER by zostawić '{title}'): ") or title
    new_budget = input("Nowy budżet (ENTER by zostawić obecny): ")
    new_revenue = input("Nowy przychód (ENTER by zostawić obecny): ")

    update = {
        "title": new_title,
        "budget": { "Amount": int(new_budget) } if new_budget else movie["budget"],
        "revenue": { "Amount": int(new_revenue) } if new_revenue else movie["revenue"],
    }

    collection.update_one({ "title": title }, { "$set": update })
    print("✏️ Film zaktualizowany.")

def search_movies_text():
    phrase = input("\n🔍 Podaj frazę do wyszukania (full-text search): ").strip()
    if not phrase:
        print("⚠️ Nie podano frazy.")
        return

    query = { "$text": { "$search": phrase } }
    projection = {
        "title": 1,
        "budget.Amount": 1,
        "revenue.Amount": 1,
        "starring": 1,
        "tagline": 1,
        "_id": 0,
        "score": { "$meta": "textScore" }
    }

    movies = collection.find(query, projection).sort([("score", { "$meta": "textScore" })])

    found = False
    for movie in movies:
        found = True
        print(f"\n🎬 Tytuł: {movie.get('title', 'Brak')} (score: {movie.get('score'):.2f})")
        print(f"🎬 Tagline: {movie.get('tagline', 'Brak')}")
        print(f"   Budżet: {movie.get('budget', {}).get('Amount', 'Brak')}")
        print(f"   Przychód: {movie.get('revenue', {}).get('Amount', 'Brak')}")
        if "starring" in movie:
            print("   Aktorzy:")
            for star in movie["starring"]:
                print(f"     - {star.get('Actor', '?')} jako {star.get('Character', '?')}")
        print("-" * 40)

    if not found:
        print("🚫 Nie znaleziono filmów dopasowanych do frazy.")

def main():

    while True:
        print("\nWybierz operację:")
        print("1. Dodaj film")
        print("2. Usuń film")
        print("3. Edytuj film")
        print("4. Wyświetl filmy")
        print("5. Wyjście")
        choice = input("Opcja: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            delete_movie()
        elif choice == "3":
            edit_movie()
        elif choice == "4":
            search_movies_text()
        elif choice == "5":
            print("👋 Do widzenia!")
            break
        else:
            print("❌ Nieprawidłowy wybór.")

    # Zamknij połączenie
    client.close()


if __name__ == "__main__":
    main()
