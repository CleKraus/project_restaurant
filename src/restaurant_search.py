import logging

import pandas as pd

import src.helper as hlp


def get_restaurants_of_category(df: pd.DataFrame, category: str) -> pd.DataFrame:
    """
    Given a table of restaurants as well as a category we are looking for, function
    returns all the restaurants of the searched category.

    Args:
        df (pd.DataFrame): DataFrame containing restaurants. Needs to contain at least
                           the column *categories*
        category (str): Category we are looking for

    Returns:
        pd.DataFrame: DataFrame of all restaurants of category we are looking for
    """

    logging.info("Searching for restaurants in categories")

    df_cat = df[df["categories"].map(lambda x: category.lower() in x.lower())].copy()

    logging.debug(f"{len(df_cat)} restaurants of category {category} remaining")

    return df_cat


def get_closest_restaurant(df: pd.DataFrame, lng: float, lat: float) -> pd.DataFrame:
    """
    Given a DataFrame with geo-coordinates, function returns the row with minimal
    distance to *lng* and *lat*.

    Args:
        df (pd.DataFrame): DataFrame containing at least the columns *longitude*
                           and *latitude*
        lng (float): Longitude of the current position
        lat (float): Latitude of the current position

    Returns:
        pd.DataFrame: DataFrame of length 1 containing only the closest restaurant
                      (if > 1 restaurant with same minimal distance, one is
                      randomly selected)
    """

    assert "longitude" in df.columns
    assert "latitude" in df.columns

    df_dist = df.copy()

    df_dist["distance"] = hlp.haversine_np(
        df_dist["longitude"], df_dist["latitude"], lng, lat
    )

    df_dist.sort_values("distance", inplace=True)

    logging.debug(
        f"Distance to closest restaurant is {min(df_dist['distance']): .2f} km"
    )

    return df_dist.head(1)


def search_restaurant(
    df: pd.DataFrame, category: str, lng: float, lat: float
) -> pd.DataFrame:
    """
    Search the closest restaurant of category *category*

    Args:
        df (pd.DataFrame): DataFrame containing all restaurants
        category (str): Category of restaurant the user is searching for
        lng (float): Longitude of the user's current position
        lat (float): Latitude of the user's current position

    Returns:
        pd.DataFrame: DataFrame containing the closest restaurant of *category*
                      (can be empty)
    """

    logging.info("Searching for the proposed restaurant")

    df_cat = get_restaurants_of_category(df, category)

    if len(df_cat) == 0:
        logging.warning(f"No restaurant of category {category} found")
        return df_cat
    else:
        df_close = get_closest_restaurant(df, lng, lat)
        return df_close
