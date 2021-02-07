import pandas as pd
import pytest

import src.preprocessing as pp
import src.restaurant_search as rs


@pytest.fixture
def initial_data_frame():
    csv_path = "data//fast_food_restaurants.csv"
    df = pd.read_csv(csv_path)
    df = pp.perform_preprocessing(df)
    return df


def test_select_mexican_restaurants(initial_data_frame):

    df_mex = rs.get_restaurants_of_category(initial_data_frame, "mexican")

    assert len(df_mex) == 1117
