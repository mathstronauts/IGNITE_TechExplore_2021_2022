"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""

# Random Pizza Generator - Dictionary
import random

# pizza lists
pizza_options = {
    "crust": ['regular', 'thin', 'stuffed'],
    "meat": ['pepperoni', 'chicken', 'bacon', 'sausage'],
    "veggie": ['mushroom', 'tomato', 'onion', 'olives', 'peppers', 'anchovies'],
    "surprise": ['chocolate', 'gummies', 'licorice', 'cherries']
    }

# message to users
print("Welcome to Random Pizza Generator! We have the following selections: ")
print("Crusts:", pizza_options["crust"])  # print all the items in the list by entering the list name
print("Meat:", pizza_options["meat"])
print("Veggies:", pizza_options["veggie"])

#Ask user to press "Enter"
input("Press Enter to generate a random pizza.") #dont need a variable because the user's input is not used else where in the code

selected_crust = random.choice(pizza_options["crust"])
selected_meat = random.choice(pizza_options["meat"])
selected_veggie = random.choice(pizza_options["veggie"])


print("Your random pizza is:")
print(selected_meat, "and", selected_veggie, selected_crust, "crust pizza")

print("Enjoy!")
