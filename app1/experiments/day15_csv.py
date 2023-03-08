import csv

with open("../files/weather.csv") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:  # start at 1 as 0 is the column labels
    if row[0] == city:
        print(row[1])

