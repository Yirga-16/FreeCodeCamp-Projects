import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # print(df, '\n\n')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index
    # labels.
    total_count = 0
    race_list = []
    race_dict = dict()

    for race in df['race']:
        if race not in race_list:
            race_list.append(race)
        total_count += 1

    for i in range(0, len(race_list)):
        count = 0

        for race in df['race']:
            if race == race_list[i]:
                count += 1
        race_dict[race_list[i]] = count

    race_count = pd.Series(data=race_dict)

    # What is the average age of men?
    total_age = 0
    total_men = 0
    for i in range(0, total_count):
        if df['sex'][i] == "Male":
            total_men += 1
            total_age += df['age'][i]

    average_age_men = total_age / total_men
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = 0
    for education in df['education']:
        if education == 'Bachelors':
            bachelors_count += 1
    percentage_bachelors = round((bachelors_count / total_count) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = 0
    higher_education_more_than_50K = 0
    lower_education = 0
    lower_education_more_than_50K = 0

    for i in range(0, len(df['salary'])):
        if df['education'][i] == "Bachelors" or df['education'][i] == "Masters" or df['education'][i] == "Doctorate":
            if df['salary'][i] == ">50K":
                higher_education_more_than_50K += 1
            higher_education += 1
        else:
            if df['salary'][i] == ">50K":
                lower_education_more_than_50K += 1
            lower_education += 1

    # percentage with salary >50K
    higher_education_rich = round((higher_education_more_than_50K / higher_education) * 100, 1)
    lower_education_rich = round((lower_education_more_than_50K / lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = 0
    num_min_workers_make_50K = 0

    for i in range(0, df['salary'].count()):
        if df['hours-per-week'][i] == min_work_hours:
            if df['salary'][i] == ">50K":
                num_min_workers_make_50K += 1
            num_min_workers += 1

    rich_percentage = round((num_min_workers_make_50K / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_list = []
    highest_earning_country = dict()

    for country in df['native-country']:
        if country not in highest_earning_country_list:
            highest_earning_country_list.append(country)

    for i in range(0, len(highest_earning_country_list)):
        count = 0
        rich_count = 0

        for j in range(0, df['native-country'].count()):
            if df['native-country'][j] == highest_earning_country_list[i]:
                count += 1
                if df['salary'][j] == ">50K":
                    rich_count += 1

        highest_earning_country[highest_earning_country_list[i]] = (rich_count / count) * 100

    highest_earning_country_percentage = round(max(highest_earning_country.values()), 1)
    highest_earning_country = max(highest_earning_country, key=highest_earning_country.get)

    # Identify the most popular occupation for those who earn >50K in India.
    IN_occupation_list = []
    IN_occupation_dict = dict()

    for occupation in df['occupation']:
        if occupation not in IN_occupation_list:
            IN_occupation_list.append(occupation)

    for i in range(0, len(IN_occupation_list)):
        count = 0

        for occupation in df['occupation']:
            if occupation == IN_occupation_list[i]:
                count += 1
        IN_occupation_dict[IN_occupation_list[i]] = count

    top_IN_occupation = max(IN_occupation_dict, key=IN_occupation_dict.get)

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


if __name__ == "__main__":
    calculate_demographic_data()
