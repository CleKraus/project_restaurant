import logging

import pandas as pd

logging.basicConfig(level=logging.DEBUG)


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

    logging.info("Selecting relevant columns")

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


def delete_restaurants_wo_category(
    df: pd.core.frame.DataFrame
) -> pd.core.frame.DataFrame:
    """
    Delete all the restaurants for which there is no category

    Args:
        df (pd.DataFrame): DataFrame containing all the restaurants

    Returns:
        pd.core.frame.DataFrame: Table containing restaurants with category
    """

    logging.info("Deleting restaurants wo category")

    assert "categories" in df.columns

    nb_rest = len(df)
    df = df[df["categories"].notnull()].copy()

    logging.debug(f"Deleted {nb_rest - len(df)} restaurants which had no category")
    return df


def perform_preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to perform several preprocessing steps:

    1. Collection of only the relevant columns
    2. Deletion of restaurants w/o category

    Args:
        df (pd.DataFrame): DataFrame containing all restaurants and
                           at least the column *categories*

    Returns:
        pd.DataFrame: Preprocessed restaurant data
    """

    logging.info("Running preprocessing steps")

    assert "categories" in df.columns

    # select the relevant columns only
    df = select_relevant_columns(df)

    # delete restaurants that do not have categories
    df = delete_restaurants_wo_category(df)

    return df
