import pandas as pd

iris_df = pd.read_json('iris.json')
titanic_df = pd.read_excel('titanic.xlsx')
movie_df = pd.read_csv('movie.csv')
flights_df = pd.read_parquet('flights.parquet')


# Mean, Median, Standard Deviation of numerical columns
iris_stats = iris_df.describe().loc[['mean', 'std']].T
iris_stats['median'] = iris_df.median(numeric_only=True)
print(iris_stats)


# Min, Max, Sum of passenger ages
print("Minimum Age:", titanic_df['Age'].min())
print("Maximum Age:", titanic_df['Age'].max())
print("Sum of Ages:", titanic_df['Age'].sum())

# 1. Director with highest total director_facebook_likes
top_director = movie_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
top_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum().max()
print(f"Top Director: {top_director} with {top_likes} total likes")

# 2. Top 5 longest movies and their directors
top_5_longest = movie_df[['movie_title', 'director_name', 'duration']].sort_values(by='duration', ascending=False).head(5)
print(top_5_longest)

# Check for missing values
missing_summary = flights_df.isnull().sum()
print("Missing values per column:\n", missing_summary)

# Fill a numerical column’s missing values with mean
# Example using 'air_time' (you can replace it with any other numeric column in your dataset)
if 'air_time' in flights_df.columns:
    flights_df['air_time'] = flights_df['air_time'].fillna(flights_df['air_time'].mean())
    print("Filled missing values in 'air_time' column with mean.")
else:
    print("'air_time' column not found. Please replace with an existing numeric column.")
