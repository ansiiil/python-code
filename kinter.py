from tkinter import *
def add():
    sum=int(e1.get())+int(e2.get())
    e3.insert(0,str(sum))
def sub():
    sub=int(e1.get())-int(e2.get())
    e3.delete(0,END)
    e3.insert(0,str(sub))
    
    
def mul():
    mul=int(e1.get())*int(e2.get())
    e3.delete(0,END)
    e3.insert(0,str(mul))
    
    

window=Tk()

window.title("welcome")
window.geometry("400x500")
window.resizable(False,False)
window.configure(background="#8c6d74")

window.attributes("-topmost",True)
window.attributes("-alpha",0.9)
window.iconbitmap("favicon.ico")
lbl=Label(text="enter first number")
lbl.place(x=20,y=20)
lbn=Label(text="enter second number")
lbn.place(x=20,y=50)
e1=Entry()
e1.place(x=130,y=20)
e2=Entry()
e2.place(x=150,y=51)
btn=Button(text="sum",command=add)
btn.place(x=180,y=90)
btn1=Button(text="sub",command=sub)
btn1.place(x=220,y=90)
btn2=Button(text="mul",command=mul)
btn2.place(x=260,y=90)
e3=Entry()
e3.place(x=150,y=130)

window.mainloop()