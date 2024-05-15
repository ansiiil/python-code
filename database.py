import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="")
cur=conn.cursor()
n=input("enter a database:")
if conn:
    cur.execute("create database %s"%n)
    print(n," database success")
else:
    print("connection failed")
    