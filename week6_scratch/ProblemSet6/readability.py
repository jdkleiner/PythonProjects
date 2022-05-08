# TODO

s = input("Text: ")
s = str(s)
# print(f"{s}")

# initialise counters to 0
numletters = 0
numwords = 0
numsent = 0

# loop through each character in the input text
# add to the counters if a letter, space, or end of sentence
for i in s:
    # print(f"{i}")
    if (i.isalpha()):
        numletters += 1
    elif (i == ' '):
        numwords += 1
    elif (i == '.' or i == '!' or i == '?'):
        numsent += 1
# add 1 to final word count, since spaces are in between words
numwords += 1
# print(f"numletters: {numletters}")
# print(f"numwords: {numwords}")
# print(f"numsent: {numsent}")

# calculate the average number of letters per 100 words in the text
L = (numletters / numwords) * 100

# calculate the average number of sentences per 100 words in the text
S = (numsent / numwords) * 100

# calculate the Coleman-Liau index
index = round((0.0588 * L) - (0.296 * S) - 15.8)

# print grade level as it relates to senior undergraduate reading level
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")