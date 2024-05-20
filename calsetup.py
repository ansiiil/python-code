from tkinter import*
def click(num):
    first_value=str(e1.get())
    e1.delete(0,END)
    e1.insert(0,first_value+str(num))

window=Tk()

window.title("calculator")
window.geometry("400x500")
window.resizable(False,False)
window.configure(background="black")

window.attributes("-topmost",True)
window.attributes("-alpha",0.9)
window.iconbitmap("favicon.ico")

e1=Entry()
one=Button(text="1",command=lambda:click(1))
two=Button(text="2",command=lambda:click(2))
add=Button(text="+")
equal=Button(text="=")
e1.pack()
one.pack()
two.pack()
equal.pack()
add.pack()
window.mainloop()