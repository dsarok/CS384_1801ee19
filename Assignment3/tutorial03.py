import csv
import re
import  os
import  operator
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
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            country = str.lower(row[2])
            try:
                f=open(directory+"/"+"country/"+country+".csv",'w')
                writer=csv.writer(f)
                writer.writerow(row)
            except:
                pass


def email_domain_extract():
    os.makedirs(directory+"/analytics/email_domain")
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:

            try:
                x = (row[3].split('@'))
                open(directory+"/email_domain/"+(x[1].split('.')[0])+".csv",'a')
                print(x[1].split('.')[0])
            except:
                pass

def gender():
    os.makedirs(directory+'/gender')
    open(directory+'/gender/'+'male.csv','w')
    open(directory+'/gender/'+'female.csv','w')
    pass


def dob():
    filename=directory+'/dob'
    os.makedirs(filename)
    open(filename+'/bday_1995_1999.csv','w')
    open(filename+'/bday_2000_2004.csv','w')
    open(filename + '/bday_2005_2009.csv','w')
    open(filename + '/bday_2010_2014.csv','w')
    open(filename + '/bday_2015_2020.csv','w')


def state():
   states=set()
   with open('studentinfo_cs384.csv', 'r') as file:
       reader = csv.reader(file)
       for row in reader:
           states.add(row[-1])
   os.makedirs(directory+'/state')
   for x in states:
       t=directory+'/state/'+x+".csv"
       open(t,'w')


def blood_group():
    bloodgroup=set()
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            bloodgroup.add(row[-2])
    bloodgroup.remove('blood_group')
    # os.makedirs(directory+"/blood_group")
    for x in bloodgroup:
        r=directory+"/blood_group/"+str.lower(x)+'.csv'
        open(r,'w')

def new_file():
    with open('studentinfo_cs384_names_split.csv','w') as file:
        writer=csv.writer(file)
        writer.writerow(['id','first_name','last_name','country','email','gender','dob','blood_group','state'])
        with open('studentinfo_cs384.csv','r') as file2:
            reader=csv.reader(file2)
            next(reader)
            for read in reader:
                id=read[0]
                newname=read[1].split(' ')
                country=read[2]
                email=read[3]
                gender=read[4]
                dob=read[5]
                blood_group=read[6]
                state=read[7]
                writer.writerow([id,newname[0],newname[-1],country,email,gender,dob,blood_group,state])


# Create the new file here and also sort it in this function only.
def new_file_sort():
    data = csv.reader(open('studentinfo_cs384_names_split.csv','r'))
    next(data)
    writer=csv.writer(open('studentinfo_cs384_names_split_sorted_first_name.csv','w'))
    writer.writerow(['id','first_name','last_name','country','email','gender','dob','blood_group','state'])
    sortedlist = sorted(data, key=operator.itemgetter(1))
    for x in sortedlist:
        writer.writerow(x)
country()