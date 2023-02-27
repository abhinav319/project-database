import psycopg2


def mydbConnection(host_name, user_name, user_password,database,port):
    connection = psycopg2.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database,
            port=port
        )
    return connection

connection = mydbConnection("localhost", "postgres", "root","abhinav","1995")


def mydbSave(connection):
  rollno = int(input("Enter roll no. "))
  name = input("Enter Name ")
  marks = int(input("Enter marks. "))
  fees = int(input("Enter fees "))
  cursor = connection.cursor()
  sql= "insert into student(rollno, name, marks, fees) values({},'{}',{},{})" .format(rollno,name,marks,fees)
  cursor.execute(sql)
  connection.commit()
  print("Database created successfully")
  return connection

def get(connection):
  cursor=connection.cursor()
  sql="select * from student"
  cursor.execute(sql)
  show=cursor.fetchall()
  print(show)



def delete(connection):
  rollno=int(input("Enter rool no you want to delete= "))
  cursor=connection.cursor()
  sql="delete from student where rollno={0}".format(rollno)
  cursor.execute(sql)
  connection.commit()
  print("1 row sucessfully delete")
  return connection

  

mydbSave(connection)
get(connection)
delete(connection)
