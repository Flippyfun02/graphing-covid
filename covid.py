from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from cs50 import SQL
import datetime, sys

def make_list(query, thelist, key): # format list so not dict
    for i in query:
        thelist.append(i[key])
    return thelist

if len(sys.argv) != 2:
    sys.exit("Usage: python3 covid.py 'Country'")

plt.title("Covid Cases")
plt.xlabel("Time")
plt.ylabel("Number of Cases")

# Each date has the countries' case reports

db = SQL("sqlite:///data.db")

# create list of dates for x axis
datesDict = db.execute("SELECT Date FROM countries WHERE Country = 'Afghanistan'")
dates = []
dates = make_list(datesDict, dates, 'Date')
for i in range(len(dates)): # format date
    dates[i] = datetime.datetime.strptime(dates[i], '%Y-%m-%d')

# create list of confirmed cases for y axis
while True:
    try: # check if country is in database
        find_confirmed = db.execute("SELECT Confirmed FROM countries WHERE Country = ?", sys.argv[1])
        confirmed = []
        confirmed = make_list(find_confirmed, confirmed, "Confirmed")
        for i in range(len(confirmed)): # int case numbers
            confirmed[i] = int(confirmed[i])

        # plot
        plt.plot(dates, confirmed, color = "red")
        break
    except: # if not, still do not return error
        print("Country is unavailable.")
plt.xticks(rotation = 30)
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.show()