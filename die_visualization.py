# Simulating multiple rolls of a six sided die and analyzing the results

import pygal
from die import Die

# Creating an instance of our die
# Because no secondary argument is passed to the class, the die is assumed to be six sided
die = Die()

# Rolling the die 100 times and storing the results in an array
results = [die.roll() for value in range(1000)]

# Ensuring that the results were generated -- optional check
# print(results)

# Conducting a frequency analysis of the results
frequencies = [results.count(value) for value in range(1, die.sides + 1)]


# Ensuring that the frequency analysis was conducted properly -- optional check
print(frequencies)

# Creating a simple histogram of the results from this experiment
hist = pygal.Bar()

hist.title = "Results from Rolling One D6 (n=1000)"
hist.x_labels = [number for number in range(1, 7)]
hist.x_title = "Result"
hist.y_title = "Result Frequency"

hist.add("D6", frequencies)
hist.render_to_file("D6_Histogram.svg")
