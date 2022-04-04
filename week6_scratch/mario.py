from cs50 import get_int

# Simple
# n = get_int("Height: ")

# for i in range(n):
#     print("#")

# Better the "pythonic way"
# while True:
#     n = get_int("Height: ")
#     if n > 0:
#         break

# for i in range(n):
#     print("#")

# Better
# def main():
#     height = get_height()
#     for i in range(height):
#         print("#")

# def get_height():
#     while True:
#         n = get_int("Height: ")
#         if n > 0:
#             break #this is how you break out of the loop
#     return n

# main()

# Best - Do it without any cs50 functions, and catch any value errors
# def main():
#     height = get_height()
#     for i in range(height):
#         print("#")

# def get_height():
#     while True:
#         try:
#             n = int(input("Height: "))
#             if n > 0:
#                 break
#         except ValueError:
#             print("That's not an integer!")
#     return n

# main()


# for i in range(4):
#     print("?", end="")
# print() #This pring is what places the prompt on the new line


#This also works, no loop needed:
# print("?" * 4)

#Make a 3x3 block
# for i in range(3):
#     for j in range(3):
#         print("#", end="")
#     print()


for i in range(3):
    print("#" * 3)