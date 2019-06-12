# Plotting daily and cumulative precipitation for Lawrence, KS
# This file requires the Lawrence weather csv file to run
# If the git repository isn't cloned, the pathway in the filename variable may need to be ammended

import csv

from matplotlib import pyplot as plt
from datetime import datetime

# Grabbing data for Death Valley
filename = 'chapter_16/lawrence_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, daily_precip, cumulative_precip, c_p = [], [], [], 0
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%m/%d/%Y")
            d_p = float(row[8])
            c_p += d_p
        except ValueError:
            print(current_date, "Missing data")
        else:
            dates.append(current_date)
            daily_precip.append(d_p)
            cumulative_precip.append(c_p)


# Plotting the mean temperature comparison
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.bar(dates, daily_precip, color='red')
ax1.set_ylabel('Daily Precipitation(in)', color='red')
for tl in ax1.get_yticklabels():
    tl.set_color('red')

ax2 = ax1.twinx()
ax2.plot(dates, cumulative_precip, color='blue')
ax2.set_ylabel('Cumulative Precipitation(in)', color='blue')
for tl in ax2.get_yticklabels():
    tl.set_color('blue')

plt.title("2014 Precipitation\nLawrence,KS")
plt.savefig("Lawrence_Precip.png")
plt.show()
