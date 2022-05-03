# TODO

cardnum = int(input("Number: "))

if str(cardnum).startswith('3'):
    print("AMEX\n")
elif str(cardnum).startswith('5'):
    print("MASTERCARD\n")
elif str(cardnum).startswith('4'):
    print("VISA\n")
else:
    print("INVALID\n")