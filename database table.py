import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="",database="assssl")
cur=conn.cursor()
if conn:
    cur.execute("create table student(name char(20),eng int,math int)")
    print("table creatd sucess")
else:
    print("connection failed")