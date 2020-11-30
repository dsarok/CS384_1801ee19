import pandas as pd
import re
pattern=re.compile(r'\d+(\D+)\d+')
def group_allocation(filename, number_of_groups):

    datafile = pd.read_csv(filename)
    unique_branches = set()

    for x in datafile['Roll']:
        if pattern.search(x):
            unique_branches.add(pattern.search(x).group(1))

    print(unique_branches)
    files = dict()
    for x in unique_branches:
        files[x] = dict()
        files[x]['Roll'] = list()
        files[x]['Name'] = list()
        files[x]['Email'] = list()

    for pos in range(len(datafile['Roll'])):
        branch = pattern.search(datafile['Roll'][pos]).group(1)
        files[branch]['Roll'].append(datafile['Roll'][pos])
        files[branch]['Name'].append(datafile['Name'][pos])
        files[branch]['Email'].append(datafile['Email'][pos])

    datastrength = {}
    datastrength['STRENGTH'] = []
    datastrength['BRANCH_CODE'] = []

    for x in unique_branches:
        new_files = {}
        new_files['Roll'] = list()
        new_files['Roll'] = files[x]['Roll'].copy()
        new_files['Name'] = list()
        new_files['Name'] = files[x]['Name'].copy()
        new_files['Email'] = list()
        new_files['Email'] = files[x]['Email'].copy()
        data = pd.DataFrame(new_files)
        data=data.sort_values(['Roll'])
        data.to_csv(x + '.csv')
        datastrength['BRANCH_CODE'].append(x)
        datastrength['STRENGTH'].append(len(files[x]['Roll']))

    dataa = pd.DataFrame(datastrength)
    dataa = dataa.sort_values(['STRENGTH', 'BRANCH_CODE'])

    groupwisedistribution = {}
    pos=0
    for x in unique_branches:
        y = len(files[x]['Roll'])
        groupwise = int(y / number_of_groups)
        groupwisedistribution[x] = list()
        for z in range(number_of_groups):
            groupwisedistribution[x].append(groupwise)
        remaining = y % number_of_groups
        pos = pos % number_of_groups
        for z in range(remaining):
            groupwisedistribution[x][pos] += 1
            pos=pos+1
            pos=pos%number_of_groups
    groups = {}
    for x in range(number_of_groups):
        groups[x] = {}
        groups[x]['NAME'] = list()
        groups[x]['ROLL'] = list()
        groups[x]['e-MAIL'] = list()
    for x in unique_branches:
        pos = 0
        flag = 0
        size = (groupwisedistribution[x][pos])
        while pos < number_of_groups:

            groups[pos]['NAME'].append(files[x]['Name'][flag])
            groups[pos]['ROLL'].append(files[x]['Roll'][flag])
            groups[pos]['e-MAIL'].append(files[x]['Email'][flag])
            flag = flag + 1
            size -= 1
            if size == 0:
                pos = pos + 1
                if pos < number_of_groups:
                    size = (groupwisedistribution[x][pos])




    dataa.to_csv('branch_strength.csv')

    for x in range(number_of_groups):
        datafile = pd.DataFrame(groups[x])
        datafile=datafile.sort_values('ROLL')
        srop=str(x+1)
        filenames = "Group_G" + (srop).zfill(2) + ".csv"
        datafile.to_csv(filenames)
    stats_file={}
    stats_file['Group number']=list()
    stats_file['total']=list()
    for x in unique_branches:
        stats_file[x]=list()
    for x in range(number_of_groups):
        filenime='Group_G'+str(x+1).zfill(2)
        stats_file['Group number'].append(filenime)
        total=0
        for y in unique_branches:
            stats_file[y].append(groupwisedistribution[y][x])
            total+=groupwisedistribution[y][x]
        stats_file['total'].append(total)
    datafiles=pd.DataFrame(stats_file)

    datafiles.to_csv('stats grouping.csv')


filename = "Btech_2020_master_data.csv"
number_of_groups = 12


group_allocation(filename,number_of_groups)