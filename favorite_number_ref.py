# Refacoting "favorite_number.py" to split the program into several functions

import json


def get_stored_number():
    """Retrieves a previously stored favorite number"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as file_object:
            number = json.load(file_object)
    except ValueError:
        return None
    else:
        return number


def get_new_number():
    """Accepts and records a favorite number if one is not already stored"""
    favorite_number = input("Please type your favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as file_object:
        json.dump(favorite_number, file_object)
    return favorite_number


def greet_user():
    """Greets the user by their favorite number, calling each function as necessary"""
    number = get_stored_number()
    if number:
        print("Aha, I remember you! You're favorite number is " + number + "!")
    else:
        get_new_number()
        print('Great, I will remember this!')


greet_user()

# Asking the user to confirm the validity of the recorded number
# If it is not correct, they will be prompted to enter the correct value

while True:
    valid = input("Was I correct?(Y/N): ")
    if valid.title() == 'Y':
        print("See, I told you I had a good memory!")
        break
    elif valid.title() == 'N':
        print("Oops, let's try that again.")
        get_new_number()
        greet_user()
    else:
        print("Sorry, that isn't a valid input. Please try again.")
