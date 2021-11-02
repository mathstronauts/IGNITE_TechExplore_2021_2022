"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""
# Word guessing game - For Loop

import mathstropy

random_word = mathstropy.randomword()  # random word generator function
chances = 3  # number of trys to guess the number
hint = mathstropy.wordmask(random_word)

print("Your job is to guess the secret word.")
print("You will have", str(chances), "chances to guess.")

print(hint)

for i in range(chances):  # the for loop will run 3 times, the upper limit is one above the highest number we want to count to
    guess = input("Enter guess: ")  # 
    
    if guess.lower() != random_word:  # add this after, simple for loop just asking for guess
        print("Sorry, guess incorrect.")
    else:
        print("You won!")
        break

# once for loop is completed
print("The secret word was", random_word)
