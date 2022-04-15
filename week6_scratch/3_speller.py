#words = dict() #defining a dictionary, toherwise known as a hash table

words = set() #set is another datatype in python that allows it to handle duplicates, allows you to thorw things into it using
# a function as simple as add

#you use def to define a function, then the name of the function and the argument
def check(word):
    if word.lower() in words:
        return True
    else:
        return False

def load(dictionary):
  file = open(dictionary, "r") #opening a file named dictionary
  for line in file: #iterate through every line in the file
      word = line.rstrip() #removing each line’s newline with rstrip
      words.add(word)
  file.close()
  return True

def size():
    return len(words) #return the length of the dictionary

def unload(): #Theres nothing to manually unload, Python manages memory for us
    return True