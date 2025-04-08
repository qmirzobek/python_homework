import sqlite3
import csv
import pandas as pd
from pathlib import Path    
current_dir = Path(__file__).resolve(strict=True).parent

# Load chinook.db and read customers table
file=current_dir/"data/chinook.db"
conn = sqlite3.connect(file)
customers_tbl = pd.read_sql_query("SELECT * FROM customers", conn)
invoices_tbl = pd.read_sql_query("SELECT * FROM invoices", conn)
# result = customers_df.head(10)
data_frame_1=pd.merge(customers_tbl,invoices_tbl,how="inner",on="CustomerId")
# print(result)


# Load movie data
movie_df = pd.read_csv(current_dir/"data/movie.csv")

# Create two smaller DataFrames
df1 = movie_df[['director_name', 'color']].drop_duplicates()
df2 = movie_df[['director_name', 'num_critic_for_reviews']].drop_duplicates()

# Left join
left_join = pd.merge(df1, df2, on="director_name", how="left")

# Full outer join
full_outer_join = pd.merge(df1, df2, on="director_name", how="outer")

# Count rows
left_count = len(left_join)
outer_count = len(full_outer_join)


titanic = pd.read_excel(current_dir/"data/titanic.xlsx")

grouped = titanic.groupby("Pclass").agg({
    "Age": "mean",
    "Fare": "sum",
    "PassengerId": "count"  # Assuming PassengerId is unique
}).rename(columns={"PassengerId": "PassengerCount"}).reset_index()

grouped_movies = movie_df.groupby(["color", "director_name"]).agg({
    "num_critic_for_reviews": "sum",
    "duration": "mean"
}).reset_index()








employees = pd.read_csv(current_dir/"data/employee.csv")

# Normalize within each department
employees["Normalized_Salary"] = employees.groupby("DEPARTMENT")["BASE_SALARY"].transform(
    lambda x: (x - x.mean()) / x.std()
)

def classify_duration(duration):
    if pd.isna(duration):
        return "Unknown"
    if duration < 60:
        return "Short"
    elif duration <= 120:
        return "Medium"
    else:
        return "Long"

movie_df["Length_Category"] = movie_df["duration"].apply(classify_duration)


