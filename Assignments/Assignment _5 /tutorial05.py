import os
import re


def rename_FIR(folder_name):
    e_padding = int(input("Enter the Episode Number Padding:"))
    list = os.listdir("./Subtitles/" + folder_name)
    for name in list:
        try:
            e_no = re.search(r'Episode\s(\d+)', name).group(1)
        except:
            e_no = re.search(r'Ep\s(\d+)', name).group(1)

        ext = '.' + re.search(r'(.{3})$', name).group(1)

        e_name = re.search(r'\d\s-\s(.*?)-', name)

        if not e_name:
            e_name = ''
        else:
            e_name = ' - ' + e_name.group(1)

        while 1:
            if len(e_no) >= e_padding:
                break
            else:
                e_no = '0' + e_no

        new_name = folder_name + ' - ' + 'Episode' + ' ' + e_no + e_name

        try:
            os.rename("./Subtitles/" + folder_name + "/" + name,
                      "./Subtitles/" + folder_name + "/" + new_name + ext)
        except WindowsError:
            I = 1
            while 1:
                if os.path.isfile("./Subtitles/" + folder_name + "/" + new_name + ' (' + str(I) + ')' + ext):
                    I = I + 1
                else:
                    os.rename("./Subtitles/" + folder_name + "/" + name, "./Subtitles/" +
                              folder_name + "/" + new_name + ' (' + str(I) + ')' + ext)
                    break


def rename_Game_of_Thrones(folder_name):
    # rename Logic
    s_padding = int(input("Enter the Season Number Padding:"))
    e_padding = int(input("Enter the Episode Number Padding:"))
    list = os.listdir("./Subtitles/" + folder_name)
    for name in list:

        e_no = re.search(r'\s(\d+)x(\d+)\s', name).group(2)
        s_no = re.search(r'\s(\d+)x(\d+)\s', name).group(1)
        ext = '.' + re.search(r'(.{3})$', name).group(1)

        e_name = re.search(r'\s(\d+)x(\d+)\s-\s(.*?)\.', name)

        if not e_name:
            e_name = ''
        else:
            e_name = ' - ' + e_name.group(3)

        while 1:
            if len(e_no) >= e_padding:
                break
            else:
                e_no = '0' + e_no

        while 1:
            if len(s_no) >= s_padding:
                break
            else:
                s_no = '0' + s_no

        new_name = folder_name + ' - Season ' + s_no + ' Episode ' + e_no + e_name

        try:
            os.rename("./Subtitles/" + folder_name + "/" + name,
                      "./Subtitles/" + folder_name + "/" + new_name + ext)
        except WindowsError:
            I = 1
            while 1:
                if os.path.isfile("./Subtitles/" + folder_name + "/" + new_name + ' (' + str(I) + ')' + ext):
                    I = I + 1
                else:
                    os.rename("./Subtitles/" + folder_name + "/" + name, "./Subtitles/" +
                              folder_name + "/" + new_name + ' (' + str(I) + ')' + ext)
                    break


def rename_Sherlock(folder_name):
    # rename Logic
    s_padding = int(input("Enter the Season Number Padding:"))
    e_padding = int(input("Enter the Episode Number Padding:"))
    list = os.listdir("./Subtitles/" + folder_name)
    for name in list:

        s_no = re.search(r'\.S(\d+)', name).group(1)
        e_no = re.search(r'E(\d+)\.', name).group(1)
        ext = '.' + re.search(r'(.{3})$', name).group(1)

        while 1:
            if len(e_no) >= e_padding:
                break
            else:
                e_no = '0' + e_no

        while 1:
            if len(s_no) >= s_padding:
                break
            else:
                s_no = '0' + s_no

        new_name = folder_name + ' - Season ' + s_no + ' Episode ' + e_no

        try:
            os.rename("./Subtitles/" + folder_name + "/" + name,
                      "./Subtitles/" + folder_name + "/" + new_name + ext)
        except WindowsError:
            I = 1
            while 1:
                if os.path.isfile("./Subtitles/" + folder_name + "/" + new_name + ' (' + str(I) + ')' + ext):
                    I = I + 1
                else:
                    os.rename("./Subtitles/" + folder_name + "/" + name, "./Subtitles/" +
                              folder_name + "/" + new_name + ' (' + str(I) + ')' + ext)
                    break


def rename_Suits(folder_name):
    # rename Logic
    s_padding = int(input("Enter the Season Number Padding:"))
    e_padding = int(input("Enter the Episode Number Padding:"))
    list = os.listdir("./Subtitles/" + folder_name)
    for name in list:

        e_no = re.search(r'\s(\d+)x(\d+)\s', name).group(2)
        s_no = re.search(r'\s(\d+)x(\d+)\s', name).group(1)
        ext = '.' + re.search(r'(.{3})$', name).group(1)

        e_name = re.search(r'\s(\d+)x(\d+)\s-\s(.*?)\.', name)

        if not e_name:
            e_name = ''
        else:
            e_name = ' - ' + e_name.group(3)

        while 1:
            if len(e_no) >= e_padding:
                break
            else:
                e_no = '0' + e_no

        while 1:
            if len(s_no) >= s_padding:
                break
            else:
                s_no = '0' + s_no

        new_name = folder_name + ' - Season ' + s_no + ' Episode ' + e_no + e_name

        try:
            os.rename("./Subtitles/" + folder_name + "/" + name,
                      "./Subtitles/" + folder_name + "/" + new_name + ext)
        except WindowsError:
            I = 1
            while 1:
                if os.path.isfile("./Subtitles/" + folder_name + "/" + new_name + ' (' + str(I) + ')' + ext):
                    I = I + 1
                else:
                    os.rename("./Subtitles/" + folder_name + "/" + name, "./Subtitles/" +
                              folder_name + "/" + new_name + ' (' + str(I) + ')' + ext)
                    break


def rename_How_I_Met_Your_Mother(folder_name):
    s_padding = int(input("Enter the Season Number Padding:"))
    e_padding = int(input("Enter the Episode Number Padding:"))
    list = os.listdir("./Subtitles/" + folder_name)
    for name in list:

        e_no = re.search(r'\s(\d+)x(.*?)\s', name).group(2)
        s_no = re.search(r'\s(\d+)x(.*?)\s', name).group(1)
        ext = '.' + re.search(r'(.{3})$', name).group(1)

        e_name = re.search(r'\s(\d+)x(.*?)\s-\s(.*?)\.', name)

        if not e_name:
            e_name = ''
        else:
            e_name = ' - ' + e_name.group(3)

        while 1:
            if len(e_no) >= e_padding:
                break
            else:
                e_no = '0' + e_no

        while 1:
            if len(s_no) >= s_padding:
                break
            else:
                s_no = '0' + s_no

        new_name = folder_name + ' - Season ' + s_no + ' Episode ' + e_no + e_name

        try:
            os.rename("./Subtitles/" + folder_name + "/" + name,
                      "./Subtitles/" + folder_name + "/" + new_name + ext)
        except WindowsError:
            I = 1
            while 1:
                if os.path.isfile("./Subtitles/" + folder_name + "/" + new_name + ' (' + str(I) + ')' + ext):
                    I = I + 1
                else:
                    os.rename("./Subtitles/" + folder_name + "/" + name, "./Subtitles/" +
                              folder_name + "/" + new_name + ' (' + str(I) + ')' + ext)
                    break


while 1:
    print("Select the Series number to Rename:")
    print("1. FIR")
    print("2. Game of Thrones")
    print("3. Sherlock")
    print("4. Suits")
    print("5. How I Met Your Mother")
    print("6. Exit...")
    i = int(input())

    if i == 1:
        rename_FIR("FIR")

    elif i == 2:
        rename_Game_of_Thrones("Game of Thrones")

    elif i == 3:
        rename_Sherlock("Sherlock")

    elif i == 4:
        rename_Suits("Suits")

    elif i == 5:
        rename_How_I_Met_Your_Mother("How I Met Your Mother")

    elif i == 6:
        print("Thank You!")
        print()
        break
    else:
        print("Wrong Input Please input from the given list number")
    print()
