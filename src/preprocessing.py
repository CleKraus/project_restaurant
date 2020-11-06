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