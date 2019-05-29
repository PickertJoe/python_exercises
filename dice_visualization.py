# Simulating multiple rolls of two six sided die and analyzing the results

import pygal
from die import Die

# Creating an instance of our die
# Because no secondary argument is passed to the class, the die is assumed to be six sided
die_1 = Die()
die_2 = Die()


# Rolling the die 100 times and storing the results in an array
results = [die_1.roll() + die_2.roll() for value in range(1000)]

# Ensuring that the results were generated -- optional check
# print(results)

# Conducting a frequency analysis of the results
combined_sides = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(2, combined_sides + 1)]

# Ensuring that the frequency analysis was conducted properly -- optional check
# print(frequencies)

# Creating a simple histogram of the results from this experiment
hist = pygal.Bar()

hist.title = "Results from Rolling Two D6 (n=1000)"
hist.x_labels = [value for value in range(2, 13)]
hist.x_title = "Result"
hist.y_title = "Result Frequency"

hist.add("2x D6", frequencies)
hist.render_to_file("2xD6_Histogram.svg")
