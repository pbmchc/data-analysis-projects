import platform
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

from date_utils import get_months_categorical_order, format_date_boundaries

register_matplotlib_converters()

FILE_PATH = 'fcc-forum-pageviews.csv'


def init_data():
    df = pd.read_csv(FILE_PATH, index_col='date', parse_dates=True)
    page_views_lower_limit, page_views_upper_limit = _get_df_value_limits(df, 'value')

    return df[page_views_lower_limit & page_views_upper_limit]


def draw_line_plot():
    df = init_data()

    df.index.names = ['Date']
    df_line = df.rename(columns={'value': 'Page Views'})

    date_format = '%#m/%Y' if platform.system() == 'Windows' else '%-m/%Y'
    from_boundary, to_boundary = format_date_boundaries(df_line.index, date_format)

    sns.set_theme()
    fig, ax = plt.subplots(figsize=(12, 8))
    plot_title = f'Daily freeCodeCamp Forum Page Views {from_boundary}-{to_boundary}'
    sns.lineplot(data=df_line, x='Date', y='Page Views', ax=ax).set_title(plot_title)

    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    df = init_data()

    df_grouped_by_date = df.groupby([df.index.year, df.index.month_name()])
    df_grouped_by_date_mean = df_grouped_by_date.mean()
    df_grouped_by_date_mean.index.names = ['Years', 'Months']
    df_grouped_by_date_mean.columns = ['Average Page Views']
    df_bar = df_grouped_by_date_mean.reset_index()

    sns.set_theme()
    fig, ax = plt.subplots(figsize=(12, 8))
    months_order = get_months_categorical_order('%B')
    sns.barplot(data=df_bar, x='Years', y='Average Page Views', hue='Months', hue_order=months_order, ax=ax, palette='deep')
    plt.legend(loc='upper left')

    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    df = init_data()

    df_box = df.reset_index()
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    df_box = df_box.rename(columns={'value': 'Page Views'})

    sns.set_theme()
    fig, axes = plt.subplots(figsize=(24, 8), ncols=2)

    year_plot_title = 'Year-wise Box Plot (Trend)'
    sns.boxplot(data=df_box, x='Year', y='Page Views', ax=axes[0]).set_title(year_plot_title)

    months_order = get_months_categorical_order('%b')
    month_plot_title = 'Month-wise Box Plot (Seasonality)'
    sns.boxplot(data=df_box, x='Month', y='Page Views', order=months_order, ax=axes[1]).set_title(month_plot_title)

    fig.savefig('box_plot.png')
    return fig


def _get_df_value_limits(df, column):
    return df[column] >= df[column].quantile(0.025), df[column] <= df[column].quantile(0.975)

