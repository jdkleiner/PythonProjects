# Simple
# for i in range(3):
#     print("meow")

# Better
# def main():
#     for i in range(3):
#         meow()

# def meow():
#     print("meow")

# main()

# Even Better: functions can take arguments, too!
def main():
    meow(3)

def meow(n):
    for i in range(n):
        print("meow")

main()



# Additional method: This solves problems with including
# our code in libraries, but we won’t need to consider
# that yet, so we can simply call main().
# if __name__ == "__main__":
#     main()