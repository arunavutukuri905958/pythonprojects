import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='students'
)

cur=mydb.cursor()

cur.execute('select * from students  limit 3,5')
get_data=cur.fetchall()

for i in get_data:
    print(i)