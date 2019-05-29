# Simulating multiple rolls of two six sided die and analyzing the results

import pygal
from die import Die

# Creating an instance of our die
# Because no secondary argument is passed to the class, the die is assumed to be six sided
die_1 = Die()
die_2 = Die()

results = []

# Rolling the die 100 times and storing the results in an array
for roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Ensuring that the results were generated -- optional check
# print(results)

# Conducting a frequency analysis of the results
frequencies = []
combined_sides = die_1.sides + die_2.sides
for value in range(2, combined_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Ensuring that the frequency analysis was conducted properly -- optional check
print(frequencies)

# Creating a simple histogram of the results from this experiment
hist = pygal.Bar()

hist.title = "Results from Rolling Two D6 (n=1000)"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Result Frequency"

hist.add("2x D6", frequencies)
hist.render_to_file("2xD6_Histogram.svg")
