import pandas as pd


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
