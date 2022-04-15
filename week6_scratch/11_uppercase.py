from cs50 import get_string

# THIS method iterates over each character in a string:
# before = get_string("Before:  ")
# print("After:   ", end="")
# for c in before:
#     print(c.upper(), end="")
# print()

# BETTER way that uppercases the entire word all at once
# before = get_string("Before:  ")
# after = before.upper()
# print(f"After:   {after}")

before = get_string("Before:  ")
print(f"After:   {before.upper()}") #YOU can actually put a small amout of logic inside curly braces