import datetime

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

birthday = datetime.datetime(birth_year, birth_month, birth_day)
today = datetime.datetime.today()

age_days = (today - birthday).days
age_years = age_days // 365

print("You are approximately", age_years, "years old.")
print("That's "+ str(age_days) + " days!")