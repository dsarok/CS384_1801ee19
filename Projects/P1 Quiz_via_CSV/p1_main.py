import  sqlite3
import os
import bcrypt
import pandas as pd
import time
import threading
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
conn=sqlite3.connect('student.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students(
    username VARCHAR(50),
    passcode VARCHAR(50),
    Name VARCHAR(50),
    Roll VARCHAR(50)
 )''')
ROLLNO=0
NAME=''
conn.commit()
print('Choose your options')
name=''
passcode=''
while True:
      os.system('clear')
      a = '''1.LOGIN\n2.SIGNUP\nchoose 1 for LOGIN OR 2 for SIGNUP\n'''
      option = input(a)
      if option=='1':
            name= input('USERNAME:')
            passcode= input('PASSWORD:').encode("utf-8")
         #   c.execute("SELECT * FROM students WHERE username='{}' AND passcode='{}'".format(name, hashed_passcode))

            c.execute("SELECT passcode FROM students WHERE username = '{}'".format(name,))
            conn.commit()
            data=c.fetchall()
            found=False
            for key in data:
                  for keys in key:
                        ignore = 0
                        if bcrypt.checkpw(passcode, keys):
                              print('Logged in as ', name)
                              found=True
                              c.execute("SELECT Roll,Name FROM students WHERE username='{}'".format(name))
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
            c.execute("SELECT username FROM students where username='{}' ".format(name))
            conn.commit()
            data=c.fetchall()
            if len(data)>0:
                  print('This username is already taken')
                  input()
            else:
                  NAME = input('ENTER YOUR NAME: ')
                  ROLL = input('ENTER YOUR ROLL NUMBER: ').upper()
                  passcode=input('ENTER YOUR PASSWORD: ')
                  passcode2=input('ENTER YOU PASSWORD AGAIN: ')
                  if passcode==passcode2:
                        passcode = passcode.encode("utf-8")
                        hashed_passcode = bcrypt.hashpw(passcode, bcrypt.gensalt())
                        c.execute('''INSERT INTO students(username,passcode,Name,Roll) VALUES(?,?,?,?)''',(name,hashed_passcode,NAME,ROLL))
                        conn.commit()
                        print('OK now new account created with username {} and password {}'.format(name,str(passcode2)))
                        input('NOW GO TO LOG IN PORTAL by pressing any key')
                        os.system('clear')
                        option='1'
                  else:
                        print('YOUR PASSWORD DIDNT MATCHED')
                        input()
quizno=input('Enter the value of quiz number')
quizfilename='quiz_wise_questions/'+'q'+quizno+'.csv'
datfile=pd.read_csv(quizfilename)
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
print('YOU HAVE ',total_time_of_quiz,' seconds left')
t1=threading.Thread(target=counter,args=(total_time_of_quiz,))
t1.start()

for x in range(len(compulsary)):
      if Timeleft == False:
            break
      os.system('clear')
      print('Roll no: ',ROLLNO,' Name :',NAME)
      print('Unattempted Questions',unattempted)
      print(x+1,".",questions[x])
      print('1',optiona[x])
      print('2',optionb[x])
      print('3',optionc[x])
      print('4',optiond[x])
      print('compalsary',compulsary[x])
      print('marks',answers[x])
      print('wrongans',wrongans[x])
      res=input('Enter your response 1,2,3,4,s(to skip):\n')
      if res==str(correctans[x]):
            totalmrks=totalmrks+int(answers[x])
            correctchoice+=1
      elif res!='1' and res!='2' and res!='3' and res!='4':
            if compulsary[x]=='y':
                  totalmrks=totalmrks-int(wrongans[x])
            wrongchoice+=1
            unattempted+=1
      else:
            totalmrks=totalmrks-int(wrongans[x])
            print(totalmrks)
            wrongchoice += 1
      if res=='1' or res=='2' or res=='3' or res=='4':
            response.append(res)
      else:
            response.append('s')
      print('totalmarks',totalmrks)
ENDED=True
print(response,totalmrks)
print(NAME,ROLLNO)
TABLENAME='''CREATE TABLE IF NOT EXISTS project1_marks(
ROLL VARCHAR(10),
QUIZNO INT,
TOTAL INT)'''
c.execute(TABLENAME)
conn.commit()
c.execute('''INSERT INTO project1_marks VALUES (?,?,?)''',(ROLLNO,quizno,totalmrks))
conn.commit()
rollnowise={
      'quiz_question':[questions],
      'option1':[optiona],
      'option2':[optionb],
      'option3':[optionc],
      'option4':[optiond],
      'correct_option':[correctans],
      'marks_choice':[response],
      'Legend':['correctchoice','wrongchoice','unattempted','totalmrks','totalmarks']
}
dataframe=pd.DataFrame.from_dict(rollnowise,orient='index')
dataframe=dataframe.transpose()
filename='q'+str(quizno)+str(ROLLNO)+".csv"
dataframe.to_csv(filename)
conn.close()