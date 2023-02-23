import psycopg2




def registrationTask():
  rollno=int(input('enter the rollno '))
  name=input('enter the name ')
  marks=int(input('enter the marks'))
  fees=int(input('enter the fees '))
  con = psycopg2.connect(host='localhost',user='postgres',password='root',port='1995',database='abhinav')
  cursor=con.cursor()
  sql="insert into student(rollno, name, marks, fees) values({},'{}',{},{})" .format(rollno,name,marks,fees)
  cursor.execute(sql)
  con.commit()
  con.close()
  print('data created')

registrationTask()

def delete():
        conn = psycopg2.connect(host='localhost',user='postgres',password='root',port='1995',database='abhinav')
        cr=conn.cursor()
        dele=int(input('enter rollno you want to delete'))
        sql="delete from student where rollno={0}".format(dele)
        cr.execute(sql)
        conn.commit()
        print("1 row sucessfully delete")
        conn.close()
delete()

def get():
        conn = psycopg2.connect(host='localhost',user='postgres',password='root',port='1995',database='abhinav')
        cursor=conn.cursor()
        sql="select * from student"
        cursor.execute(sql)
        show=cursor.fetchall()
        print(show)
        
get()





