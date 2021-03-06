# Analyzing the high and low temperatures for Death Valley
# This file requires the Death Valley weather csv file to run
# If the git repository isn't clone, the pathway in the filename variable may need to be ammended

import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'chapter_16/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "Missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Printing out a numbered index of all the column headers in this file -- optional check
# for index, column_header in enumerate(header_row):
#    print(index, column_header)

# Printing out the high temperatures -- optional check
# print(highs)

# Plotting the high temperature data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.8)
plt.plot(dates, lows, c='blue', alpha=0.8)
plt.fill_between(dates, highs, lows, facecolor='grey', alpha=0.5)
plt.title("Daily High and Low Temperatures, 2014\nDeath Valley, CA")
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig("Death_Valley.png")
plt.show()
