from matplotlib import pyplot as plt
from cs50 import SQL

plt.title("Covid Cases")
plt.xlabel("Time")
plt.ylabel("Number of Cases")

# Each date has the countries' case reports

db = SQL("sqlite:///data.db")

# create list of dates for x axis
datesDict = db.execute("SELECT Date FROM countries WHERE Country = 'Afghanistan'")
dates = []
for i in datesDict:
    dates.append(i['Date'])

# create list of confirmed cases
select_country = "United Kingdom"
confirmed = db.execute("SELECT Confirmed FROM countries WHERE Country = ?", select_country)
uk_confirmed = []

for i in confirmed:
    uk_confirmed.append(i['Confirmed'])

# plot
plt.plot(dates, uk_confirmed, color = "red")
plt.show()