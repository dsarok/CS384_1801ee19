import csv
import re
with open('studentinfo_cs384.csv','r') as file:
    reader=csv.reader(file)

    for row in reader:

        roll=re.split('[A-Z]+',row[0])
        branch=(re.split('[0-9]+',row[0]))
        try:
            print(roll[0] ," ", branch[1])
        except:
            pass
