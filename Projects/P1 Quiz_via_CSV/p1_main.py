import  sqlite3
conn=sqlite3.connect('students.db')
c=conn.cursor()
c.execute('''CREATE TABLE students(
  username  text,
  password  text
  )
''')
print('Choose your options')
a='''1.LOGIN\n2.SIGNUP\nchoose 1 for Signup OR 2 for Login\n'''
option=input(a)
username=''
password=''
if option=='1':
      name=input('USERNAME:')
      password=input('PASSWORD:')
      c.execute("Select count(*) FROM students where username={} AND password={}".format(username,password))
      while len(c.fetchone())==0:
            print('Wrong username or Password')
            name = input('USERNAME:')
            password = input('PASSWORD:')
            c.execute("SELECT COUNT(*) FROM students WHERE username={} AND password={}".format(username, password))

conn.commit()
conn.close()
