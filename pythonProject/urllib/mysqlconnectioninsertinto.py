import mysql.connector

conn=mysql.connector.connect(host="localhost",database='mydb',user='root',password='ipl@2013')

if conn.is_connected():
    print("connection is successful")
cursor=conn.cursor()
try:
    cursor.execute("insert into emp values(1,'sijo',10000)")
    conn.commit()
    print("Employee added successfully")
except:
    conn.rollback()

conn.close()