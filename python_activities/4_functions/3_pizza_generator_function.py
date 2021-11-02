"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""
# Random Pizza Generator with Function

import random

# random selector function
def random_selector(List):
    List_size = len(List)
    a = random.randint(0, List_size - 1)
    return List[a]

# pizza lists
crust = ['regular', 'thin', 'stuffed']  # index positions: regular = 0, thin = 1, stuffed = 2
meat = ['pepperoni', 'chicken', 'bacon', 'sausage'] 
veggie = ['mushroom', 'tomato', 'onion', 'olives', 'peppers', 'anchovies']
surprise = ['chocolate', 'gummies', 'licorice', 'cherries']  # optional extra list

# message to users
print("Welcome to Random Pizza Generator! We have the following selections: ")
print("Crusts:", crust)  # print all the items in the list by entering the list name
print("Meat:", meat)
print("Veggies:", veggie)

#Ask user to press "Enter"
input("Press Enter to generate a random pizza.") #dont need a variable because the user's input is not used else where in the code

# message to users, implement function!
selected_crust = random_selector(crust)
selected_meat = random_selector(meat)
selected_veggie = random_selector(veggie)

print("Your random pizza is:")
print(selected_meat, "and", selected_veggie, selected_crust, "crust pizza")

print("Enjoy!")
