import  os
title=input("Main Title of the Web Series")
def rename_FIR(folder_name):
    season = input("Season Number Padding (take int input):")
    episode = input("Episode Number Padding (take int input):")
    Files=list()
    for root, dirs, files in os.walk("./Subtitles/FIR"):
        for filename in files:
            Files.append(filename)
    for files in Files:
        x=files.split('-')
        newfilename=x[0]+"-"+x[1]+"-"

def rename_Game_of_Thrones(folder_name):
    season = input("Season Number Padding (take int input):")
    episode = input("Episode Number Padding (take int input):")
    

def rename_Sherlock(folder_name):
    season = input("Season Number Padding (take int input):")
    episode = input("Episode Number Padding (take int input):")
    

def rename_Suits(folder_name):
    season = input("Season Number Padding (take int input):")
    episode = input("Episode Number Padding (take int input):")
    

def rename_How_I_Met_Your_Mother(folder_name):
    season = input("Season Number Padding (take int input):")
    episode = input("Episode Number Padding (take int input):")



if title=="How I Met Your Mother":
    rename_How_I_Met_Your_Mother("Subtitles/How_I_Met_Your_Mother")
elif title=="Suits":
    rename_Suits("Suits")
elif title=="Sherlock":
    rename_Sherlock("Subtitles/Sherlock")
elif title=="Game of Thrones":
    rename_Game_of_Thrones("Subtitles/Game_of_Thrones")
elif title=="FIR":
    rename_FIR("Subtitles/FIR")