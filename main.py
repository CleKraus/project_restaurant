import logging

import pandas as pd
from fastapi import FastAPI, HTTPException, Query

import src.preprocessing as pp
import src.restaurant_search as rs

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)

# Input data
"""
category = "mexican"
latitude = 39
longitude = -108
"""

csv_path = "data//fast_food_restaurants.csv"

# read the raw csv-file
df = pd.read_csv(csv_path)

# perform the preprocssing steps
df = pp.perform_preprocessing(df)


@app.get("/")
def get_recommendation(
    category: str,
    longitude: float = Query(..., gt=-180, lt=180),
    latitude: float = Query(..., gt=-90, lt=90),
):

    # search for the best restaurant
    df_close = rs.search_restaurant(df, category, longitude, latitude)

    if len(df_close) == 0:
        raise HTTPException(status_code=404, detail="No restaurants found")

    return {
        "restaurant_name": df_close.iloc[0]["name"],
        "address": df_close.iloc[0]["address"],
        "city": df_close.iloc[0]["city"],
        "distance": df_close.iloc[0]["distance"],
        "categories": df_close.iloc[0]["categories"],
    }
