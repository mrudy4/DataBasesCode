import redis

def get_songs_from_cache(genre, userN):
    """Sprawdzanie, czy utwory są w pamięci podręcznej Redis."""
    cache_key = f"user:{userN}:genre:{genre}:songs"
    cached_songs = r.get(cache_key)
    
    if cached_songs:
        print("Znaleziono dane w cache.")
        return cached_songs
    else:
        print("Brak danych w cache, pobieram z bazy danych...")
        return None


def set_songs_to_cache(genre, userN, songs):
    """Zapisz dane do pamięci podręcznej Redis na 10 minut."""
    cache_key = f"user:{userN}:genre:{genre}:songs"
    r.setex(cache_key, 600, songs)  # 600 sek = 10 minut
    print("Zapisano dane do cache.")

def pop_songs(userN):
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "Pop":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Zamień listę utworów na format JSON lub string, aby przechować w Redis
    songs_str = str(pop_songs)  # Możesz także użyć JSON, jeśli chcesz

    set_songs_to_cache("Pop", userN, songs_str)  # Zapisz utwory w cache

    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")

def rock_songs(userN):
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "Rock":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Zamień listę utworów na format JSON lub string, aby przechować w Redis
    songs_str = str(pop_songs)  # Możesz także użyć JSON, jeśli chcesz

    set_songs_to_cache("Rock", userN, songs_str)  # Zapisz utwory w cache
    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")

def hip_hop_songs(userN):
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "Hip-Hop":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Zamień listę utworów na format JSON lub string, aby przechować w Redis
    songs_str = str(pop_songs)  # Możesz także użyć JSON, jeśli chcesz

    set_songs_to_cache("Hip-Hop", userN, songs_str)  # Zapisz utwory w cache
    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")

def soul_songs():
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "Soul":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")

def funk_songs():
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "Funk":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")

def RB_songs():
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "R&B":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")

def EDM_songs():
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "EDM":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")

def alternative_songs():
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "Alternative":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")

def cRap_songs():
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "Country Rap":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")

def folk_songs():
    song_keys = r.keys("song:*")
    pop_songs = []
    for key in song_keys:
        genre = r.hget(key, "genre")

        if genre == "Folk":
            song = r.hgetall(key)
            pop_songs.append(song)

    # Wyświetl wyniki
    for song in pop_songs:
        print(f"{song['title']} - {song['artist']}")




def main():
    userN = 0
    print("Co zamierzasz zrobic?")
    work = True

    while work == True:
        
        print("Jaki rodzaj muzyki preferujesz?")
        print("1. Pop")
        print("2. Rock")
        print("3. Hip-Hop")
        print("4. Soul")
        print("5. Funk")
        print("6. R&B")
        print("7. EDM")
        print("8. Alternative")
        print("9. Country Rap")
        print("10. Folk")
        print("11. Wszystkie :)")
        print("12. Ocen swoje ulubione utwory")

        choice = input("Wybierz opcje: ")

        if choice == "1":
            print("Preferujesz Pop")
            print("Oto utwory, które mogą Ci się spodobać:")
            # Sprawdzenie cache przed wywołaniem funkcji
            pop_songs_cache = get_songs_from_cache("Pop", userN)
            if pop_songs_cache:
                print(pop_songs_cache)
            else:
                pop_songs(userN)  # Jeśli brak danych w cache, pobierz je
            
            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "2":
            print("Preferujesz Rock")
            print("Oto utwory, które mogą Ci się spodobać:")

            rock_songs_cache = get_songs_from_cache("Rock", userN)
            if rock_songs_cache:
                print(rock_songs_cache)
            else:
                rock_songs(userN)  # Jeśli brak danych w cache, pobierz je
            
            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "3":
            print("Preferujesz Hip-Hop")
            print("Oto utwory, które mogą Ci się spodobać:")
            
            hip_hop_songs_cache = get_songs_from_cache("Hip-Hop", userN)
            if hip_hop_songs_cache:
                print(hip_hop_songs_cache)
            else:
                hip_hop_songs(userN)  # Jeśli brak danych w cache, pobierz je
            
            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "4":
            print("Preferujesz Soul")
            print("Oto utwory, które mogą Ci się spodobać:")
            soul_songs()


            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")

        elif choice == "5":
            print("Preferujesz Funk")
            print("Oto utwory, które mogą Ci się spodobać:")
            funk_songs()

            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "6":
            print("Preferujesz R&B")
            print("Oto utwory, które mogą Ci się spodobać:")
            RB_songs()

            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "7":
            print("Preferujesz EDM")
            print("Oto utwory, które mogą Ci się spodobać:")
            EDM_songs()
            
            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "8":
            print("Preferujesz Alternative")
            print("Oto utwory, które mogą Ci się spodobać:")
            alternative_songs()

            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "9":
            print("Preferujesz Country Rap")
            print("Oto utwory, które mogą Ci się spodobać:")
            cRap_songs()


            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "10":
            print("Preferujesz Folk")
            print("Oto utwory, które mogą Ci się spodobać:")
            folk_songs()


            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "11":
            print("Preferujesz wszystkie gatunki")
            print("Oto utwory, które mogą Ci się spodobać:")
            pop_songs()
            rock_songs()
            hip_hop_songs()
            soul_songs()
            funk_songs()
            RB_songs()
            EDM_songs()
            alternative_songs()
            cRap_songs()
            folk_songs()

            if server == 0:
                print("Czy chcesz dodać utwór do swojej playlisty? (T/N)")
                add_choice = input("Wybierz opcje: ")

                if add_choice == "T" or add_choice == "t":
                    song_to_add = input("Podaj tytul utworu do dodania: ")
                    r.sadd(f"user:{userN}:playlist", song_to_add)
                    print(f"Utwór '{song_to_add}' został dodany do Twojej playlisty.")
                else:
                    print("Nie dodano utworu do playlisty.")
            else:
                print("Nie można dodać utworu do playlisty, ponieważ jesteś na serwerze replikacyjnym.")
        elif choice == "12":
            print("Oto Twoje ulubione utwory:")
            favorite_songs = r.smembers(f"user:{userN}:playlist")
            if favorite_songs:
                for song in favorite_songs:
                    print(song)

                if server == 0:
                    print("Ktory utwor chcesz ocenic?")
                    song_to_rate = input("Podaj tytul utworu do oceny: ")
                    msg = song_to_rate+f" | user-{userN}"

                    rating = input("Podaj ocene (1-5): ") 
                    r.zadd(f"song_ratings", {msg: rating})  
                    print(f"Utwór '{song_to_rate}' został oceniony na {rating}.")
                    
                    should_show = input("Czy chcesz zobaczyc wszystkie oceny? (T/N)")
                    if should_show == "T" or should_show == "t":
                        print("Oto wszystkie oceny:")
                        data = r.zrevrange("song_ratings", 0, -1, withscores=True)
                        for title, rating in data:
                            print(f"{title:<20} | Rating: {rating}")
                    else:
                        print("Nie pokazano ocen.")

            else:
                print("Nie masz jeszcze ulubionych utworów.")


        elif choice == "X" or choice == "x":
            work = False
            print("Koniec programu")


try:
    r = redis.Redis(host='localhost', port=80, decode_responses=True)
    server = 0
    if __name__ == "__main__":
        main()

except redis.ConnectionError:
    print("Nie można połączyć się z głównym serwerem Redis. Sprawdź konfigurację.")
    print("Próba połączenia z serwerem replikacyjnym Redis...")
    try:
        r = redis.Redis(host='localhost', port=88, decode_responses=True)
        server = 1
        if __name__ == "__main__":
            main()
    except redis.ConnectionError:
        print("Nie można połączyć się z serwerem replikacyjnym Redis. Sprawdź konfigurację.")
