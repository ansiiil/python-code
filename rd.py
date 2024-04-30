file=open("text.txt","a")
def add():
    name=input("enter name:")
    adress=input("enter adress:")
    phone=input("enter phone number:")
    file.write("name:"+name+"\nadress:"+adress+"\n+phone:"+phone+"\n""___________________""\n")
    print(name+"details adedd sucesfully")
for a in range(3):
    add()