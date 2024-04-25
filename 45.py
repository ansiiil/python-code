name=[]
def start():
    select=int(input("select a number(1 add,2 select,3 edit,4 delete,5 exit)"))
    if select==1:
        n=input("enter a number:")
        name.append(n)
        print(name)
        start()
    elif select==2:
        n=input("enter a selected name:")
        if n in name:
            print(n)
        else :
            name.append(n)
            print(name)
            data=name.index(n)
            print("your selected name:",name[data])
            start()
    elif select==3:
        n=input("enter a name:")
        m=input("enter replacing name:")
        if n in name:2

            print(n)
            data=name.index(n)
            name[data]=m
            print(name)
        else:
            print(n,"the name is not in list")
        start()
    elif select==4:
        n=input("enter the deleting name:")
        data=name.index(n)
        del name[data]
        print(name)
        start()
    else :
        exit()
start()

