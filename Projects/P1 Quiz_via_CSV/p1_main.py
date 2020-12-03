import  sqlite3
import os
import bcrypt
import pandas as pd
conn=sqlite3.connect('student.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students(
    username VARCHAR(50),
    passcode VARCHAR(50)
 )''')
# c.execute("INSERT INTO students values('ram','jai_shree_ram')")
# c.execute('''INSERT INTO students VALUES ('jaishreeram','jaishreeram')''')
# x=c.execute('''SELECT * FROM students''')
# conn.commit()
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
                  passcode=input('ENTER YOUR PASSWORD: ')
                  passcode2=input('ENTER YOU PASSWORD AGAIN: ')
                  if passcode==passcode2:
                        passcode = passcode.encode("utf-8")
                        hashed_passcode = bcrypt.hashpw(passcode, bcrypt.gensalt())
                        c.execute('''INSERT INTO students(username,passcode) VALUES(?,?)''',(name,hashed_passcode))
                        conn.commit()
                        print('OK now new account created with username {} and password {}'.format(name,str(passcode)))
                        input('NOW GO TO LOG IN PORTAL by pressing any key')
                        os.system('cls')
                        option='1'
                  else:
                        print('YOUR PASSWORD DIDNT MATCHED')
                        input()
quizno=input('Enter the value of quiz number')
quizfilename='quiz_wise_questions/'+'q'+quizno+'.csv'
print('quiz_wise_questions/'+'q'+quizno+'.csv')
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
for x in range(len(compulsary)):
      print(x+1,".",questions[x])
      print('1',optiona[x])
      print('2',optionb[x])
      print('3',optionc[x])
      print('4',optiond[x])
      print('compalsary',compulsary[x])
      print('marks',answers[x])
      print('wrongans',wrongans[x])
      print('correct answer is ',correctans[x])
      res=input('Enter your response 1,2,3,4,5:\n')
      if res==str(correctans[x]):
            totalmrks=totalmrks+int(answers[x])
            print(totalmrks,answers[x],'aslfdjl')
      elif res!='1' or res!='2' or res!='3' or res!='4':
            if compulsary[x]=='y':
                  totalmrks=totalmrks-int(wrongans[x])
      else:
            totalmrks=totalmrks-int(wrongans[x])
            print(totalmrks)
      if res=='1' or res=='2' or res=='3' or res=='4':
            response.append(res)
      else:
            response.append('s')
      print(totalmrks)
print(response,totalmrks)

conn.close()