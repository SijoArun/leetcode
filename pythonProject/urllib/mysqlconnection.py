import mysql.connector

conn=mysql.connector.connect(host="localhost",database='mydb',user='root',password='ipl@2013')

if conn.is_connected():
    print("connection is successful")
cursor=conn.cursor()
cursor.execute('select * from emp where id={}'.format('2'))
row=cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone()

conn.close()