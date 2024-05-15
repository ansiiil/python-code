import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="aaa")
cur=conn.cursor()
n=int(input("select(1 create,2 add,3 update,4 del)"))
if n==1:
    m=input("enter a table name")
    if conn:
        cur.execute("create table %s(name char(20),mala int,math int)"%m)
        print("table created")
elif n==2:
    name=input("enter a name")
    mala=int(input("enter a mala mark"))
    math=int(input("enter a math mark"))      
    if conn:
        cur.execute("insert into shadow value('%s',%s,%s)"%(name,mala,math))
        conn.commit()
        print("%s added succesfully"%name)
elif n==3:
    m=input("enter a table name")
    name1=input("enter a name to be changed") 
    name2=input("enter a name to be substituted")
    if conn:
        cur.execute("update %s set name='%s'where name='%s'"%(m,name1,name2))   
        conn.commit()
        print("database updated succesfully")    
elif n==4:
    m=input("enter a table name")        
    name=input("enter a name")
    if conn:
        cur.execute("delete from %s where name='%s'"%(m,name))
        conn.commit()
        print("deleted succesfully")
else:
    m=input("enter a table name")
    name=input("enter a name")
    if conn:
        cur.execute("select from %s where name='%s'"%(m,name))  
        result=cur.fetchall()
        for a in result:
            print("name :",a[0])      
 