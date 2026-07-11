import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

import seaborn as sns

def plot_price_history(
    df,
    commodity_name,
    price_column="Close",
    figsize=(14, 6)
):
    """
    Plot historical commodity prices.
    """

    plt.figure(figsize=figsize)

    plt.plot(
        df.index,
        df[price_column],
        linewidth=2
    )

    plt.title(
        f"{commodity_name} Price History (2015-2026)",
        fontsize=16
    )

    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.show()



def plot_moving_average(
    df,
    commodity_name,
    price_column="Close"
):

    plt.figure(figsize=(14,6))

    plt.plot(
        df.index,
        df[price_column],
        label="Price"
    )

    plt.plot(
        df.index,
        df["MA_30"],
        label="30 Day MA"
    )

    plt.plot(
        df.index,
        df["MA_90"],
        label="90 Day MA"
    )

    plt.title(
        f"{commodity_name} Price Trend with Moving Averages"
    )

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.legend()

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.show()



def plot_return_distribution(
    df,
    commodity_name
):

    fig = px.histogram(
        df,
        x="Daily_Return",
        nbins=100,
        title=f"{commodity_name} Daily Return Distribution"
    )

    fig.show()


def plot_return_distribution(
    df,
    commodity_name,
    price_column="Close"
):

    returns = (
        df[price_column]
        .pct_change()
        .dropna()
    )


    plt.figure(figsize=(12,5))


    plt.hist(
        returns,
        bins=100
    )


    plt.title(
        f"{commodity_name} Daily Return Distribution"
    )


    plt.xlabel(
        "Daily Return"
    )

    plt.ylabel(
        "Frequency"
    )


    plt.grid(alpha=0.3)

    plt.show()


def plot_rolling_volatility(
    df,
    commodity_name,
    window=30
):

    column = f"Rolling_{window}_Volatility"

    plt.figure(figsize=(14,6))

    plt.plot(
        df.index,
        df[column],
        linewidth=2
    )

    plt.title(
        f"{commodity_name} {window}-Day Rolling Volatility"
    )

    plt.xlabel("Date")
    plt.ylabel("Annualized Volatility (%)")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.show()


def plot_correlation_heatmap(
    corr_matrix
):

    plt.figure(figsize=(8,6))

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="RdYlBu_r",
        center=0,
        linewidths=0.5
    )

    plt.title("Commodity Return Correlation")

    plt.tight_layout()

    plt.show()


def plot_rolling_correlation(
    rolling_corr,
    commodity1,
    commodity2
):

    plt.figure(figsize=(14,6))

    plt.plot(
        rolling_corr.index,
        rolling_corr,
        linewidth=2
    )

    plt.axhline(
        0,
        linestyle="--",
        alpha=0.5
    )

    plt.title(
        f"30-Day Rolling Correlation\n{commodity1} vs {commodity2}"
    )

    plt.xlabel("Date")

    plt.ylabel("Correlation")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.show()


def plot_drawdown(
    df,
    commodity_name
):

    plt.figure(figsize=(14,6))

    plt.fill_between(
        df.index,
        df["Drawdown"],
        0,
        alpha=0.5
    )

    plt.plot(
        df.index,
        df["Drawdown"],
        linewidth=1.5
    )

    plt.title(
        f"{commodity_name} Drawdown"
    )

    plt.xlabel("Date")
    plt.ylabel("Drawdown (%)")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.show()

def plot_drawdown0(
    df,
    commodity_name
):

    plt.figure(figsize=(14,6))

    plt.plot(
        df.index,
        df["Drawdown"],
        color="red",
        linewidth=1.5
    )

    plt.fill_between(
        df.index,
        df["Drawdown"],
        0,
        color="red",
        alpha=0.25
    )

    plt.title(
        f"{commodity_name} Drawdown Curve"
    )

    plt.xlabel("Date")
    plt.ylabel("Drawdown (%)")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.show()







def plot_rolling_sharpe(
    df,
    commodity_name,
    window=252
):

    column = f"Rolling_{window}_Sharpe"

    plt.figure(figsize=(14,6))

    plt.plot(
        df.index,
        df[column],
        linewidth=2
    )

    plt.axhline(
        0,
        linestyle="--",
        color="black"
    )

    plt.title(
        f"{commodity_name} Rolling {window}-Day Sharpe Ratio"
    )

    plt.xlabel("Date")
    plt.ylabel("Sharpe Ratio")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.show()



def plot_feature_correlation(df):

    plt.figure(figsize=(12,8))

    sns.heatmap(
        df.corr(),
        cmap="coolwarm",
        center=0
    )

    plt.title("Feature Correlation Matrix")

    plt.show()