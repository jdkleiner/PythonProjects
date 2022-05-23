from cs50 import get_int

n = get_int("n: ")

#note: dividing a number by 2 will either have 0 or 1 as a remainder, and thats how you determine if its even or odd 
if n % 2 == 0:
    print("even")
else:
    print("odd")