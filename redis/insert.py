import redis
import random

r = redis.Redis(host='172.19.0.2', port=6379, decode_responses=True)

# Lista użytkowników
users = [f"user:{i}" for i in range(50)]

# Lista utworów (50) z rzeczywistymi nazwami
songs = [
    {"id": "song:1", "title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop"},
    {"id": "song:2", "title": "Bohemian Rhapsody", "artist": "Queen", "genre": "Rock"},
    {"id": "song:3", "title": "Shape of You", "artist": "Ed Sheeran", "genre": "Pop"},
    {"id": "song:4", "title": "Smells Like Teen Spirit", "artist": "Nirvana", "genre": "Rock"},
    {"id": "song:5", "title": "Billie Jean", "artist": "Michael Jackson", "genre": "Pop"},
    {"id": "song:6", "title": "Rolling in the Deep", "artist": "Adele", "genre": "Soul"},
    {"id": "song:7", "title": "Lose Yourself", "artist": "Eminem", "genre": "Hip-Hop"},
    {"id": "song:8", "title": "Humble", "artist": "Kendrick Lamar", "genre": "Hip-Hop"},
    {"id": "song:9", "title": "Bad Guy", "artist": "Billie Eilish", "genre": "Pop"},
    {"id": "song:10", "title": "Levitating", "artist": "Dua Lipa", "genre": "Pop"},
    {"id": "song:11", "title": "Radioactive", "artist": "Imagine Dragons", "genre": "Alternative"},
    {"id": "song:12", "title": "Peaches", "artist": "Justin Bieber", "genre": "R&B"},
    {"id": "song:13", "title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "genre": "Funk"},
    {"id": "song:14", "title": "Shake It Off", "artist": "Taylor Swift", "genre": "Pop"},
    {"id": "song:15", "title": "Halo", "artist": "Beyoncé", "genre": "Pop"},
    {"id": "song:16", "title": "Can't Stop", "artist": "Red Hot Chili Peppers", "genre": "Rock"},
    {"id": "song:17", "title": "Seven Nation Army", "artist": "The White Stripes", "genre": "Alternative"},
    {"id": "song:18", "title": "Someone Like You", "artist": "Adele", "genre": "Soul"},
    {"id": "song:19", "title": "Stay", "artist": "The Kid LAROI & Justin Bieber", "genre": "Pop"},
    {"id": "song:20", "title": "As It Was", "artist": "Harry Styles", "genre": "Pop"},
    {"id": "song:21", "title": "Starboy", "artist": "The Weeknd", "genre": "Pop"},
    {"id": "song:22", "title": "Sunflower", "artist": "Post Malone", "genre": "Hip-Hop"},
    {"id": "song:23", "title": "Lucid Dreams", "artist": "Juice WRLD", "genre": "Hip-Hop"},
    {"id": "song:24", "title": "Goosebumps", "artist": "Travis Scott", "genre": "Hip-Hop"},
    {"id": "song:25", "title": "All of Me", "artist": "John Legend", "genre": "R&B"},
    {"id": "song:26", "title": "Clocks", "artist": "Coldplay", "genre": "Alternative"},
    {"id": "song:27", "title": "Don't Start Now", "artist": "Dua Lipa", "genre": "Pop"},
    {"id": "song:28", "title": "Thinking Out Loud", "artist": "Ed Sheeran", "genre": "Pop"},
    {"id": "song:29", "title": "Happy", "artist": "Pharrell Williams", "genre": "Funk"},
    {"id": "song:30", "title": "Toxic", "artist": "Britney Spears", "genre": "Pop"},
    {"id": "song:31", "title": "In the End", "artist": "Linkin Park", "genre": "Rock"},
    {"id": "song:32", "title": "Stressed Out", "artist": "Twenty One Pilots", "genre": "Alternative"},
    {"id": "song:33", "title": "Circles", "artist": "Post Malone", "genre": "Pop"},
    {"id": "song:34", "title": "Savage Love", "artist": "Jawsh 685 & Jason Derulo", "genre": "Pop"},
    {"id": "song:35", "title": "Take Me to Church", "artist": "Hozier", "genre": "Soul"},
    {"id": "song:36", "title": "Old Town Road", "artist": "Lil Nas X", "genre": "Country Rap"},
    {"id": "song:37", "title": "Bad Habits", "artist": "Ed Sheeran", "genre": "Pop"},
    {"id": "song:38", "title": "Heat Waves", "artist": "Glass Animals", "genre": "Alternative"},
    {"id": "song:39", "title": "MONTERO (Call Me By Your Name)", "artist": "Lil Nas X", "genre": "Pop"},
    {"id": "song:40", "title": "Faded", "artist": "Alan Walker", "genre": "EDM"},
    {"id": "song:41", "title": "Believer", "artist": "Imagine Dragons", "genre": "Alternative"},
    {"id": "song:42", "title": "Sicko Mode", "artist": "Travis Scott", "genre": "Hip-Hop"},
    {"id": "song:43", "title": "Demons", "artist": "Imagine Dragons", "genre": "Alternative"},
    {"id": "song:44", "title": "Break My Heart", "artist": "Dua Lipa", "genre": "Pop"},
    {"id": "song:45", "title": "Rockstar", "artist": "Post Malone", "genre": "Hip-Hop"},
    {"id": "song:46", "title": "Watermelon Sugar", "artist": "Harry Styles", "genre": "Pop"},
    {"id": "song:47", "title": "My Universe", "artist": "Coldplay & BTS", "genre": "Pop"},
    {"id": "song:48", "title": "Call Out My Name", "artist": "The Weeknd", "genre": "R&B"},
    {"id": "song:49", "title": "Before You Go", "artist": "Lewis Capaldi", "genre": "Pop"},
    {"id": "song:50", "title": "Let Her Go", "artist": "Passenger", "genre": "Folk"},
]

# Zapis informacji o utworach jako hash
for song in songs:
    r.hset(song["id"], mapping={
        "title": song["title"],
        "artist": song["artist"],
        "genre": song["genre"]
    })
'''
# Zbiory gatunków
genres = set(song["genre"] for song in songs)

# Historia odtwarzania użytkowników (listy)
for user in users:
    for _ in range(10):
        song_id = random.choice(songs)["id"]
        r.lpush(f"{user}:history", song_id)

# Ulubione gatunki (zbiory)
for user in users:
    r.sadd(f"{user}:genres", *random.sample(list(genres), 3))

# Ranking najpopularniejszych utworów (zbiory posortowane)
'''
'''
for song in songs:
    r.zadd("song:ranking", {song["id"]: random.randint(50, 1000)})
'''
'''

# Ulubione utwory użytkowników (zbiory)
for user in users:
    r.sadd(f"{user}:favorites", *[random.choice(songs)["id"] for _ in range(5)])
'''