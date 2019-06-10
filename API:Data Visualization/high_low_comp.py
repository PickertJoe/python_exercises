# Analyzing the high and low temperatures for Death Valley
# This file requires the Death Valley weather csv file to run
# If the git repository isn't clone, the pathway in the filename variable may need to be ammended

import csv

from matplotlib import pyplot as plt
from datetime import datetime

# Grabbing data for Death Valley
filename = 'chapter_16/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    means_DV, dates_DV = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            mean = int(row[2])
        except ValueError:
            print(current_date, "Missing data")
        else:
            dates_DV.append(current_date)
            means_DV.append(mean)

# Grabbing data for Sitka
filename = 'chapter_16/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    means_S, dates_S = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            mean = int(row[2])
        except ValueError:
            print(current_date, "Missing data")
        else:
            dates_S.append(current_date)
            means_S.append(mean)

# Plotting the mean temperature comparison
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_S, means_S, c='red', alpha=0.8, label="Sitka, AK")
plt.plot(dates_DV, means_DV, c='blue', alpha=0.8, label="Death Valley, CA")
plt.title("Daily Mean Temperatures, 2014")
plt.xlabel('', fontsize=16)
plt.legend()
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig("Mean_Comparison.png")
plt.show()
