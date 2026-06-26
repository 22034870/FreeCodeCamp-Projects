import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data
df = pd.read_csv('medical_examination.csv')

# 2. Add an 'overweight' column
# BMI is weight in kg divided by the square of height in meters.
# Height is given in cm, so we divide by 100 to get meters.
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize data by making 0 always good and 1 always bad. 
# If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    # 4. Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 5. Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # We group by the essential columns, calculate the size, and reset the index while naming the new count column 'total'.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 6. Draw the catplot with sns.catplot()
    catplot = sns.catplot(
        x="variable", 
        y="total", 
        hue="value", 
        col="cardio",
        data=df_cat, 
        kind="bar"
    )

    # 7. Get the figure for the output
    fig = catplot.fig

    # 8. Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 9. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 10. Calculate the correlation matrix
    corr = df_heat.corr()

    # 11. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 12. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 9))

    # 13. Plot the correlation matrix using sns.heatmap()
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt='.1f', 
        center=0,
        vmin=-0.1, 
        vmax=0.3, # Adjust to match the FCC example image scaling
        cbar_kws={'shrink': .5}, 
        square=True
    )

    # 14. Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig