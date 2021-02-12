import logging

import pandas as pd


def select_relevant_columns(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """
    Select relevant columns of the passed data frame *df*

    Args:
        df (pd.core.frame.DataFrame): Data frame for which columns should be selected

    Raises:
        KeyError: Raises error if not all columns are in data frame

    Returns:
        pd.core.frame.DataFrame: Small data frame only containing relevant columns
    """
    rel_cols = [
        "name",
        "address",
        "postalCode",
        "city",
        "latitude",
        "longitude",
        "categories",
    ]

    try:
        df = df[rel_cols].copy()
    except KeyError:

        msg = f"""
               Data needs to have at least
               the following columns: {', '.join(rel_cols)}
               """

        raise KeyError(msg)

    return df


def remove_restaurant_wo_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function removes restaurants without category.

    Args:
        df (pd.DataFrame): DataFrame containing all restaurants. Needs to
                           contain at least the column *categories*

    Returns:
        pd.DataFrame: DataFrame containing restaurants with category only
    """

    assert "categories" in df.columns

    len_before = len(df)
    df = df[df["categories"].notnull()].copy()
    logging.info(f"Deleted {len_before - len(df)} restaurants as they had no category")

    return df


def run_preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to run preprocessing steps:

    1. Select relevant columns
    2. Delete restaurants w/o category


    Args:
        df (pd.DataFrame): Table with raw restaurant data

    Returns:
        pd.DataFrame: Preprocessed restaurant data
    """

    logging.info("Running preprocessing steps")

    df = select_relevant_columns(df)
    df = remove_restaurant_wo_category(df)

    return df
