# running an elementary conditional test
emperor = 'Hadrian'
print("Is the current emperor Hadrian? I predict yes.")
print(emperor == 'Hadrian')

print("\nIs the current emperor Antoninus Pius? I predict no.")
print(emperor == "Antoninus Pius")

# checking the existence of a unique username
user1 = "john"
user2 = "John"
print("\nThe user name " + user2 + " is currently taken: ")
print(user2.lower() == user1)

# checking the existence of a case-specific unique username
print("\nThe user name " + user2 + " is currently taken: ")
print(user2 == user1)

# creating a list of Roman emperors
princeps = ["Augustus", 'Trajan', 'Hadrian', 'Marcus Aurelius', 'Vespasian']
# conditional tests for the list
print("\nHadrian is one of my favorite emperors: ")
print('Hadrian' in princeps)
print("\nNero is one of my favorite emperors: ")
print('Nero' in princeps)
print("\nNero is one of my least favorite emperors: ")
if 'Nero' not in princeps:
    print("This is indeed true.")
else:
    print("That is incorrect.")

# creating a list of login names
users = ['Paul', 'Peter', 'Mary', 'Francios', 'Wume', 'Admin']
for user in users:
    if user.lower() == 'admin':
        print('\nWelcome to the server, ' + user + '.')
    else:
        print('\nWelcome back, ' + user + '.')

# creating a list of admin names and a list of login names
# running a conditional test to search for overlaps
admins = ['Frank', 'Richard', 'Abby', 'Penelope']
users = ['Penelope', 'Gauis', 'Lucius', 'Frank']
for user in users:
    if user in admins:
        print('Welcome back administrator: ' + user + '.')
    else:
        print('Welcome back user: ' + user + '.')

# creating an if-elif chain to assign appropriate ordinal endings
ordinals = []
for value in range(1, 10):
    ordinals.append(value)
print(ordinals)
for value in ordinals:
    if value == 1:
        print(str(value) + "st")
    elif value == 2:
        print(str(value) + "nd")
    elif value == 3:
        print(str(value) + "rd")
    else:
        print(str(value) + "th")
