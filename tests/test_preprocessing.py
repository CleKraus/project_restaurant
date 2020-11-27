import pandas as pd
import pytest

import src.preprocessing as pp


@pytest.fixture
def initial_data_frame():
    csv_path = "data//fast_food_restaurants.csv"
    df = pd.read_csv(csv_path)
    return df


def test_2_select_relevant_cols_original_df(initial_data_frame):

    df = pp.select_relevant_columns(initial_data_frame)
    print("Test 2")
    assert len(df.columns) == 8


def test_3_error_select_relevant_cols():

    df = pd.DataFrame({"a": range(10)})
    print("Test 3")
    with pytest.raises(KeyError):
        pp.select_relevant_columns(df)


def test_1_ensure_length_compatibility_df(initial_data_frame):

    df_pp = pp.select_relevant_columns(initial_data_frame)
    print("Test 1")
    assert len(initial_data_frame) == len(df_pp)
