import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import the data
    df = pd.read_csv("https://raw.githubusercontent.com/datasets/sea-level-rise/refs/heads/main/data/epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points', color='blue', alpha=0.6)

    # Line of best fit (1880 - 2050)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = intercept + slope * x_pred
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line (1880-2050)')

    # Line of best fit (2000 - 2050)
    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    x_recent_pred = pd.Series(range(2000, 2051))
    y_recent_pred = intercept_recent + slope_recent * x_recent_pred
    plt.plot(x_recent_pred, y_recent_pred, 'g', label='Best Fit Line (2000-2050)')

    # Customize the plot
    plt.title("Rise in Sea Level", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Sea Level (inches)", fontsize=12)
    plt.legend()
    plt.grid(True)

    # Save and show plot
    plt.savefig("sea_level_plot.png")
    plt.show()
    #call function
    draw_plot()
    