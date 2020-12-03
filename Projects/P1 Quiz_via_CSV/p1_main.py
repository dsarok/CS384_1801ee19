import  sqlite3
import os
import bcrypt

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


conn.close()