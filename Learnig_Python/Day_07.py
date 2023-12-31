word_list = ['ardvark', 'baboon', 'camel']

import random

choose_word = random.choice(word_list)

word_length = len(choose_word)

display = []

for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = choose_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True