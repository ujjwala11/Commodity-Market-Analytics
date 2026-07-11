from pathlib import Path
import pandas as pd

# Project root (commodity-analytics/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# data/raw directory
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

def load_data(filename: str) -> pd.DataFrame:
    """
    Load a single commodity dataset.
    """

    filepath = RAW_DATA_PATH / f"{filename}.csv"

    if not filepath.exists():
        raise FileNotFoundError(
            f"Dataset not found: {filepath}\n"
            "Make sure the CSV exists inside data/raw/"
        )

    df = pd.read_csv(filepath)

    df["Date"] = pd.to_datetime(df["Date"])

    df = (
        df
        .sort_values("Date")
        .set_index("Date")
    )

    return df

def load_all_data():
    """
    Load all commodity datasets.

    Returns
    -------
    dict
    """

    commodities = {
        "gold": load_data("gold"),
        "silver": load_data("silver"),
        "crude_oil": load_data("crude_oil"),
        "natural_gas": load_data("natural_gas"),
        "copper": load_data("copper"),
    }

    return commodities

from functools import reduce


def merge_commodities(data_dict: dict) -> pd.DataFrame:
    """
    Merge closing prices of all commodities.

    Parameters
    ----------
    data_dict : dict

    Returns
    -------
    pd.DataFrame
    """

    dfs = []

    for name, df in data_dict.items():

        temp = df[["Close"]].copy()

        temp = temp.reset_index() 

        temp.rename(columns={"Close": name}, inplace=True)

        dfs.append(temp)

    merged = reduce(
        lambda left, right:
        pd.merge(left, right, on="Date", how="outer"),
        dfs
    )

    merged.sort_values("Date", inplace=True)

    merged.reset_index(drop=True, inplace=True)

    return merged