"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""
# Random Pizza Generator 
import random

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

# generate a random index position
crust_size = len(crust) #get the size of the crust list
meat_size = len(meat) #get the size of the meat list
veggie_size = len(veggie)#get the size of the veggie list

crust_idx = random.randint(0, crust_size - 1)
meat_idx = random.randint(0, meat_size - 1)
veggie_idx = random.randint(0, veggie_size - 1)

# message to users
selected_crust = crust[crust_idx]
selected_meat = meat[meat_idx]
selected_veggie = veggie[veggie_idx]


print("Your random pizza is:")
print(selected_meat, "and", selected_veggie, selected_crust, "crust pizza")

print("Enjoy!")
