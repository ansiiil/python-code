class first:
    def one(self):
        print("its a first class")
class second:
    def two(self):
        print("its a second class")
class fourth:
    def four(self):
        print("its a fourth class")
class third(first,second,fourth):
    def three(self):
        print("its a third class")
        
x=third()
x.one()
x.two()
x.three()   
x.four()  