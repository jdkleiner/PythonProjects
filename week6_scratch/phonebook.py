# from cs50 import get_string

# people = {
#     "Carter": "+1-617-495-1000",
#     "David": "+1-949-468-2750"
# }

# name = get_string("Name: ")
# if name in people:
#     number = people[name]
#     print(f"Number: {number}")

import csv
from cs50 import get_string

# file = open("phonebook.csv", "a") # "a" means open it in append format, if it exists it'll add to the bottom of it

# name = get_string("Name: ")
# number = get_string("Number: ")

# writer = csv.writer(file) #This is functionality is python specific
# writer.writerow([name, number])

# file.close()

name = get_string("Name: ")
number = get_string("Number: ")

with open("phonebook.csv", "a") as file: #This method using "with" keeps you from having to close it explicitly

    writer = csv.writer(file)
    writer.writerow([name, number])

