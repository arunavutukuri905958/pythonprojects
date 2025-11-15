import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='students'
)

cur=mydb.cursor()
get_data1=('''select * from students  where name like '%a%' ''')


cur.execute(get_data1)

get_data=cur.fetchall()

for i in get_data:
    print(i)