# THIS IS A LIST IN PYTHON
# scores = [72, 73, 33]

# average = sum(scores) / len(scores)
# print(f"Average: {average}")


from cs50 import get_int

# CREATE AN EMPTY LIST
scores = []
for i in range(3):
    score = get_int("Score: ")
    # scores.append(score)
    scores += [score] #acheives the same as the line above, but by concatenating lists instead (notice to do this you have to make the current score a list itself first)
                      # This is the same as doing it more verbosely like this: scores = scores + [score]
average = sum(scores) / len(scores)
print(f"Average: {average}")