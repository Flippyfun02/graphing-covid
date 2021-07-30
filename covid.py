from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from cs50 import SQL
from pylab import *
import datetime, sys

def make_list(query, thelist, key): # format list so not dict
    for i in query:
        thelist.append(i[key])
    return thelist

db = SQL("sqlite:///data.db")
colors = {"Confirmed" : "red", "Recovered" : "green", "Deaths" : "blue"}

# check command line arguments
if len(sys.argv) < 2:
    sys.exit("Usage: python3 covid.py 'Country 1'")

command = db.execute("SELECT Country FROM countries")
available_countries = []
available_countries = set(make_list(command, available_countries, 'Country'))

for i in range(1, len(sys.argv)):
    if sys.argv[i] not in available_countries:
        sys.exit(f"{sys.argv[i]} is not available. \nUsage: python3 covid.py 'Country 1'")

# set up figure
fig = plt.figure()
fig.suptitle('World Covid Cases', weight = 'bold')
subplots_adjust(hspace = 0.500)
fig.text(0.5, 0.025, 'Time', ha = 'center', va = 'center', weight = 'bold')
fig.text(0.04, 0.5, 'Number of Cases', ha = 'center', va = 'center', rotation = 'vertical', weight = 'bold')

# create list of dates for x axis
datesDict = db.execute("SELECT Date FROM countries WHERE Country = 'Afghanistan'")
dates = []
dates = make_list(datesDict, dates, 'Date')
for i in range(len(dates)): # format date
    dates[i] = datetime.datetime.strptime(dates[i], '%Y-%m-%d')

# create graphs | i is iterable
for i, v in enumerate(range(len(sys.argv) - 1)):
    v += 1
    i += 1
    ax = subplot(len(sys.argv) - 1, 1, v) # create subplot
    ax.set_title(sys.argv[i])
    
    # create list of data for each country
    for x in ["Confirmed", "Recovered", "Deaths"]:
        find = db.execute("SELECT Confirmed, Recovered, Deaths FROM countries WHERE Country = ?", sys.argv[i])
        print(find)
        data = []
        data = make_list(find, data, x)

        for y in range(len(data)):
            data[y] = int(data[y])

        # plot data
        ax.plot(dates, data, color = colors[x], label = x)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

fig.autofmt_xdate()
handles, labels = ax.get_legend_handles_labels() # get label information
fig.legend(handles, labels, loc = 'upper right')
plt.tight_layout(pad = 2.0, w_pad = 2.0, h_pad = 2.0)
plt.show()