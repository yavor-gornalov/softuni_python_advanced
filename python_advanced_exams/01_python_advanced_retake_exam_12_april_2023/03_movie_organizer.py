# https://judge.softuni.org/Contests/Practice/Index/3893#2

def movie_organizer(*args):
    movies = {}
    for movie in args:
        movie_name, genre = movie
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie_name)

    genres_sorted = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for genre, movie_data in genres_sorted:
        result += f"{genre} - {len(movie_data)}\n"
        for name in sorted(movie_data):
            result += f"* {name}\n"

    return result


# tests
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
