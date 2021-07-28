from matplotlib import pyplot as plt
import cs50, csv

plt.title("Covid Cases")
plt.xlabel("Time")
plt.ylabel("Number of Cases")

# Each date has the countries' case reports
# countries = {country_name : country}
# country = [{Date : YYYY-MM-DD, Country : name, cases, etc}]

countries = []
country = []
temp_data = []
counter = 1

with open("countries-aggregated-2021-07-26.csv") as data:
    reader = csv.DictReader(data)
    for line in reader:
        keys = list(line) # list of keys
        for i in range(2, len(keys)):
            line[keys[i]] = int(line[keys[i]]) # ints confirmed, recovered, deaths

# plt.show()