import csv
import sys


def main():

    # TODO: Check for command-line usage
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py FILENAME.CSV FILENAME.TXT")

    # TODO: Read database file into a variable
    reader = csv.reader(open(sys.argv[1]))

    # make list from csv header
    str_list = next(reader)

    # remove name item
    str_list = str_list[1:]
    # print(str_list)
    # print(f"{reader}")

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as dna_file:
        dna_mem = dna_file.read()
    # print(f"{dna_mem}")

    # TODO: Find longest match of each STR in DNA sequence
    # define list
    count_list = []
    sequence = dna_mem

    # generate a single list containing counts for each STR in the DNA sequence
    for subsequence in str_list:
        # print(subsequence)
        match_max = longest_match(sequence, subsequence)
        # print(match_max)

        # add value to list
        count_list.append(match_max)
    # print(count_list)

    # TODO: Check database for matching profiles
    # define list
    match_list = []
    # loop through each individuals str counts and compare to list for a match
    for s in reader:
        # print("name: " + s[0])
        rows_s = s[1:len(s)]
        # conver row_s list to integer (b/c count_list contains integers)
        rows_s = [int(x) for x in rows_s]

        # print(rows_s)
        if (count_list) == rows_s:
            match_name = s[0]
            match_list.append(match_name)
    # print(match_list)

    if len(match_list) > 0:
        print(match_list[0])
    else:
        print("No match")

    # return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
