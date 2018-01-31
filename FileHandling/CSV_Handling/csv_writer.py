import csv

data = [
    'Name, Type, Age'.split(","),
    'Sachin, Batsman, 40'.split(","),
    'Virat, Batsman, 28'.split(","),
    'Dhoni, Batsman/Wk, 36'.split(","),
    'Umesh, Bowler, 29'.split(","),
    'Bhuvi, Bowler, 29'.split(",")
]

with open('data_1.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter = ',')

    for i in data:
        writer.writerow(i)