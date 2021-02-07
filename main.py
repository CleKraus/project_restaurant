import pandas as pd

import src.preprocessing as pp
import src.restaurant_search as rs

csv_path = "data//fast_food_restaurants.csv"

# read the raw csv-file
df = pd.read_csv(csv_path)

# perform the preprocssing steps
df = pp.perform_preprocessing(df)

# search for the best restaurant
df_mex = rs.get_restaurants_of_category(df, "mexican")
