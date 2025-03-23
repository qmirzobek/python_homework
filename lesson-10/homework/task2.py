import requests
import os
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def get_genre_id(genre_name):
    """Fetch genre ID from TMDb based on genre name."""
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url).json()
    
    for genre in response["genres"]:
        if genre["name"].lower() == genre_name.lower():
            return genre["id"]
    return None

def get_movies_by_genre(genre_id):
    """Fetch movies of a specific genre."""
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url).json()
    return response["results"]

def recommend_movie():
    """Ask the user for a genre and recommend a random movie."""
    genre_name = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
    genre_id = get_genre_id(genre_name)

    if genre_id is None:
        print("Genre not found. Please try again.")
        return
    
    movies = get_movies_by_genre(genre_id)

    if not movies:
        print("No movies found for this genre.")
        return

    movie = random.choice(movies)
    print(f"\nRecommended Movie: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Release Date: {movie['release_date']}")

recommend_movie()
