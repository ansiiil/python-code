def data(a,b):
    global c
    global d
    global e
    global f
    c=a+b
    d=a-b
    e=a*b
    f=a//b
def sum():
    print("sum:",c)
def sub():
    print("sub:",d)
def multiple():
    print("multiple:",e)
def division():
    print("dividion:",f)     
a=int(input("enter a number:"))
b=int(input("enter a second number:"))
data(a,b)
sum()
sub()
multiple()
division()    
