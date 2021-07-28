from matplotlib import pyplot as plt
import cs50, csv

plt.title("Covid Cases")
plt.xlabel("Time")
plt.ylabel("Number of Cases")

# Each date has the countries' case reports
# countries = {country_name : country}
# country = [{date : YYYY-MM-DD, cases, etc}]

countries = []
country = []
with open("countries-aggregated-2021-07-26.csv") as data:
    reader = csv.DictReader(data)
    for i in reader:
        

# plt.show()