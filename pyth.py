name=["ansil","jibin","farih"]
select=int(input("select a number(1 add,2 select,3 edit,4 dlt)"))
if select==1:
    n=input("enter a name:")
    name.append(n)
    print(name)
elif select==2:
    n=input("enter a selected name:")
    data=name.index(n)
    print("your selected name:",name[data])
elif select==3:
    n=input("enter a name:")
    m=input("enter raplacing name:")
    data=name.index(n)
    name[data]=m
    print(name)
elif select==4:
    n=input("enter the deleting name:")
    data=name.index(n)
    del name[data]
    print(name)
else :
    print("invalid data:")
    