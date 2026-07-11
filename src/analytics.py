import pandas as pd
import numpy as np


def commodity_profile(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate summary statistics for each commodity.

    Parameters
    ----------
    merged_df : pd.DataFrame
        Merged commodity dataset.

    Returns
    -------
    pd.DataFrame
    """

    profiles = []

    for commodity in merged_df.columns[1:]:

        prices = merged_df[commodity].dropna()

        total_return = (
            (prices.iloc[-1] - prices.iloc[0]) / prices.iloc[0]
        ) * 100

        daily_returns = prices.pct_change().dropna()

        annualized_volatility = daily_returns.std() * np.sqrt(252) * 100

        profile = {
            "Commodity": commodity.replace("_", " ").title(),
            "Start Price": round(prices.iloc[0], 2),
            "Latest Price": round(prices.iloc[-1], 2),
            "Minimum": round(prices.min(), 2),
            "Maximum": round(prices.max(), 2),
            "Mean": round(prices.mean(), 2),
            "Median": round(prices.median(), 2),
            "Std Dev": round(prices.std(), 2),
            "Total Return (%)": round(total_return, 2),
            "Annualized Volatility (%)": round(annualized_volatility, 2)
        }

        profiles.append(profile)

    return pd.DataFrame(profiles)



def add_moving_averages(
    df,
    windows=[30,90],
    price_column="Close"
):
    """
    Add rolling moving averages.

    Parameters
    ----------
    df : pd.DataFrame

    windows : list
        Rolling window sizes.

    price_column : str

    Returns
    -------
    pd.DataFrame
    """

    df = df.copy()

    for window in windows:
        df[f"MA_{window}"] = (
            df[price_column]
            .rolling(window=window)
            .mean()
        )

    return df


def add_returns(
    df,
    price_column="Close"
):
    """
    Add daily return calculations.

    Parameters
    ----------
    df : pd.DataFrame
        Commodity price dataframe

    price_column : str
        Price column

    Returns
    -------
    pd.DataFrame
    """

    df = df.copy()

    df["Daily_Return"] = (
        df[price_column]
        .pct_change()
    )

    return df


def calculate_monthly_returns(
    df,
    price_column="Close"
):

    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError(
            "DataFrame must have DatetimeIndex"
        )

    monthly = (
        df[price_column]
        .resample("ME")
        .last()
        .pct_change()
    )

    return monthly


def cumulative_return(
    returns
):
    """
    Calculate cumulative return from periodic returns.

    Parameters
    ----------
    returns : pd.Series
        Daily or monthly returns.

    Returns
    -------
    pd.Series
        Cumulative growth of investment.
    """

    return (
        (1 + returns)
        .cumprod()
        - 1
    )


def calculate_cagr(
    df,
    price_column="Close"
):

    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError(
            "DataFrame must have DatetimeIndex"
        )


    start_price = df[price_column].iloc[0]

    end_price = df[price_column].iloc[-1]


    years = (
        df.index[-1] -
        df.index[0]
    ).days / 365.25


    cagr = (
        (end_price / start_price)
        **
        (1 / years)
    ) - 1


    return cagr * 100





def return_summary(
    df,
    price_column="Close"
):
    """
    Generate return based performance metrics.
    """

    df = df.copy()

    daily_returns = (
        df[price_column]
        .pct_change()
        .dropna()
    )


    total_return = (
        (df[price_column].iloc[-1] /
         df[price_column].iloc[0])
        - 1
    ) * 100


    annualized_return = (
        ((df[price_column].iloc[-1] /
          df[price_column].iloc[0])
          **
          (252 / len(df)))
        - 1
    ) * 100


    volatility = (
        daily_returns.std()
        *
        np.sqrt(252)
    ) * 100


    sharpe_ratio = (
        daily_returns.mean()
        /
        daily_returns.std()
    ) * np.sqrt(252)


    return pd.DataFrame({
        "Total Return (%)":[round(total_return,2)],
        "Annualized Return (%)":[round(annualized_return,2)],
        "Annualized Volatility (%)":[round(volatility,2)],
        "Sharpe Ratio":[round(sharpe_ratio,2)]
    })



def return_distribution_stats(
    df,
    price_column="Close"
):
    """
    Calculate statistical properties of daily returns.
    """

    returns = (
        df[price_column]
        .pct_change()
        .dropna()
    )

    stats = {

        "Mean Daily Return (%)":
            returns.mean() * 100,

        "Daily Volatility (%)":
            returns.std() * 100,

        "Skewness":
            returns.skew(),

        "Kurtosis":
            returns.kurtosis(),

        "Best Day (%)":
            returns.max() * 100,

        "Worst Day (%)":
            returns.min() * 100
    }


    return pd.DataFrame([stats])



def calculate_var(
    df,
    confidence=0.95,
    price_column="Close"
):
    """
    Historical Value at Risk.

    Returns worst expected daily loss.
    """

    returns = (
        df[price_column]
        .pct_change()
        .dropna()
    )


    var = np.percentile(
        returns,
        (1-confidence)*100
    )


    return var * 100


def calculate_rolling_volatility(
    df,
    window=30,
    price_column="Close"
):
    """
    Calculate rolling annualized volatility.

    Parameters
    ----------
    df : DataFrame

    window : int
        Rolling period.

    price_column : str

    Returns
    -------
    DataFrame
    """

    df = df.copy()

    returns = (
        df[price_column]
        .pct_change()
    )


    df["Daily_Return"] = returns


    df[f"Rolling_{window}_Volatility"] = (
        returns
        .rolling(window)
        .std()
        *
        np.sqrt(252)
        *
        100
    )


    return df


def volatility_summary(
    df,
    column="Rolling_30_Volatility"
):

    volatility = (
        df[column]
        .dropna()
    )


    return pd.DataFrame({

        "Average Volatility (%)":
        [round(volatility.mean(),2)],

        "Maximum Volatility (%)":
        [round(volatility.max(),2)],

        "Minimum Volatility (%)":
        [round(volatility.min(),2)]

    })

def correlation_matrix(
    merged_df
):
    """
    Correlation matrix of daily returns.
    """

    returns = (
        merged_df
        .pct_change()
        .dropna()
    )

    return returns.corr()

def rolling_correlation(
    df1,
    df2,
    window=30,
    price_column="Close"
):
    """
    Rolling correlation between two commodities.
    """

    returns1 = df1[price_column].pct_change()
    returns2 = df2[price_column].pct_change()

    corr = (
        returns1
        .rolling(window)
        .corr(returns2)
    )

    return corr



def calculate_drawdown(
    df,
    price_column="Close"
):
    """
    Calculate drawdown series.

    Returns
    -------
    pd.DataFrame
    """

    df = df.copy()

    running_max = (
        df[price_column]
        .cummax()
    )

    df["Drawdown"] = (
        df[price_column]
        -
        running_max
    ) / running_max * 100

    return df


def maximum_drawdown(
    df
):
    """
    Calculate maximum drawdown.
    """

    return df["Drawdown"].min()



def calculate_drawdowno(
    df,
    price_column="Close"
):
    """
    Calculate drawdown series.

    Returns
    -------
    DataFrame
    """

    df = df.copy()

    rolling_peak = df[price_column].cummax()

    df["Drawdown"] = (
        df[price_column] - rolling_peak
    ) / rolling_peak * 100

    return df


def rolling_sharpe_ratio(
    df,
    price_column="Close",
    window=252,
    risk_free_rate=0.02
):
    """
    Calculate rolling annualized Sharpe Ratio.

    Parameters
    ----------
    window : int
        Rolling window in trading days.
    """

    df = df.copy()

    daily_returns = df[price_column].pct_change()

    daily_rf = risk_free_rate / 252

    rolling_return = (
        daily_returns
        .rolling(window)
        .mean()
        * 252
    )

    rolling_volatility = (
        daily_returns
        .rolling(window)
        .std()
        * np.sqrt(252)
    )

    df[f"Rolling_{window}_Sharpe"] = (
        rolling_return - risk_free_rate
    ) / rolling_volatility

    return df


def rolling_sharpe_summary(
    df,
    window=252
):

    column = f"Rolling_{window}_Sharpe"

    return pd.Series({
        "Average Rolling Sharpe": round(df[column].mean(), 2),
        "Maximum Rolling Sharpe": round(df[column].max(), 2),
        "Minimum Rolling Sharpe": round(df[column].min(), 2)
    })

def calculate_sortino_ratio(
    df,
    price_column="Close",
    risk_free_rate=0.02
):
    """
    Calculate annualized Sortino Ratio.
    """

    returns = df[price_column].pct_change().dropna()

    downside_returns = returns[returns < 0]

    downside_deviation = (
        downside_returns.std()
        * np.sqrt(252)
    )

    annual_return = returns.mean() * 252

    sortino = (
        annual_return - risk_free_rate
    ) / downside_deviation

    return sortino


