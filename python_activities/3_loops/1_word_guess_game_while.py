"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""
# Word guessing game - While Loop

import mathstropy

random_word = mathstropy.randomword()  # random word generator function

print("Your job is to guess the secret word.")
print("Enter 'give up' to quit the game.")

hint = mathstropy.wordmask(random_word)
print(hint)  # this shows the masked word, some letters of the word are hidden

guess = input("Enter guess: ")  # initialize the cv

while guess.lower() != random_word.lower():  # while guess is not equal to the random word
    print("Sorry, guess incorrect.") # statement

    if guess == "give up":  # optional addition
        break
    
    guess = input("Enter guess: ")  # update the cv


# once while loop ends
print("The secret word was", random_word)
