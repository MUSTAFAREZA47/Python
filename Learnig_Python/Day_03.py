##_if_esle Conditionals

##
##print('Welcome to the rolllercoaster!')
##height = int(input('what is your height in cm?'))
##
##if height > 120:
##    print('You can ride the rollercoaster!')
##else:
##    print('Sorry, you have to grow taller before you can ride.')


##Recognise Even _and odd number

##number = int(input('which number do you want to choose?'))
##
##if number % 2 == 0:
##    print(f'Woow, You choose a even number {number}')
##else:
##    print(f'Cool, you choose a odd number {number}')


##BMI calculator 2.0
##
##height = float(input('enter your height in m: '))
##wight = float(input('enter your weight in kg: '))
##
##BMI = round(wight / height ** 2)
##
##if BMI < 18.5:
##    print(f'Your BMI is {BMI}, and You are Underweight.')
##elif 18.5 < BMI < 25:
##    print(f'Your BMI is {BMI}, and You are Normal wight.')
##elif 25 < BMI < 30:
##    print(f'Your BMI is {BMI}, and You are Overweight.')
##elif 35 < BMI < 35:
##    print(f'Your BMI is {BMI}, and You are Obese.')
##else:
##    print(f'Your BMI is {BMI}, and You are clinically obese.')


##Leap Year Calculator
##
##year = int(input('which year do you want to check?\n'))
##
##if year % 4 ==0:
##    if year % 400 == 0:
##        if year % 100 != 0:
##            print(f'{year} is a leap year!')
##        else:
##            print(f'{year} is a leap year!')
##    else:
##        print('it is not leap year.')
##else:
##    print('it is not leap year.')


##_if_esle Conditionals
##
##print('Welcome to the rolllercoaster!')
##height = int(input('what is your height in cm?'))
##bill = 0
##
##if height > 120:
##    print('You can ride the rollercoaster!')
##    age = int(input('what is your age? '))
##    if age < 12:
##        bill = 5
##        print('Child tickets are $5')
##    elif age <= 18:
##        bill = 7
##        print('Youth tickets are $7')
##    else:
##        bill = 12
##        print('Adult tickets are $12')
##
##    wants_bill = input('Do you want to take photo? Y or N.')
##    if wants_bill == "Y" :
##        print(f'Your total bill is ${bill + 3}')
##    else:
##        print(f'Your total bill is ${bill}.')
##else:
##    print('Sorry, you have to grow taller before you can ride.')


##print('Welcome to Python Pizza Deliveries!')
##
##size = input('what size pizza do you want? S, M, or L?')
##add_pepperoni = input('Do you want pepperoni? Y or N?')
##extra_cheese = input('Do you want extra cheese? Y or N?')
##
##bill = 0
##
##if size == "S":
##    bill += 15
##elif size == "M":
##    bill += 20
##else:
##    bill += 25
##
##if add_pepperoni == "Y":
##    if size == "S":
##        bill += 2
##    else:
##        bill += 3
##
##if extra_cheese == "Y":
##    bill += 1
##
##print(f'Your final bill is ${bill}!')

##Love Calculator
##
##print("Welcome to the love calculator!")
##
##name1 = input('What is your name? \n')
##name2 = input('What is their name? \n')
##
##lower_case_name1 = name1.lower()
##lower_case_name2 = name2.lower()
##
##t_occur = lower_case_name1.count('t') + lower_case_name2.count('t')
##r_occur = lower_case_name1.count('r') + lower_case_name2.count('r')
##u_occur = lower_case_name1.count('u') + lower_case_name2.count('u')
##e_occur = lower_case_name1.count('e') + lower_case_name2.count('e')
##
##true = t_occur + r_occur + u_occur + e_occur
##
##l_occur = lower_case_name1.count('l') + lower_case_name2.count('l')
##o_occur = lower_case_name1.count('o') + lower_case_name2.count('o')
##v_occur = lower_case_name1.count('v') + lower_case_name2.count('v')
##e_occur = lower_case_name1.count('e') + lower_case_name2.count('e')
##
##love = l_occur + o_occur + v_occur + e_occur
##
##percentage_love_score = str(true) + str(love)
##percentage_love_score1 = int(percentage_love_score)
##
##if percentage_love_score1 < 10 or percentage_love_score1 > 90:
##    print(f'Your Score is {percentage_love_score1}, you go together like coke and mentos.')
##else:
##    print(f'Your Score is {percentage_love_score1}, you are alright together.')


