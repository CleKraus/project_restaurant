import logging

import pandas as pd

import src.preprocessing as pp
import src.select_restaurant as sr

logging.basicConfig(level=logging.DEBUG)

csv_path = "data//fast_food_restaurants.csv"

df = pd.read_csv(csv_path)

# run preproccessing
df = pp.run_preprocessing(df)


df_cat = sr.get_restaurant_of_category(df, "mexican")


print(df_cat.head())
