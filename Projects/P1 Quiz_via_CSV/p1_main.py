import sqlite3
import os
import bcrypt
import pandas as pd
import time
import threading
import re


total_time_of_quiz=20
ENDED=False
Timeleft=True

def counter(x):
      global Timeleft
      for x in range(x):
            if ENDED:
                  break
            time.sleep(1)
      Timeleft=False
      print('TEST HAS ENDED')
conn=sqlite3.connect('project1_quiz_cs384.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS project1_registration(
    username VARCHAR(50),
    passcode VARCHAR(50),
    Name VARCHAR(50),
    Roll VARCHAR(50),
    whatsapp VARCHAR(10)
 )''')
ROLLNO=0
NAME=''
conn.commit()
print('  Choose your options : ')
print("")
name=''
passcode=''
while True:
      try:
            os.system('cls')
      except:
            os.system('clear')
      a = '''1. LOGIN\n2. SIGNUP\n  choose 1 for LOGIN OR 2 for SIGNUP\n '''
      option = input(a)
      if option=='1':
            name= input('USERNAME: ')
            passcode= input('PASSWORD:').encode("utf-8")
         #   c.execute("SELECT * FROM students WHERE username='{}' AND passcode='{}'".format(name, hashed_passcode))

            c.execute("SELECT passcode FROM project1_registration WHERE username = '{}'".format(name,))
            conn.commit()
            data=c.fetchall()
            found=False
            for key in data:
                  for keys in key:
                        ignore = 0
                        if bcrypt.checkpw(passcode, keys):
                              print('Logged in as ', name)
                              found=True
                              c.execute("SELECT Roll,Name FROM project1_registration WHERE username='{}'".format(name))
                              conn.commit()
                              x=c.fetchall()
                              ROLLNO=(x[0][0])
                              NAME=x[0][1]
                              break
            if found==False:
                  print('Wrong Username or Password')
            else:
                  break

      if option=='2':

            name=input('ENTER YOUR DESIRED USERNAME: ')
            c.execute("SELECT username FROM project1_registration where username='{}' ".format(name))
            conn.commit()
            data=c.fetchall()
            if len(data)>0:
                  print('This username is already taken')
                  input()
            else:
                  NAME = input('ENTER YOUR NAME: ')
                  print("")
                  ROLL = input(' ENTER YOUR ROLL NUMBER: ').upper()
                  print("")
                  passcode=input(' ENTER YOUR PASSWORD: ')
                  passcode2=input(' Please Confirm Your Password: ')
                  if passcode==passcode2:
                        while True:
                              print("")
                              wats = input("Enter Your What's App Number: ")
                              if(len(wats)!= 10):
                                    continue
                              else:
                                   re.finditer(r'[0-9]+',wats)
                                   break
                        passcode = passcode.encode("utf-8")
                        hashed_passcode = bcrypt.hashpw(passcode, bcrypt.gensalt())
                        c.execute('''INSERT INTO project1_registration(username,passcode,Name,Roll,whatsapp) VALUES(?,?,?,?,?)''',(name,hashed_passcode,NAME,ROLL,wats))
                        conn.commit()
                        print(' Congratulations! Your new account has created with username {} and password {}'.format(name,str(passcode2)))
                        input('NOW Press ENTER LOG IN PORTAL by pressing any key')
                        try:
                              os.system('cls')
                        except:
                              os.system('clear')
                        option='1'
                  else:
                        print('''YOUR PASSWORD DIDN'T MATCHED''')
                        input()

print("  Welcome to the Quiz Portal: ")

path = r'C:\Users\hp\OneDrive\Documents\CS 384 Git Assignments\CS384_2020_skeleton\Projects\P1 Quiz_via_CSV\quiz_wise_questions'
quiz_quantity = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path,name))])
print("")
print(f"There are {quiz_quantity} quizzes")
while True:
      quiz_input = int(input(" Enter the Quiz number you want to give: \n "))
      if quiz_input > quiz_quantity:
            print("This Quiz doesn't exists. Please enter correct input")
            print("")
      else:
            break

quiz_filename = path + "/q" + str(quiz_input) + ".csv"
datfile=pd.read_csv(quiz_filename)

questions=datfile['question']
compulsary=datfile['compulsory']
optiona=datfile['option1']
optionb=datfile['option2']
optionc=datfile['option3']
optiond=datfile['option4']
answers=datfile['marks_correct_ans']
wrongans=datfile['marks_wrong_ans']
correctans=datfile['correct_option']
response=[]
totalmrks=0
correctchoice=0
wrongchoice=0
unattempted=0
totalmarks=0
for x in answers:
      totalmarks+=int(x)
print('YOU HAVE ',total_time_of_quiz,' seconds for the quiz! All the best.')
time.sleep(2)
t1=threading.Thread(target=counter,args=(total_time_of_quiz,))
t1.start()


for x in range(len(compulsary)):
      if Timeleft == False:
            break
      try:
            os.system('cls')
      except:
            os.system('clear')
      print(' Roll no: ',ROLLNO,'   Candidate name: ',NAME)
      print("")
      #print('Unattempted Questions',unattempted)
      print(x+1,".",questions[x])
      print('1. ',datfile['option1'][x])
      print('2. ',datfile['option2'][x])
      print('3. ',datfile['option3'][x])
      print('4. ',datfile['option4'][x])
      if datfile['compulsory'][x].lower() == 'y':
            compulsion = "YES"
      else:
            compulsion = "NO"
      print('Is Question compulsory: ',compulsion)
      print('Correct_marks:  ',datfile['marks_correct_ans'][x])
      print('Negative_marks:  ',datfile['marks_wrong_ans'][x])
      res=input('Enter your response 1,2,3,4,s(to skip):\n')
      if res==str(correctans[x]):
            totalmrks=totalmrks+int(answers[x])
            correctchoice += 1
      elif res!='1' and res!='2' and res!='3' and res!='4':
            if datfile['compulsory'][x].lower() =='y':
                  totalmrks=totalmrks + int(wrongans[x])
            wrongchoice += 1
            unattempted += 1
      else:
            totalmrks=totalmrks + int(wrongans[x])
            #print(totalmrks)
            wrongchoice += 1
      if res=='1' or res=='2' or res=='3' or res=='4':
            response.append(res)
      else:
            response.append('s')
      #print('totalmarks',totalmrks)


#with keyboard.Listener(on_press = on_press, on_release = on_release )as listener:
 #     listener.join()

ENDED=True

print(response,totalmrks)
try:
      os.system('cls')
except:
      os.system('clear')
print(NAME,ROLLNO)
print(f"Your Response has been recorded and saved in file with filename as: q{quiz_input}_{ROLLNO}")

TABLENAME='''CREATE TABLE IF NOT EXISTS project1_marks(
ROLL VARCHAR(10),
QUIZNO INT,
TOTAL INT)'''
c.execute(TABLENAME)
conn.commit()
c.execute('''INSERT INTO project1_marks VALUES (?,?,?)''',(ROLLNO,quiz_input,totalmrks))
conn.commit()
legend = ['correctchoice','wrongchoice','unattempted','totalmrks','totalmarks']
totals = [correctchoice,wrongchoice,unattempted,totalmrks,totalmarks]
questions=datfile['question']
compulsary=datfile['compulsory']
optiona=optiona.tolist()
optionb=optionb.tolist()
optionc=optionc.tolist()
optiond=optiond.tolist()
correctans=correctans.tolist()
answers=answers.tolist()
wrongans=datfile['marks_wrong_ans'].tolist()
#correctans=datfile['correct_option'].tolist()

index = 0
"""
for indx in range(0,max(5,len(datfile))):
      if indx < 5:
            ignore_completely = 0
      else:
            legend.append('NaN')

"""
rollnowise={
      'quiz_question':questions,
      'option1':optiona,
      'option2':optionb,
      'option3':optionc,
      'option4':optiond,
      'correct_option':correctans,
      'marks_choice':response,

}

#datatowrite = pd.DataFrame([questions,optiona,optionb,optionc,optiond,correctans,response,legend],columns=['quiz_question','option1','option2','option3','option4','correct_option','marked_choice','Legend'])

legend_list = {
      'Total' : totals,
      'Legend': legend
}
dataframe2 = pd.DataFrame(legend_list)
dataframe1=pd.DataFrame(rollnowise)
dataframe = pd.concat([dataframe1,dataframe2],axis=1)
#dataframe=dataframe.transpose()
filename_path = r'C:\Users\hp\OneDrive\Documents\CS 384 Git Assignments\CS384_2020_skeleton\Projects\P1 Quiz_via_CSV\individual_responses'
filename = filename_path + '/q' + str(quiz_input) + "_" + str(ROLLNO)+".csv"
dataframe.to_csv(filename)
#datatowrite.to_csv(filename)
quizwise_filepath = r'C:\Users\hp\OneDrive\Documents\CS 384 Git Assignments\CS384_2020_skeleton\Projects\P1 Quiz_via_CSV\quiz_wise_responses'
quizwise_file = quizwise_filepath + '/scores_q' + str(quiz_input) + ".csv"
quizwise = {
      'Roll no.':[ROLLNO],
      'Total Marks Obtained': [totalmrks]
}
dataframe_quizwise = pd.DataFrame(quizwise)
if os.path.isfile(quizwise_file) == False:
      dataframe_quizwise.to_csv(quizwise_file, mode='a')
else:
      dataframe_quizwise.to_csv(quizwise_file,mode='a',header=False)


"""
c.execute("SELECT * FROM project1_marks")
conn.commit()
data_sheet = c.fetchall()
for itr in range(len(data_sheet)):
      roll_data = data_sheet[itr][0]
      quizno_data = data_sheet[itr][1]
      total_data = data_sheet[itr][2]
      file_data = "q" + str(quizno_data) + ".csv"
      
      data_forwrite = {
            'Roll No. ': 
      }
      df_data = pd
"""
conn.close()
