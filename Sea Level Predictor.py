import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5, label='Original Data')

    # 3. Create first line of best fit (1880 - 2050)
    # Calculate regression for the entire dataset
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create an array of years from 1880 to 2050 for the x-axis
    x_all = pd.Series([i for i in range(1880, 2051)])
    # Calculate the corresponding y values using the slope and intercept
    y_all = res_all.intercept + res_all.slope * x_all
    
    plt.plot(x_all, y_all, 'r', label='Best Fit Line (1880-2050)')

    # 4. Create second line of best fit (2000 - 2050)
    # Filter the dataframe for years 2000 and onwards
    df_recent = df[df['Year'] >= 2000]
    
    # Calculate regression for the recent dataset
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create an array of years from 2000 to 2050 for the x-axis
    x_recent = pd.Series([i for i in range(2000, 2051)])
    # Calculate the corresponding y values
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    
    plt.plot(x_recent, y_recent, 'green', label='Best Fit Line (2000-2050)')

    # 5. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()