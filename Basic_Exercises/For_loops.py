# creating a list of favorite pizza toppings
pizzas = ["mushroom", "garlic", "spinach"]
# creating a replicable message
message = "My favorite pizza topping is "
# repeating message for each topping
for pizza in pizzas:
    print(message + pizza.title() + ".")
# additional message after the termination of the loop
print("\nI love pizza!")

# populating a list from 1 to 5
numbers = list(range(1, 6))
print(numbers)

# creating a list of the first ten square numbers
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# creating the same list with list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

# creating a list of values 1-20 inclusive
twenty = []
for value in range(1, 21):
    twenty.append(value)
print(twenty)

# creating the same list with a list comprehension
twenty = [value for value in range(1, 21)]
print(twenty)

# creating a list from 1 to 1,000,000 using list comprehension
million = [value for value in range(1, 1000001)]
# print(million)

# creating a list of odd numbers
odds = []
for value in range(1, 20, 2):
    odds.append(value)
print(odds)

# creating a list of multiples of 3 from 3 to 30 inclusive
threes = []
for value in range(3, 33, 3):
    threes.append(value)
print(threes)

# Repeating this process with a comprehension list
threes = [value for value in range(3, 33, 3)]
print(threes)

# creating a list of the first 10 cubic numbers
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# repeating a process with a simple for loop
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)

# creating a tuple or Roman emperors
princeps = ("Augustus", 'Trajan', 'Hadrian', 'Marcus Aurelius', 'Claudius')
for name in princeps:
    print(name)

# attempting to incorrectly modify a member of the tuple
# this should return a type error
#princeps[4] = "Vespasian"
# for name in princeps:
#    print(name)

# correctly reassigning the last member of the tuple
princeps = ("Augustus", 'Trajan', 'Hadrian', 'Marcus Aurelius', 'Claudius')
princeps = ("Augustus", 'Trajan', 'Hadrian', 'Marcus Aurelius', 'Vespasian')
for name in princeps:
    print(name)
