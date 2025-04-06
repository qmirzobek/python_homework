import pandas as pd

# 1. iris.json
iris_df = pd.read_json("iris.json")
iris_df.columns = iris_df.columns.str.lower()
iris_selected = iris_df[["sepal_length", "sepal_width"]]
print("Selected Iris columns:\n", iris_selected.head())

# 2. titanic.xlsx
titanic_df = pd.read_excel("titanic.xlsx")
titanic_over_30 = titanic_df[titanic_df["Age"] > 30]
print("\nPassengers over 30:\n", titanic_over_30.head())

gender_counts = titanic_df["Sex"].value_counts()
print("\nGender counts:\n", gender_counts)

# 3. Flights parquet
try:
    flights_df = pd.read_parquet("flights.parquet")  # Requires pyarrow or fastparquet
    selected_flights = flights_df[["origin", "dest", "carrier"]]
    print("\nSelected Flights columns:\n", selected_flights.head())

    unique_destinations = flights_df["dest"].nunique()
    print("\nNumber of unique destinations:", unique_destinations)
except Exception as e:
    print("\nCould not read flights.parquet:", e)

# 4. movie.csv
movie_df = pd.read_csv("movie.csv")
long_movies = movie_df[movie_df["duration"] > 120]
sorted_movies = long_movies.sort_values(by="director_facebook_likes", ascending=False)
print("\nSorted long movies:\n", sorted_movies[["movie_title", "duration", "director_facebook_likes"]].head())
