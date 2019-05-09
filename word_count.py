# a simple function definition to constrain the word count of a text document
def count_words(filename):
    """Reads in a text file and outputs the number of words it contains"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
        except FileNotFoundError:
            message = "The file " + " could not be found."
            message += "Check the file's pathway or user entry."
            print(message)
        else:
            #Approximates the word count of the file
            words = contents.split()
            num_words = len(words)
            print("The file " + filename + " has " + str(num_words) " words in it.")
