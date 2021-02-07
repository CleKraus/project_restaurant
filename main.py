import logging

import pandas as pd

import src.preprocessing as pp
import src.restaurant_search as rs

logging.basicConfig(level=logging.DEBUG)

# Input data
category = "mexican"
latitude = 39
longitude = -108


csv_path = "data//fast_food_restaurants.csv"

# read the raw csv-file
df = pd.read_csv(csv_path)

# perform the preprocssing steps
df = pp.perform_preprocessing(df)

# search for the best restaurant
df_close = rs.search_restaurant(df, category, longitude, latitude)

print(df_close)
