import pandas as pd

from number_utils import round_decimal

FILE_PATH = 'adult.data.csv'


def calculate_demographic_data(print_data=True):
    df = pd.read_csv(FILE_PATH)

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    df_men = df[df['sex'] == 'Male']
    average_age_men = round_decimal(df_men['age'].mean())

    # What is the percentage of people who have a Bachelor's degree?
    df_bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = _get_df_percentage(df_bachelors, df)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_selector = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    df_higher_education = df[higher_education_selector]
    df_lower_education = df[~higher_education_selector]
    df_higher_education_high_salary = _get_df_high_salary(df_higher_education)
    df_lower_education_high_salary = _get_df_high_salary(df_lower_education)
    percentage_higher_education_high_salary = _get_df_percentage(df_higher_education_high_salary, df_higher_education)
    percentage_lower_education_high_salary = _get_df_percentage(df_lower_education_high_salary, df_lower_education)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_hour_workers = df[df['hours-per-week'] == min_work_hours]
    df_min_hour_workers_high_salary = _get_df_high_salary(df_min_hour_workers)
    percentage_min_hour_workers_high_salary = _get_df_percentage(df_min_hour_workers_high_salary, df_min_hour_workers)

    df_high_salary = _get_df_high_salary(df)

    # What country has the highest percentage of people that earn >50K?
    countries_counts = df['native-country'].value_counts()
    countries_high_salary_counts = df_high_salary['native-country'].value_counts()
    countries_high_salary_percentages = round_decimal(countries_high_salary_counts / countries_counts * 100)

    highest_earning_country = countries_high_salary_percentages.idxmax()
    highest_earning_country_percentage = countries_high_salary_percentages.max()

    # Identify the most popular occupation for those who earn >50K in India.
    df_high_salary_india = df_high_salary[df_high_salary['native-country'] == 'India']
    top_india_high_salary_occupation = df_high_salary_india['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {percentage_higher_education_high_salary}%")
        print(f"Percentage without higher education that earn >50K: {percentage_lower_education_high_salary}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {percentage_min_hour_workers_high_salary}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top high salary occupation in India:", top_india_high_salary_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': percentage_higher_education_high_salary,
        'lower_education_rich': percentage_lower_education_high_salary,
        'min_work_hours': min_work_hours,
        'rich_percentage': percentage_min_hour_workers_high_salary,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_india_occupation': top_india_high_salary_occupation
    }


def _get_df_high_salary(df):
    return df[df['salary'] == '>50K']


def _get_df_percentage(df_part, df):
    return round_decimal(len(df_part.index) / len(df.index) * 100)

