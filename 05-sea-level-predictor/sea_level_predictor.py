import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

FILE_PATH = 'epa-sea-level.csv'
YEAR_COLUMN = 'Year'
SEA_LEVEL_COLUMN = 'CSIRO Adjusted Sea Level'


def init_data():
    return pd.read_csv(FILE_PATH)


def draw_plot():
    df = init_data()

    df_scatter = df[[YEAR_COLUMN, SEA_LEVEL_COLUMN]]
    years = df_scatter[YEAR_COLUMN]
    sea_level = df_scatter[SEA_LEVEL_COLUMN]

    plt.scatter(x=years, y=sea_level)

    predictions_range = _get_predictions_range(years.max() + 1)

    years_with_predictions, sea_level_values = _get_line_of_best_fit(df, predictions_range)
    plt.plot(years_with_predictions, sea_level_values, color='black')

    df_current_mill = df_scatter[df_scatter[YEAR_COLUMN] >= 2000]

    years_with_predictions_current_mill, sea_level_values_current_mill = _get_line_of_best_fit(df_current_mill, predictions_range)
    plt.plot(years_with_predictions_current_mill, sea_level_values_current_mill, color='red')

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    plt.savefig('sea_level_plot.png')
    return plt.gca()


def _get_predictions_range(predictions_range_start, predictions_range_end=2050):
    return pd.Series([year for year in range(predictions_range_start, predictions_range_end + 1)])


def _get_line_of_best_fit(df, predictions_range):
    years = df[YEAR_COLUMN]
    sea_level = df[SEA_LEVEL_COLUMN]
    result = linregress(years, sea_level)
    years_with_predictions = pd.concat([years, predictions_range])
    sea_level_values = result.slope * years_with_predictions + result.intercept

    return years_with_predictions, sea_level_values
