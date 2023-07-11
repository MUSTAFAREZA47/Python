##fruits = ['Apple', 'Peach', 'Pear']
##for fruit in fruits:
##    print(fruit)
##    print(fruit + 'Pie')
##    print(fruits)

##Average Height

##student_height = input("Input a list of student heights").split()
##for n in range(0, len(student_height)):
##    student_height[n] = int(student_height[n])
##print(student_height)
##
##total_height = 0
##for height in students_height:
##    total_height += height
##print(total_height)

##Adding Even Number

##number_range = range(1, 101)
##
##total = 1
##for even in number_range:
##    if even % 2 == 0:
##        total += even
##print(total)
##
####another method
##
##number_range = range(2, 101, 2)
##
##total = 1
##for even in number_range:
##    total += even
##print(total)

##Fizz_Buzz Game

##for number in range(1, 101):
##    if number % 3 == 0:
##        print("Fizz")
##    if number % 5 == 0:
##        print("Buzz")
##    if number % 15 == 0:
##        print("Fizz_Buzz")
##    else:
##        print(number)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

####Lower_Level
##
##password = ""
##for char in range(1, nr_letters + 1):
##    random_char = random.choice(letters)
##    password += random_char
####    print(password)
##
##for char in range(1, nr_symbols + 1):
##    random_char = random.choice(symbols)
##    password += random_char
####    print(password)
##
##for char in range(1, nr_numbers + 1):
##    random_char = random.choice(numbers)
##    password += random_char
####    print(password)
##
####print(password)


##Higher_Level

password_list = []
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char
##    print(password)

for char in range(1, nr_symbols + 1):
    random_char = random.choice(symbols)
    password_list += random_char
##    print(password)

for char in range(1, nr_numbers + 1):
    random_char = random.choice(numbers)
    password_list += random_char
##    print(password)

print(password_list)

random.shuffle(password_list)

print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is {password}")





