#Finance calculator
#Prompt the user to input their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
#Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
#Calculate annual savings
annual_savings = monthly_savings * 12
#Calculate annual savings with interest
interest_rate = 0.05
projected_savings = annual_savings + (annual_savings * interest_rate)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
