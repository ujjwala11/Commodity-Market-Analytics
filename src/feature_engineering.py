import pandas as pd
import numpy as np


def add_lag_features(
    df,
    lags=[1, 7, 14, 30],
    price_column="Close"
):
    """
    Add lag features.

    Parameters
    ----------
    df : pd.DataFrame

    lags : list
        Previous trading days.

    price_column : str

    Returns
    -------
    pd.DataFrame
    """

    df = df.copy()

    for lag in lags:

        df[f"Lag_{lag}"] = (
            df[price_column]
            .shift(lag)
        )

    return df


def add_rolling_features(
    df,
    price_column="Close",
    windows=[7, 30]
):

    df = df.copy()

    for window in windows:

        df[f"RollingMean_{window}"] = (
            df[price_column]
            .rolling(window)
            .mean()
        )

        df[f"RollingStd_{window}"] = (
            df[price_column]
            .rolling(window)
            .std()
        )

        df[f"RollingMax_{window}"] = (
            df[price_column]
            .rolling(window)
            .max()
        )

        df[f"RollingMin_{window}"] = (
            df[price_column]
            .rolling(window)
            .min()
        )

    return df


def add_momentum_features(
    df,
    price_column="Close",
    periods=[5,10,30]
):

    df = df.copy()

    for period in periods:

        df[f"Momentum_{period}"] = (
            df[price_column]
            .pct_change(period)
        )

    return df


def add_rsi(
    df,
    price_column="Close",
    window=14
):

    df = df.copy()

    delta = df[price_column].diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)


    avg_gain = (
        gain
        .rolling(window)
        .mean()
    )

    avg_loss = (
        loss
        .rolling(window)
        .mean()
    )


    rs = avg_gain / avg_loss


    df["RSI"] = (
        100 -
        (100 / (1 + rs))
    )

    return df

def add_macd(
    df,
    price_column="Close"
):

    df = df.copy()


    ema12 = (
        df[price_column]
        .ewm(span=12, adjust=False)
        .mean()
    )


    ema26 = (
        df[price_column]
        .ewm(span=26, adjust=False)
        .mean()
    )


    df["MACD"] = ema12 - ema26


    df["MACD_Signal"] = (
        df["MACD"]
        .ewm(span=9, adjust=False)
        .mean()
    )


    df["MACD_Hist"] = (
        df["MACD"]
        -
        df["MACD_Signal"]
    )


    return df

def add_bollinger_bands(
    df,
    price_column="Close",
    window=20
):

    df = df.copy()


    rolling_mean = (
        df[price_column]
        .rolling(window)
        .mean()
    )


    rolling_std = (
        df[price_column]
        .rolling(window)
        .std()
    )


    df["BB_Middle"] = rolling_mean


    df["BB_Upper"] = (
        rolling_mean
        +
        2*rolling_std
    )


    df["BB_Lower"] = (
        rolling_mean
        -
        2*rolling_std
    )


    df["BB_Width"] = (
        df["BB_Upper"]
        -
        df["BB_Lower"]
    )


    return df

def add_volatility_features(
    df,
    price_column="Close",
    windows=[7,30]
):

    df = df.copy()


    returns = (
        df[price_column]
        .pct_change()
    )


    for window in windows:

        df[f"Volatility_{window}"] = (
            returns
            .rolling(window)
            .std()
            *
            np.sqrt(252)
        )


    return df

def add_calendar_features(df):

    df = df.copy()


    df["Year"] = df.index.year

    df["Month"] = df.index.month

    df["Quarter"] = df.index.quarter

    df["DayOfWeek"] = df.index.dayofweek


    return df

import numpy as np
import pandas as pd


def add_trend_features(df):

    df = df.copy()


    # =========================
    # Moving averages
    # =========================

    df["EMA_7"] = (
        df["Close"]
        .ewm(span=7)
        .mean()
    )


    df["EMA_21"] = (
        df["Close"]
        .ewm(span=21)
        .mean()
    )


    df["EMA_50"] = (
        df["Close"]
        .ewm(span=50)
        .mean()
    )


    # EMA crossover

    df["EMA_Crossover"] = (
        df["EMA_7"] -
        df["EMA_21"]
    )


    # =========================
    # RSI
    # =========================

    delta = df["Close"].diff()


    gain = delta.clip(lower=0)

    loss = (
        -delta.clip(upper=0)
    )


    avg_gain = (
        gain
        .rolling(14)
        .mean()
    )

    avg_loss = (
        loss
        .rolling(14)
        .mean()
    )


    rs = avg_gain / avg_loss


    df["RSI_14"] = (
        100 -
        (100/(1+rs))
    )


    # =========================
    # MACD
    # =========================

    ema12 = (
        df["Close"]
        .ewm(span=12)
        .mean()
    )


    ema26 = (
        df["Close"]
        .ewm(span=26)
        .mean()
    )


    df["MACD"] = (
        ema12 -
        ema26
    )


    df["MACD_Signal"] = (
        df["MACD"]
        .ewm(span=9)
        .mean()
    )


    # =========================
    # ATR
    # =========================

    high_low = (
        df["High"]
        -
        df["Low"]
    )


    high_close = (
        abs(
            df["High"]
            -
            df["Close"].shift()
        )
    )


    low_close = (
        abs(
            df["Low"]
            -
            df["Close"].shift()
        )
    )


    tr = pd.concat(
        [
            high_low,
            high_close,
            low_close
        ],
        axis=1
    ).max(axis=1)


    df["ATR_14"] = (
        tr
        .rolling(14)
        .mean()
    )


    # =========================
    # Price position
    # =========================


    df["Price_vs_MA30"] = (
        df["Close"]
        /
        df["RollingMean_30"]
    )


    df["Price_vs_MA7"] = (
        df["Close"]
        /
        df["RollingMean_7"]
    )


    # =========================
    # Returns
    # =========================

    df["Return_1D"] = (
        df["Close"]
        .pct_change()
    )


    df["Return_5D"] = (
        df["Close"]
        .pct_change(5)
    )


    df["Return_20D"] = (
        df["Close"]
        .pct_change(20)
    )


    return df