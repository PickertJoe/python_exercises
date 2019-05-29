# Simple program to read and graph the high temperatures of a location
# This file requires the Sitka weather csv file to run
# If the git repository isn't clone, the pathway in the filename variable may need to be ammended

import csv

from matplotlib import pyplot as plt

filename = 'chapter_16/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

# Printing out a numbered index of all the column headers in this file -- optional check
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Printing out the high temperatures -- optional check
print(highs)

# Plotting the high temperature data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
plt.title("Daily High Temperatures, July 2014")
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
