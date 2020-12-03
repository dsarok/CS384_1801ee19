import csv
import re
with open('studentinfo_cs384.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


