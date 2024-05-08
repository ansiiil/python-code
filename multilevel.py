class first:
    def one(self):
        print("its a first class")
class second(first):
    def two(self):
        print("its a second class")
class third(second):
    def three(self):
        print("its a third classd")
        
x=third()
x.one()
x.two()
        