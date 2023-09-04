import mysql.connector

def update(id):
    conn=mysql.connector.connect(host="localhost",database='mydb',user='root',password='ipl@2013')
    if conn.is_connected():
        print("connection is successful")
        cursor=conn.cursor()
        str="update emp set sal='25000' where id='%d'"
        args=(id)
    try:
        cursor.execute(str % args)
        conn.commit()
        print("Employee updated")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

idvalue=int(input("Enter the id which you want to update"))
update(idvalue)