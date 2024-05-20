from tkinter import *
def click(num):
    first_value=str(e1.get())
    e1.delete(0,END)
    e1.insert(0,first_value+str(num))
def sub():
    second_value=str(e1.get)
    global old_value 
    old_value=second_value
    global math 
    math="sub"
    e1.delete(0,END)
def sum():
    second_value=str(e1.get)
    global old_value 
    old_value=second_value
    global math 
    math="sum"
    e1.delete(0,END)

def mul():
    second_value=str(e1.get)
    global old_value 
    old_value=second_value
    global math 
    math="mul"
    e1.delete(0,END)
def div():
    second_value=str(e1.get)
    global old_value 
    old_value=second_value
    global math 
    math="div"
    e1.delete(0,END)
def equal():
    new_value=str(e1.get())
    e1.delete(0,END)
    if math=="sum":
        result=int(new_value)+int(old_value)
        e1.insert(0,result)
    elif math=="sub":
        result=int(new_value)-int(old_value)
        e1.insert(0,result)
    elif math=="mul":
        result=int(new_value)*int(old_value)
        e1.insert(0,result)
    else:
        result=int(new_value)/int(old_value)
        e1.insert(0,result)
window=Tk()
window.title("calculator")
window.geometry("400x500")
window.resizable(False,False)
window.configure(background="black")

window.attributes("-topmost",True)
window.attributes("-alpha",0.9)
window.iconbitmap("favicon.ico")
e1=Entry()
e1.place(x=130,y=20)
btn=Button(text="1",command=lambda:click("1"))
btn.place(x=10,y=50)
btn1=Button(text="2",command=lambda:click("2"))
btn1.place(x=10,y=75)
btn2=Button(text="3",command=lambda:click("3"))
btn2.place(x=10,y=100)
btn3=Button(text="4",command=lambda:click("4"))
btn3.place(x=30,y=50)
btn4=Button(text="5",command=lambda:click("5"))
btn4.place(x=30,y=75)
btn5=Button(text="6",command=lambda:click("6"))
btn5.place(x=30,y=100)
btn6=Button(text="7",command=lambda:click("7"))
btn6.place(x=50,y=50)
btn7=Button(text="8",command=lambda:click("8"))
btn7.place(x=50,y=75)
btn8=Button(text="9",command=lambda:click("9"))
btn8.place(x=50,y=100)
btn9=Button(text="0",command=lambda:click("0"))
btn9.place(x=30,y=125)

btn10=Button(text="-",command=sub)
btn10.place(x=10,y=125)
btn11=Button(text="+",command=sum)
btn11.place(x=70,y=50)
btn12=Button(text="*",command=mul)
btn12.place(x=50,y=125)
btn13=Button(text="/",command=div)
btn13.place(x=70,y=75)
btn14=Button(text="=",command=equal)
btn14.place(x=70,y=100)





















window.mainloop()