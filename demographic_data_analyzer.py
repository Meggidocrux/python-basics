import pandas as pd

df=pd.read_csv(r"C:/Users/FEYISARA\Downloads/adult.data.csv")

print(df)
print(df.columns)

race_counts=df['Race'].value_counts()
print('race_counts:',race_counts)

average_age_men = df[df['Gender'] == 'Male']['Age'].mean()
print(round(average_age_men, 1))

percentage_bachelors = round( df['Education'].value_counts(normalize=True)['Bachelors'] * 100.0, 1 )
print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")

advanced_edu = df['Education'].isin(['Bachelors', 'Masters', 'Doctorate'])
high_income = df['Salary'] == '>50,000'
percentage_adv_high_income = (advanced_edu & high_income).mean() *100
print(f"percentage of people with advanced education making more than 50k:{percentage_adv_high_income:.2f}%")

percentage_non_adv_high_income = ((~advanced_edu) & high_income).mean() * 100
print(f"percentage of people without adavanced education making more than 50k:{percentage_non_adv_high_income:.2f}%")

min_hours_per_week = df['Hours-per-week'].min()
print(f"minimum hours a person works per week:{min_hours_per_week}")

num_min_workers = df['Hours-per-week'].shape[0]
num_min_rich=df[(df['Hours-per-week'] == 'min_hours_per_week') &(df['Salary'] == '>50,000')].shape[0]
rich_percentage = (num_min_rich/num_min_workers)*100
print("percentage of people who work the minimum hours and earn more than 50k:",round(rich_percentage, 1))

country_highest_percentage = df['Native-Country'].isin(['Race','Gender', 'Occupation'])
high_income = df['Salary'] == '>50,000'
percentage_of_people = (country_highest_percentage & high_income).mean() * 100
print(f"percentage of country that has the highest percentage of people that earn >50K:{percentage_of_people:.2f}%")

percentage_of_people = df['Salary'] == '>50K' & (df['Native-Country'] == 'India').isin['Occupation'].value_counts().keys[0]
