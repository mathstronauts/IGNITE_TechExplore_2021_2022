"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""
# Random Pizza Generator For Loop

import random

# Pizza toppings lists
crust = ['regular', 'thin', 'stuffed']  # index positions: regular = 0, thin = 1, stuffed = 2
meat = ['pepperoni', 'chicken', 'bacon', 'sausage'] 
veggie = ['mushroom', 'tomato', 'onion', 'olives', 'peppers', 'anchovies']

# Ask user to press "Enter"
input("Press Enter to put everything on your pizza!")
print("")

# print meat
for item in meat:  # print every item in the list
    print(item)

# print veggies
for item in veggie:
    print(item)

print("_____________")
print("\___________/")
