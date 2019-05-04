# this program will deal with simple input operations

# asking a user for their choice of rental car
prompt = "What make of car would you like to rent: "
rental = input(prompt)
print("Sounds good, let me see if I can find you a " + rental + ".")

# asking a dining party for their group size
prompt = "\nWelcome to McDonald's! How many do we have this evening? : "
size = input(prompt)
size = int(size)
if size > 8:
    print("Sorry folks, we're looking at a 45 minute to two hour wait.")
else:
    print("Great, if you'll all follow me...")
