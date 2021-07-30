from matplotlib import pyplot as plt
from cs50 import SQL
import datetime

def make_list(query, thelist, key): # format list so not dict
    for i in query:
        thelist.append(i[key])
    return thelist

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
    dates[i] = datetime.datetime.strptime(dates[i], '%Y-%m-%d').strftime("%b %Y")

# create list of confirmed cases for y axis
select_country = "United Kingdom"
find_confirmed = db.execute("SELECT Confirmed FROM countries WHERE Country = ?", select_country)
confirmed = []
confirmed = make_list(find_confirmed, confirmed, "Confirmed")

# plot
plt.plot(dates, confirmed, color = "red")
plt.show()