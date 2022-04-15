#from cs50 import get_int

#x = get_int("x: ")
#y = get_int("y: ")
#print(x + y)

#x = int(input("x: ")) #using python input function and a type cast using int function
#y = int(input("y: "))
#print(x + y)

#try:
#     x = int(input("x: "))
# except:
#     print("That is not an int!")
#     exit()
# try:
#     y = int(input("y: "))
# except:
#     print("That is not an int!")
#     exit()
# print(x + y)

# THE FOLLOWING CHUNK WORKS
# try:
#     x = int(input("x: "))
# except ValueError:
#     print("That is not an int!")
#     exit()
# try:
#     y = int(input("y: "))
# except ValueError:
#     print("That is not an int!")
#     exit()
# print(x + y)


# NEW
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

z = x / y
# print(z)
print(f"{z:.50f}")