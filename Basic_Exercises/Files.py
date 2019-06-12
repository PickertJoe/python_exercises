# Basic exercise in reading and writing external files
# If executed on a Mac OS, this program may include extraneous characters from the RFT file format
# Double check files before running

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# repeating the process but reading the file line by line
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

# storing the lines of the document in a list and printing them later
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# reading a new, user-generated text file using three separate methods
# using relative file paths
with open('text_files/learning_python.txt') as file_object:
    contents = file_object.read()
    print("\n" + contents.rstrip())

with open('text_files/learning_python.txt') as file_object:
    print("\n")
    for line in file_object:
        print(line.rstrip())

with open('text_files/learning_python.txt') as file_object:
    lines = file_object.readlines()

print("\n")
for line in lines:
    print(line.rstrip())

# replacing 'Python' in the previous exercise with 'C++'
with open('text_files/learning_python.txt') as file_object:
    lines = file_object.readlines()
print("\n")
for line in lines:
    line = line.replace('Python', 'C++')
    print(line.rstrip())

# a simple program to ask the user for their name before writing it to a text document
filename = 'name_storage.txt'
print('---Welcome to the Name Codifier!---')
names = []
while True:
    print("\nType 'q' at any time to quit.")
    holder = input("Please enter your name: ")
    if holder.title() == 'Q':
        print("\nExiting program...")
        break
    else:
        print("Sending to database...")
        names.append(holder)

with open(filename, 'w') as file_object:
    for line in names:
        file_object.write(line.title() + "\n")

# a similar program but one that continually appends the storage file instead of rewriting it
filename = 'roman_data.txt'
print('---Welcome to the Favorite Roman Codifier!---')
names = []
while True:
    print("\nType 'q' at any time to quit.")
    holder = input("Please enter your favorite Roman: ")
    if holder.title() == 'Q':
        print("\nExiting program...")
        break
    else:
        print("Sending to database...")
        names.append(holder)

with open(filename, 'a') as file_object:
    for line in names:
        file_object.write(line.title() + "\n")
