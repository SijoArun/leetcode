import mysql.connector

def delete(id):
    conn=mysql.connector.connect(host="localhost",database='mydb',user='root',password='ipl@2013')
    if conn.is_connected():
        print("connection is successful")
        cursor=conn.cursor()
        str="delete from emp where id='%d'"
        args=(id)
    try:
        cursor.execute(str % args)
        conn.commit()
        print("Employee deleted")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

idvalue=int(input("Enter the id which you want to delete"))
delete(idvalue)