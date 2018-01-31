import csv
import pandas as pd

# with open('data.csv') as file:
#     reader = csv.reader(file)
# 
#     for data in reader:
#         print(data[0], data[1], data[2])

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
print(df)