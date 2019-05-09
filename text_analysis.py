# pulling in the text of Alice in Wonderland

with open('pcc/chapter_10/alice.txt') as file_object:
    contents = file_object.read()

# using the .split() module to approximate the number of words in the text
words = contents.split()
num_words = len(words)
file = "Alice in Wonderland"
#This method produces the same number of words found in the book exercise
#print("The manuscript of " + file + " has " + str(num_words) + " words in it.")

#defining this function for late use
def count_words(filename):
    """Reads in a text file and outputs the number of words it contains"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = "The file could not be found."
        message += "Check the file's pathway or user entry."
        print(message)
    else:
        #Approximates the word count of the file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has " + str(num_words) + " words in it.")


