class first:
    def one(self):
        print("its a first class")
class second(first):
    def two(self):
        print("its a second class")
x=second()
x.one()
x.two()
        