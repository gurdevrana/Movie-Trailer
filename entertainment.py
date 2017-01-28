import media
import fresh_tomatoes

#  Intialization of objects of class movie in media.py

ironman = media.movie(
        "IronMan 3", "Tony Stark encounters a formidable foe called"
        "the Mandarin.After failing to defeat this enemy"
        ",he embarks on a journey",
        "https://upload.wikimedia.org/wikipedia/en/d/d5/"
        "Iron_Man_3_theatrical_poster.jpg",
        "https://www.youtube.com/watch?v=oYSD2VQagc4")

batman = media.movie(
        "Batman the dark knight", "Batman has a new foe,the Joker,"
        "who is anaccomplished criminal hell-bent on "
        "decimating Gotham City.",
        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

inception = media.movie(
            "Inception", "Cobb steals information from his targets by"
            "entering their dreams.He is wanted for his alleged role"
            "in his wife's murder and his only "
            "chance at redemption is to perform inception",
            "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_"
            "%282010%29_theatrical_poster.jpg",
            "https://www.youtube.com/watch?v=YoHD9XEInc0")

spiderman = media.movie(
            "The amazing spiderman 2", "Peter Parker fights crime "
            "as Spider-Man in Manhattan. Oscorp,owned by his "
            "childhood friend, Harry Osborn",
            "https://upload.wikimedia.org/wikipedia/en/0/02/The_"
            "Amazing_Spiderman_2_poster.jpg",
            "https://www.youtube.com/watch?v=DlM2CWNTQ84")

thor = media.movie(
    "thor", "Thor is exiled by his father Odin, the King of Asgard,"
    "to the Earth to live among mortals.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
    "https://www.youtube.com/watch?v=npvJ9FTgZbM")

aos = media.movie(
    "agents of shield", "Agent Phil leads team of highly skilled agents"
    "from the global law-enforcement organisation known as S.H.I.E.L.D. "
    "Together, they combat extraordinary and inexplicable threats.",
    "https://upload.wikimedia.org/wikipedia/en/6/6a/Agents_of_SHIELD_logo.jpg",
    "https://www.youtube.com/watch?v=T3T-evQZiQo")

#  list of objects of class movie is stored in movies
movies = [ironman, batman, inception, spiderman, thor, aos]

#  fresh_tomatoes open function is called and movies is passed as a agrument
fresh_tomatoes.open_movies_page(movies)
