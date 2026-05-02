movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "comedy": ["Mr Bean", "The Mask", "Superbad"],
    "romance": ["Titanic", "Notebook", "La La Land"],
    "horror": ["Conjuring", "It", "Nun"]
}

print("Movie Recommendation System")
print("Genres: action, comedy, romance, horror")

genre = input("Enter your favorite genre: ").lower()

if genre in movies:
    print("Recommended movies:")
    for m in movies[genre]:
        print("-", m)
else:
    print("Genre not found")