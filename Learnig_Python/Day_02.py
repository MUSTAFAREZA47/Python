##Your Life in Weeks Calculator

name = input('what is your name?')
age = input('what is your current age?')

remaining_age = 90 - int(age)

days = int(remaining_age * 365)
weeks = int(remaining_age * 52)
months = int(remaining_age * 12)

print(f'{name},You have {days} days, {weeks} weeks, and {months} months left.')


##Day_02 Tip Calculator

print('Welocme to the tip calculator')
total_bill = float(input('what was the total bill? $\n'))
tip = int(input('what percentage tip would you like to give? 10, 12, or 15?\n'))
percentage_tip = (total_bill * tip) / 100
total = float(total_bill + percentage_tip)
spliting_bill = int(input('How many people to split the bill?'))
print(f"Each person should pay: {total / spliting_bill}")

