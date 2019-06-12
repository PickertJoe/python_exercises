# Using JSON functionaility to store and retrieve user-provided input

import json

filename = 'favorite_number.json'
try:
    with open(filename) as file_object:
        number = json.load(file_object)
except ValueError:
    number = input('Please type your favorite number: ')
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)
        print('Great, I will remember this!')
else:
    print("Aha, I remember you! You're favorite number is " + number + "!")
