from cs50 import get_string

#s = get_string("Do you agree? ")

# Simplest
#if s == "Y" or s == "y":
# Better
# if s in ["Y", "y", "yes", "YES", "YeS"]:
#     print("Agreed.")
# elif s == "N" or s == "n":
#     print("Not agreed.")

# Bestter:
#s = s.lower()

# Best: you can chain functions together in python
s = get_string("Do you agree? ").lower()

if s in ["y", "yes"]:
    print("Agreed.")
elif s in ["n", "no"]:
    print("Not agreed.")