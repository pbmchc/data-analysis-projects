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


def draw_cat_plot():
    df = init_data()

    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat_grouped = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False)
    df_cat_grouped_with_total = df_cat_grouped.agg(total=pd.NamedAgg(column="value", aggfunc="count"))

    sns.set_theme()
    g = sns.catplot(x='variable', y='total', col='cardio', hue='value', data=df_cat_grouped_with_total, kind='bar')
    fig = g.fig

    fig.savefig('catplot.png', bbox_inches='tight', pad_inches=0.25)
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

