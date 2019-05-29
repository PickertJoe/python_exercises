# Analyzing the high and low temperatures of two different locations
# This file requires the Sitka and Death Valley weather csv files to run
# If the git repository isn't clone, the pathway in the filename variable may need to be ammended

import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'chapter_16/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)


# Printing out a numbered index of all the column headers in this file -- optional check
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Printing out the high temperatures -- optional check
print(highs)

# Plotting the high temperature data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.title("Daily High Temperatures, July 2014")
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
