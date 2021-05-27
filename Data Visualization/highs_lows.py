import csv
from datetime import datetime
from matplotlib import pyplot as plt

#first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
#print(first_date)

# Get dates and high temperatures from file.
filename = 'Data Visualization\data\sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = row[8]
        highs.append(high)

        low = row[9]
        lows.append(low)
# Plot data.

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title('Daily high and low temperatures 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
