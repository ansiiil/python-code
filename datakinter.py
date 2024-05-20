import mysql.connector
from tkinter import*
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="kinter")
cur=conn.cursor
if conn:
    


window=Tk()
window.title("nill")
window.geometry("400x500")
window.resizable(False,False)
window.configure(background="green")
window.attributes("-topmost",True)
window.attributes("-alpha",0.9)
lbl=Label(text="name")
lbl.place(x=30,y=50)
lbl1=Label(text="adress")
lbl1.place(x=30,y=80)
lbl2=Label(text="phone")
lbl2.place(x=30,y=110)
e1=Entry()
e1.place(x=68,y=50)
e2=Entry()
e2.place(x=70,y=80)
e3=Entry()
e3.place(x=72,y=110)


btn=Button(text="save",)
btn.place(x=100,y=150)



window.mainloop()
