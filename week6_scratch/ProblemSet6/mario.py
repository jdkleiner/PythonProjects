def main():
    height = get_height()
    for i in range(1, height + 1):
        # add white space buffer
        print(" " * (height - i), end = '')
        # add left pyramid block(s), spaces and right pyramid block(s)
        print("#" * i,"","#" * i, end="\n")


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            # if n > 0:
            if n > 0 and n < 9:
                break
        except ValueError:
            print("That's not an integer!")
    return n

main()