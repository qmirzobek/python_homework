import pandas as pd
import sqlite3

# Load chinook.db and read customers table
conn = sqlite3.connect("/mnt/data/chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
customers_preview = customers_df.head(10)

# Load iris.json
iris_df = pd.read_json("/mnt/data/iris.json")
iris_shape = iris_df.shape
iris_columns = iris_df.columns.tolist()

# Load titanic.xlsx
titanic_df = pd.read_excel("/mnt/data/titanic.xlsx")
titanic_preview = titanic_df.head()

# Load movie.csv
movie_df = pd.read_csv("/mnt/data/movie.csv")
movie_sample = movie_df.sample(10, random_state=1)

(customers_preview, iris_shape, iris_columns, titanic_preview, movie_sample)
