import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', sep=',')
    #print(df.head())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # "Select race column from df, count the number of occurrences for each unique value in race column"
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # "Select sex column from df, calculates the average of the values in the selected column"
    #average_age_men = round(df.loc[df['sex'] == 'Male', ['age']].mean(), 1)
    # Select all men
    men = df[df['sex'] == 'Male']
    # Count average
    average_age_men = round(men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    # "Select from education only Bachelors and count them. Divide them by education count, multiply by 100 and round by 1 decimal"
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].shape[0] / df['education'].shape[0] * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # Select from education column Bachelors, Masters and Doctorate
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    # Select from education column NOT Bachelors, Masters and Doctorate
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    # "Filter by education and high salary and round by 1 decimal"
    higher_education_rich = round(higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0] * 100, 1)
    lower_education_rich = round(lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0] * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    # "Calculate minimum value from hours-per-week column"
    min_work_hours = df['hours-per-week'].min()
    #print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]

    # "Select hours-per-week rows", for simpler formula 
    min_hours = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(min_hours[min_hours['salary'] == ">50K"].shape[0] / num_min_workers * 100, 1) 

    # What country has the highest percentage of people that earn >50K?
    # "Select unique native country and selects the rows form salary that are greater than 50K"
    high_salary_by_country_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    #print(high_salary_by_country_count)
    # "Count native-country column occurrence for all rows"
    count_country_occurrence = df['native-country'].value_counts()
    #print(count_country_occurrence)
    salary_percentage_by_country = high_salary_by_country_count / count_country_occurrence * 100
    #print(salary_percentage_by_country)

    highest_earning_country = salary_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(salary_percentage_by_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == ">50K") & (df['native-country'] == 'India')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
