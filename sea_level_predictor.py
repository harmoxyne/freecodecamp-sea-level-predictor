import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig, ax = plt.subplots()
    fig.set_figwidth(12)
    fig.set_figheight(7)

    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    x1 = np.arange(df['Year'].min(), 2050)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.plot(x1, intercept1 + slope1 * x1, 'r', label='linregress')
    # Create second line of best fit
    x2 = np.arange(2000, 2050)
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df[df['Year'] >= 2000]['Year'],
                                                                  df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    ax.plot(x2, intercept2 + slope2 * x2, 'g', label='linregress')
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
