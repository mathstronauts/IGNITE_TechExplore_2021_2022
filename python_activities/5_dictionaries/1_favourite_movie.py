"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""

# Favourite Movie/TV Show Dictionary

# Poll the class for their favourite movie or TV show, ask for some options on Google Classroom BEFORE CLASS
# OR poll for the following examples: Friends, Interstellar, The Office, Parasite, Other

# sample of poll results:
#   Friends: 4
#   Interstellar: 6
#   The Office: 2
#   Parasite: 7

# create dictionary
dict = {
    "Friends": 4,
    "Interstellar": 6,
    "The Office": 2,
    "Parasite": 7,
    }

print(dict)  # print the entire dictionary
print(len(dict))  # length is the number of items in the dictionary

# accessing dictionary items
options = dict.keys()
Friends_vote = dict["Friends"]
votes = dict["Friends"] + dict["Interstellar"] + dict["The Office"] + dict["Parasite"]

print("Options:", options)
print("Friends Votes:", Friends_vote)
print("Total Votes:", votes)
