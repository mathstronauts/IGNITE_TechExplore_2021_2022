"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""
# Joke Bot If/Else Statement

score = 0  # keep score of correct responses

name = input("Please enter your name: ")

print("Hello", name, ". Welcome to the Joke Bot!")

# Ask first joke
guess1 = input("Why couldn't the engineer fix the computer? ")
if guess1.lower() == "too many bits":
    print("Well done!\n")
    score += 1
else:
    print("too many bits\n")

# Ask second joke
guess2 = input("Why can you never trust atoms? ")
if guess2.lower() == "they make up everything":
    print("Well done!\n")
    score += 1
else:
    print("they make up everything\n")

# Ask third joke
guess3 = input("What do you call a fish made of two sodium atoms? ")
if guess3 == "2Na" or guess3.lower() == "two na" or guess3.lower() == "tuna":
    print("Well done!\n")
    score += 1
else:
    print("2Na\n")


# final message
print("You got", str(score), "of the jokes. Nice!")
print("Thanks for playing", name, "!")
