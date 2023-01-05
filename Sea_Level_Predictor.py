import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df)

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.plot(x, y, 'o', color='#4287f5', label="CSIRO Adjusted Sea Level Per Year")

    # plt.show()

    # Create first line of best fit
    result = linregress(x, y)
    slope, y_intercept = result.slope, result.intercept

    # extend line to 2050
    x_best_fit = np.linspace(1880, 2050)
    y_best_fit = slope * x_best_fit + y_intercept
    plt.plot(x_best_fit, y_best_fit, 'r', label="first line of best fit")

    plt.legend(loc="upper left")
    # plt.show()



    # Create second line of best fit
    df = df[df['Year'] >= 2000]
    # print(df)

    # plt.plot(df['Year'], y_intercept + slope * (df['Year']), 'black', label="second line of best fit")

    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope, y_intercept = result.slope, result.intercept

    # extend line to 2050
    updated_x_best_fit = np.linspace(1880, 2050)
    y_best_fit = slope * x_best_fit + y_intercept
    plt.plot(updated_x_best_fit, y_best_fit, 'black', label="second line of best fit")



    plt.legend(loc="upper left")
    # plt.show()

    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


if __name__ == "__main__":
    draw_plot()