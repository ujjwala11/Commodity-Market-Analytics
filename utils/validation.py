import pandas as pd


def validate_dataset(df: pd.DataFrame, dataset_name: str) -> dict:
    """
    Validate a financial dataset and return a summary.

    Parameters
    ----------
    df : pd.DataFrame
        Commodity price dataset.

    dataset_name : str
        Name of the dataset.

    Returns
    -------
    dict
        Summary statistics and validation results.
    """

    summary = {
        "Dataset": dataset_name,
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Start Date": df["Date"].min(),
        "End Date": df["Date"].max(),
        "High >= Low": (df["High"] >= df["Low"]).all(),
        "Zero Volume Days": int((df["Volume"] == 0).sum()),
        "Maximum Close": df["Close"].max(),
        "Minimum Close": df["Close"].min(),
        "Average Close": round(df["Close"].mean(), 2),
    }

    print("=" * 70)
    print(f"DATA VALIDATION REPORT : {dataset_name}")
    print("=" * 70)

    print(f"Shape                : {df.shape}")
    print(f"Date Range           : {summary['Start Date']} → {summary['End Date']}")
    print(f"Missing Values       : {summary['Missing Values']}")
    print(f"Duplicate Rows       : {summary['Duplicate Rows']}")
    print(f"High >= Low          : {summary['High >= Low']}")
    print(f"Zero Volume Days     : {summary['Zero Volume Days']}")
    print(f"Minimum Close Price  : {summary['Minimum Close']:.2f}")
    print(f"Maximum Close Price  : {summary['Maximum Close']:.2f}")
    print(f"Average Close Price  : {summary['Average Close']:.2f}")

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values by Column")
    print(df.isnull().sum())

    print("\nSummary Statistics")
    print(df.describe())

    print("=" * 70)

    return summary