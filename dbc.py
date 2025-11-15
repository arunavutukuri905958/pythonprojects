import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='students'
)

cur=mydb.cursor()


data="""INSERT INTO students (name,class,email,ph_no)
values(%s,%s,%s,%s)"""

k=[
   ('junnu','5th','junnu@gmail.com',7788),('sam','9th','sam@gmail.com',0000),('jai','10th','jai@gamil.com',2029)]
cur.executemany(data,k)
mydb.commit()





