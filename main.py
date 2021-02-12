import logging

import pandas as pd

import src.preprocessing as pp
import src.select_restaurant as sr

logging.basicConfig(level=logging.DEBUG)

category = "mexican"
lng = -400
lat = 39

csv_path = "data//fast_food_restaurants.csv"

df = pd.read_csv(csv_path)

# run preproccessing
df = pp.run_preprocessing(df)

# find the closest restaurant of the searched category
df_closest = sr.search_restaurant(df, category, lng, lat)

print(df_closest.head())
