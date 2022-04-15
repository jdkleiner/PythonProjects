import csv

# This is a dictionary we've called houses (Also called a hash table)
# It has keys, and values
houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

# with open("hogwarts.csv", "r") as file: # In "r" read mode, just want to read it
#     reader = csv.reader(file)
#     next(reader) # skip the header row with next(reader)
#     for row in reader:
#         house = row[1] # Get the current person's house, The second item in each row w/ row[1]
#         houses[house] += 1 # Adds to the running tally for that house

# We can improve our program by reading each row as a dictionary, using the first row in the file as the keys for each value:
# This is a more readable way to do it
with open("hogwarts.csv", "r") as file:
    reader = csv.DictReader(file) # Using DictReader in the csv library
    for row in reader:
        house = row["House"] # This method uses the column names in the csv
        houses[house] += 1

# Print out the count for each house
for house in houses:
    count = houses[house]
    print(f"{house}: {count}")