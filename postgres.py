import psycopg2
import sys
def data_connection(sql):
  database=input("enter database name: ")
  conn = psycopg2.connect(host='localhost',user='postgres',password='root',port='1995',database=database)
  cursor = conn.cursor()
  sql=sql
  cursor.execute(sql)

  a=input('''Enter 1 number if you want to save:\nEnter 2nd number if you want show all data\nEnter 3 if you want to delete:  ''')
  if a=="1":
    conn.commit()
  
  elif a=="2":
    show= cursor.fetchall()
    print(show)

  elif a=="3":
    conn.commit()

  conn.close()
  return cursor
  

  

def save():
  rollno=sys.argv[1]
  name=sys.argv[2]
  marks=sys.argv[3]
  fees=sys.argv[4]
  
  
  
  sql="insert into student(rollno, name, marks, fees) values({},'{}',{},{})" .format(rollno,name,marks,fees)
  data_connection(sql)
  print('data created sucessfull')



def delete():
  rollno=sys.argv[1]
  sql="delete from student where rollno={0}".format(rollno)
  data_connection(sql)
  print("1 row sucessfully delete")


def get():
  sql="select * from student"
  data_connection(sql)
  

      
save()
get()
delete()






