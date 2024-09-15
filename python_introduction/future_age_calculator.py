#future_age_calculator
#Prompt user to input their current age
current_age = int(input("how old are you? "))
#Calculate users age in 2050
current_year = 2023
future_year = 2050
years_to_future_year = future_year - current_year
age_in_future_year = current_age + years_to_future_year
#print future age
print(f"in {future_year} you will be {age_in_future_year} years old")
