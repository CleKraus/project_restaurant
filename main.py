import pandas as pd

import src.preprocessing as pp

csv_path = "data//fast_food_restaurants.csv"

df = pd.read_csv(csv_path)

df = pp.select_relevant_columns(df)

print(df.head())
