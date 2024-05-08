class first:
    def one(self):
        print("its a first class")
class second:
    def two(self):
        print("its a second class")
class third(first,second):
    def three(self):
        print("its a third class")
        
x=third()
x.one()
x.two()
x.three()     