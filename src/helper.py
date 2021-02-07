import numpy as np
import pandas as pd


def haversine_np(
    lon1: pd.Series, lat1: pd.Series, lon2: float, lat2: float
) -> pd.Series:
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.

    Function from
    https://stackoverflow.com/questions/29545704/fast-haversine-approximation-python-pandas
    """

    lon2 = np.array([lon2] * len(lon1))
    lat2 = np.array([lat2] * len(lat1))

    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km
