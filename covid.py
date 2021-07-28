from matplotlib import pyplot as plt
import csv

plt.title("Covid Cases")
plt.xlabel("Time")
plt.ylabel("Number of Cases")

# Each date has the countries' case reports

with open("countries-aggregated.csv") as data:
    reader = csv.reader(data)
    next(reader)

plt.show()