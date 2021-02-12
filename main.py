import logging

import pandas as pd
from fastapi import FastAPI, HTTPException, Query

import src.preprocessing as pp
import src.select_restaurant as sr

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

csv_path = "data//fast_food_restaurants.csv"

df = pd.read_csv(csv_path)

# run preproccessing
df = pp.run_preprocessing(df)


@app.get("/")
def get_recommendation(
    category: str,
    longitude: float = Query(..., gt=-180, lt=180),
    latitude: float = Query(..., gt=-90, lt=90),
):

    # find the closest restaurant of the searched category
    df_closest = sr.search_restaurant(df, category, longitude, latitude)

    # raise an error if no restaurant were found
    if len(df_closest) == 0:
        raise HTTPException(status_code=404, detail="No restaurants found")

    dict_out = {
        "restaurant_name": df_closest.iloc[0]["name"],
        "address": df_closest.iloc[0]["address"],
        "city": df_closest.iloc[0]["city"],
        "distance": df_closest.iloc[0]["distance"],
        "categories": df_closest.iloc[0]["categories"],
    }
    return dict_out
