import csv
import re
import  os
directory=os.getcwd()+"/analytics"
def std(x):

    if x == '01':
        return 'btech'
    elif x == '11':
        return "mtech"
    elif x == '12':
        return "msc"
    elif x == '21':
        return "phd"

def course():
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            roll = re.split('[A-Z]+', row[0])
            branch = (re.split('[0-9]+', row[0]))
            try:
               var =std( roll[0][-2:len(roll[0])])
               a=str(roll[0][0:2])+"_"+str.lower(branch[1])+"_"+var+'.csv'
               c=directory+"/course/"+str.lower(branch[1])+"/"+var
               os.makedirs(c)
               f=open(c+"/"+a+".csv",'a')


            except:
                f=open(directory+"/course/"+"misc.csv",'a')

def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
