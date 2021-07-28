from matplotlib import pyplot as plt
import csv

with open("countries-aggregated.csv") as data:
    reader = csv.reader(data)
    next(reader)