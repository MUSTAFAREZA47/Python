##def greet():
##    print("Hello")
##    print("Hello")
##    print("Hello")
##
##
##greet()
##
##def greet_with_name(name):
##    print(f"Hello {name}")
##    print(f"how do you do {name}")
##
##greet_with_name("ahmed")
##
##def greet_with(name, location):
##    print(f"Hello, My name is {name}")
##    print(f"I live at {location}")
##
##
##greet_with(location = "Sasaram", name = "Ahmed")

##AREA CALCULATOR
##
##test_h = int(input("Height fo the wall: "))
##test_w = int(input("Width fo the wall: "))
##
##coverage = 5
##
##def paint_cal(height=test_h, width=test_w, cover=coverage):
##    number_of_cans = round((height * width) / cover)
##    print(f"you will need {number_of_cans} cans"  )
##
##paint_cal()

##PRIME NUMBER CHECKER
##
##n = int(input('Check this number: '))
##
##def prime_checker(number=n):
##    is_prime = True
##    for i in range(2, number):
##        if number % i == 0:
##            is_prime = False
##    if is_prime:
##        print("It is a prime number.")
##    else:
##        print("It is not a prime number.")
##prime_checker()

##CIPHER CODE GENERATOR
##
##alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
##
##direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
##text = input("Type your message:\n").lower()
##shift = int(input("Type the shift number:\n"))
##
###TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
##def encrypt(plain_text, shift_amount):
##  cipher_text =""
##  for letter in plain_text:
##    position = alphabet.index(letter)
##    new_position = position + shift_amount
##    new_letter = alphabet[new_position]
##    cipher_text += new_letter
##  print(f"The encoded text is {cipher_text}")
##
##def decode(plain_text, shift_amount):
##  cipher_text =""
##  for letter in plain_text:
##    position = alphabet.index(letter)
##    new_position = position - shift_amount
##    new_letter = alphabet[new_position]
##    cipher_text += new_letter
##  print(f"The encoded text is {cipher_text}")
##
##
##    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
##    #e.g.
##    #plain_text = "hello"
##    #shift = 5
##    #cipher_text = "mjqqt"
##    #print output: "The encoded text is mjqqt"
##
##    ##HINT: How do you get the index of an item in a list:
##    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
##
##    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
##
###TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
##if direction == 'encode':
##  encrypt(text, shift)
##else:
##  decode(text, shift)


