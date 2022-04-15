# from sys import argv, exit

# if len(argv) != 2:
#     print("Missing command-line argument")
#     exit(1) # exit with 1

# print(f"hello, {argv[1]}")
# exit(0) # exit with 0


# We can import the entire sys library, and make it clear in our program where these functions come from:
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)