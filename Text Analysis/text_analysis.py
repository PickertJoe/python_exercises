# pulling in the text of Alice in Wonderland

with open('chapter_10/alice.txt') as file_object:
    contents = file_object.read()

# using the .split() module to approximate the number of words in the text
words = contents.split()
num_words = len(words)
file = "Alice in Wonderland"
# This method produces the same number of words found in the book exercise
print("The manuscript of " + file + " has " + str(num_words) + " words in it.")

# A function to replicate this process was created in the separate file word_count.py
# Importing this function from the separate module

from word_count import count_words

count_words("chapter_10/alice.txt")
count_words("chapter_10/moby_dick.txt")
count_words("chapter_10/siddhartha.txt")

# Calling the function for a nonexistent file to test try-except block
count_words("chapter_10/crime_and_punishment.txt")
