from tkinter import*
from tkinter import filedialog as fd
import tkinter.messagebox as Message
import tkinter.font as tkfont
from tkinter import colorchooser as cc

window=Tk()


window.title("Notepad")
window.geometry("500x500")
window.iconbitmap("favicon.ico")
window.resizable(True,True)
text=Text(wrap="word")
text.pack(side="top",fill="both",expand=True)

def new_file():
    text.delete("1.0","end")
    window.title("Notepad")
def open():
    file=fd.askopenfile(parent=window,mode="rb",title="Open A File")#rb=read binary
    if file:
        content=file.read()
        text.delete("1.0","end")
        text.insert("1.0",content)#0 or 1.0 is okay
        file.close()
        window.title(file.name)
def save():
    file=fd.asksaveasfile(mode="w",defaultextension=".txt",filetypes=[("Text Document","*.txt"),("All Files","*.*")])
    if file:
        content=text.get("1.0","end")
        file.write(content)
        file.close()
        window.title(file.name)
def cut():
    text.event_generate("<<Cut>>")
def copy():
    text.event_generate("<<Copy>>")
def paste():
    text.event_generate("<<Paste>>")
def bgcolor():
    color=cc.askcolor(title="Select The Color")
    text.config(bgcolor=[1])



