# Simulating multiple rolls of a six sided die and analyzing the results

import pygal
from die import Die

# Creating an instance of our die
# Because no secondary argument is passed to the class, the die is assumed to be six sided
die = Die()

results = []

# Rolling the die 100 times and storing the results in an array
for roll in range(1000):
    result = die.roll()
    results.append(result)

# Ensuring that the results were generated -- optional check
# print(results)

# Conducting a frequency analysis of the results
frequencies = []
for value in range(1, die.sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Ensuring that the frequency analysis was conducted properly -- optional check
print(frequencies)

# Creating a simple histogram of the results from this experiment
hist = pygal.Bar()

hist.title = "Results from Rolling One D6 (n=1000)"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Result Frequency"

hist.add("D6", frequencies)
hist.render_to_file("D6_Histogram.svg")
