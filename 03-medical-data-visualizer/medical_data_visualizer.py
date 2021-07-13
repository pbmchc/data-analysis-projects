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

    height_lower_limit, health_upper_limit = _get_df_reference_limits(df, 'height')
    weight_lower_limit, weight_upper_limit = _get_df_reference_limits(df, 'weight')
    height_reference_limits = height_lower_limit & health_upper_limit
    weight_reference_limits = weight_lower_limit & weight_upper_limit
    arterial_pressure_errors = df['ap_lo'] <= df['ap_hi']

    df_heat = df[height_reference_limits & weight_reference_limits & arterial_pressure_errors]
    df_corr = df_heat.corr()

    mask = np.zeros_like(df_corr)
    mask[np.triu_indices_from(mask)] = True

    sns.set_theme()
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(df_corr, ax=ax, mask=mask, annot=True, fmt='.1f', center=0, square=True)

    fig.savefig('heatmap.png', bbox_inches='tight', pad_inches=0.25)
    return fig


def _get_df_overweight(df):
    return (_get_df_bmi(df) > 25).astype(int)


def _get_df_bmi(df):
    return df['weight'] / ((df['height'] / 100) ** 2)


def _get_df_reference_limits(df, column):
    return df[column] >= df[column].quantile(0.025), df[column] <= df[column].quantile(0.975)


def _map_series_to_binary(series, threshold=1):
    return (series > threshold).astype(int)
