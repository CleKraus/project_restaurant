import pandas as pd


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

    df_cat = df[df["categories"].map(lambda x: category.lower() in x.lower())].copy()

    return df_cat
