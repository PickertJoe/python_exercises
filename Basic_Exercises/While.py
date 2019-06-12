# this program will deal with simple while loops that take user input

# creating a loop to take the name of favorite romans
prompt = "\nWho would you say is your favorite Roman?"
prompt += "\nIf you're sick of talking to me, just type 'quit': "
roman = " "
while roman != "quit":
    roman = input(prompt)
    if roman != "quit":
        print("\nAh yes, " + roman.title() + " is my favorite Roman too!")

# creating a loop to report ticket prices depending on age
print("\nWelcome to the movie theater!")
prompt = "Your ticket price depends on your age."
prompt += "\nHow old are you?: "
while True:
    print("\nWhen you're ready to leave, just type 'quit'")
    age = input(prompt)
    if age == "quit":
        break
    try:
        int(age)
    except ValueError:
        print("\nLook kid, I don't know who you think you are, \
                \nbut this is a family establishment.")
        print("Please tell me your actual age.")
    else:
        if int(age) < 3:
            print("\nNo worries, you can get in for free!")
        elif int(age) >= 3 and int(age) < 12:
            print("\nYour ticket will be $10.")
        elif int(age) >= 12:
            print("\nYour ticket will be $15.")

# using a while loop to transfer the contents of one list to another
# creating a list of sandwiches to prepare
print("\nMy friends just ordered some sandwiches.")
sandwich_orders = ['tuna', 'chicken', 'pb&j', 'veggie', 'tofu']
sandwich_made = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    sandwich_made.append(sandwich)
    print("Making a " + sandwich.upper() + " sandwich.")
print("--- Sandwich List---")
for sandwich in sandwich_made:
    print(sandwich.upper() + " sandwich")

# recreating the previous exercise to run out of a certain type of sandwich
sandwich_orders = ['pastrami', 'chicken', 'pastrami', 'pb&j', 'veggie', 'pastrami', 'tofu']
sandwich_made = []
print("\nMy friends just ordered some sandwiches.\nHere is the list of orders:")
for sandwich in sandwich_orders:
    print(sandwich.title())
print("\n")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        print("Sorry, friend, but I'm all out of pastrami!")
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')
    print("Making a " + sandwich.upper() + " sandwich.")
    sandwich_made.append(sandwich)
print("\nHere is a list of all the sandwiches I made:")
for sandwich in sandwich_made:
    print(sandwich.title())

# using a while loop to populate a simple dictionary of users' vacation destinations
vacations = {}
flag = True
prompt1 = "\nWhat is your name?: "
prompt2 = "What is your dream vacation destination?: "
prompt3 = "Would you like to let someone else enter their information?('Y/N'): "
while flag:
    name = input(prompt1)
    destination = input(prompt2)
    vacations[name] = destination
    more = input(prompt3)
    if more.title() == 'N':
        flag = False
    elif more.title() == 'Y':
        continue
    else:
        print("Invalid input, returning to start.")
print("\n---Dream Vacation Destinations---")
for name, destination in vacations.items():
    print(name.title() + " wants to visit " + destination.title() + ".")

