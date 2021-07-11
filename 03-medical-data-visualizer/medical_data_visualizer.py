import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

FILE_PATH = 'medical_examination.csv'


def init_data():
    df = pd.read_csv(FILE_PATH)

    df['overweight'] = _get_df_overweight(df)
    df['cholesterol'] = _map_series_to_binary(df['cholesterol'])
    df['gluc'] = _map_series_to_binary(df['gluc'])

    return df


# Draw Categorical Plot
def draw_cat_plot():
    df = init_data()

    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None

    # Set up the matplotlib figure
    fig, ax = None

    # Draw the catplot with 'sns.catplot()'

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    df = init_data()

    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None

    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


def _get_df_overweight(df):
    return (_get_df_bmi(df) > 25).astype(int)


def _get_df_bmi(df):
    return df['weight'] / ((df['height'] / 100) ** 2)


def _map_series_to_binary(series, threshold=1):
    return (series > threshold).astype(int)

