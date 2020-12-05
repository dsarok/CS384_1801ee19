import  sqlite3
import os
import bcrypt
import pandas as pd
import time
import threading
import  re
total_time_of_quiz=60
ENDED=False
Timeleft=True
def counter(x):
      global Timeleft
      for x in range(x):
            if ENDED:
                  break
            time.sleep(1)
      Timeleft=False
      os.system('clear')
      print('TEST HAS ENDED \n PRESS ANY KEY TO VIEW THE RESPONSE')
conn=sqlite3.connect('project1_quiz_cs384.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS project1_registration(
    username VARCHAR(50),
    passcode VARCHAR(50),
    Name VARCHAR(50),
    Roll VARCHAR(50),
    WHATSAPP VARCHAR(10)
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
                  time.sleep(3)
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
                  ROLL = input('ENTER YOUR ROLL NUMBER: ').upper()
                  passcode=input('ENTER YOUR PASSWORD: ')
                  passcode2=input('ENTER YOUR PASSWORD AGAIN: ')
                  if passcode==passcode2:
                        passcode = passcode.encode("utf-8")
                        wats=input('ENTER YOUR WHATSAPP NUMBER')
                        while True:
                             if len(wats)==10:
                                   if re.finditer(r'[0-9]+',wats):
                                         break

                        hashed_passcode = bcrypt.hashpw(passcode, bcrypt.gensalt())
                        c.execute('''INSERT INTO project1_registration(username,passcode,Name,Roll,WHATSAPP) VALUES(?,?,?,?,?)''',(name,hashed_passcode,NAME,ROLL,wats))
                        conn.commit()
                        print('OK now new account created with username {} and password {}'.format(name,str(passcode2)))
                        input('NOW GO TO LOG IN PORTAL by pressing any key')
                        os.system('clear')
                        option='1'
                  else:
                        print('YOUR PASSWORD DIDNT MATCHED')
                        input()
quizno=0
quizfilename=''
while True:
      try:
            quizno=input('Enter the value of quiz number :')
            quizfilename = 'quiz_wise_questions/' + 'q' + quizno + '.csv'
            datfile = pd.read_csv(quizfilename)
            break
      except:
            print('Enter a valid quiz number')
            time.sleep(1)
            os.system('clear')
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

t1=threading.Thread(target=counter,args=(total_time_of_quiz,))
t1.start()

for x in range(len(compulsary)):
      if Timeleft == False:
            break
      os.system('clear')
      print('quiz is of ', total_time_of_quiz, ' seconds')
      print('Roll no: ',ROLLNO,' Name :',NAME)
      print('Unattempted Questions',unattempted)
      print("q",x+1," ",questions[x])
      print('1',optiona[x])
      print('2',optionb[x])
      print('3',optionc[x])
      print('4',optiond[x])
      if compulsary[x]=='y':
            print('yes')
      else:
            print('no')
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
            totalmrks=totalmrks+int(wrongans[x])
            print(totalmrks)
            wrongchoice += 1
      if res=='1' or res=='2' or res=='3' or res=='4':
            response.append(res)
      else:
            response.append('s')
      print('totalmarks',totalmrks)
time.sleep(1)
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
sz=len(response)
rem=len(questions)-sz
for x in range(rem):
      response.append('s')

optiona=optiona.tolist()
optionb=optionb.tolist()
optionc=optionc.tolist()
optiond=optiond.tolist()
correctans=correctans.tolist()
answers=answers.tolist()
wrongans=wrongans.tolist()
questions=questions.tolist()
rollnowise={
      'quiz_question':questions,
      'option1':optiona,
      'option2':optionb,
      'option3':optionc,
      'option4':optiond,
      'correct_option':correctans,
      'positive marks':answers,
      'negative marks':wrongans,
      'response':response,

}
listing=[correctchoice,wrongchoice,unattempted,totalmrks,totalmarks]

legend={
      'Legend':['correctchoice','wrongchoice','unattempted','marks','fullmarks'],
      'Total':listing
}
dataframe=pd.DataFrame(rollnowise)
dataframe2=pd.DataFrame(legend)
dataframe3=pd.concat([dataframe,dataframe2],ignore_index=False,axis=1)
filename='individual_responses/'+'q'+str(quizno)+'_'+str(ROLLNO)+".csv"
dataframe3.to_csv(filename)
c.execute('SELECT * FROM project1_marks')
conn.commit()
quizfile={
      'Roll':[str(ROLLNO)],
      'MARKS':[str(totalmrks)]
}
dataset=pd.DataFrame(quizfile)
filename="quiz_wise_responses/"+'scores_'+'q'+quizno+'.csv'
dataset.to_csv(filename,mode='a')
conn.close()