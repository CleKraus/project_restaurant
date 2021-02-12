import logging

import pandas as pd

import src.helper as hlp


def get_restaurant_of_category(df: pd.DataFrame, category: str) -> pd.DataFrame:
    """
    Given a table of restaurants *df* as well as a category we are looking for, function
    returns all restaurants of the *category*.

    Args:
        df (pd.DataFrame): DataFrame containing restaurants. Needs to contain at
                           least the column *categories*
        category (str): Category we are looking for

    Returns:
        pd.DataFrame: DataFrame containing all restaurants of category *category*
    """

    assert "categories" in df.columns

    df_cat = df[df["categories"].map(lambda x: category.lower() in x.lower())].copy()

    return df_cat


def get_closest_restaurant(df: pd.DataFrame, lng: float, lat: float) -> pd.DataFrame:
    """
    Given a user position, return the closest restaurant out of the restaurants in *df*

    Args:
        df (pd.DataFrame): Table of restaurants
        lng (float): Longitude of user's current position
        lat (float): Latitude of user's current position

    Returns:
        pd.DataFrame: DataFrame contianing the closest restaurant
    """

    assert "longitude" in df.columns
    assert "latitude" in df.columns

    df_dist = df.copy()

    df_dist["distance"] = hlp.haversine_np(
        df_dist["longitude"], df_dist["latitude"], lng, lat
    )

    # sort restaurants by distance
    df_dist.sort_values("distance", inplace=True)

    logging.debug(
        f"Distance to closest restaurant is {min(df_dist['distance']): .2f} km"
    )

    # return the closest resturant
    return df_dist.head(1)


def search_restaurant(
    df: pd.DataFrame, category: str, lng: float, lat: float
) -> pd.DataFrame:
    """
    Function to search the closest restaurant of type *category*

    Args:
        df (pd.DataFrame): Tbale with restaurants
        category (str): Category to be searched for
        lng (float): Latitude
        lat (float): Longitude

    Returns:
        pd.DataFrame: DataFrame with the closest restaurant of searched *category*
    """

    df_cat = get_restaurant_of_category(df, category)

    if len(df_cat) == 0:
        logging.warning(f"No restaurants of category {category} found")
        return df_cat
    else:
        df_close = get_closest_restaurant(df_cat, lng, lat)
        return df_close
