import mysql.connector

conn=mysql.connector.connect(host="localhost",database='mydb',user='root',password='ipl@2013')

if conn.is_connected():
    print("connection is successful")
cursor=conn.cursor()
cursor.execute('select * from emp')
rows=cursor.fetchall()
print("Total from of rows",cursor.rowcount)
for row in rows:
    print(row)
conn.close()