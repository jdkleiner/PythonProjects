from sys import argv

# if len(argv) == 2:
#     print(f"hello, {argv[1]}")
# else:
#     print("hello, world")

#USE
#python argv.py Joey Kleiner
#In this above, "argv.py" is the first argument, Joey the second, Kleiner the third

# for arg in argv:
#     print(arg)

# If you dont want to print out the name of the program
# Start at element 1 instead of 0, and go all the way to the end
for arg in argv[1:]:
# for arg in argv[:-1]:
    print(arg)