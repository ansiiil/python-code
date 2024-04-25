a=100                    # a is global variable
def add():
    b=200                #b is local varaiable
    c=a+b
    print("sum :",c)
add()
print("value of A",a)