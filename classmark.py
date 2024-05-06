class student:
    def data(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def total(self):
        self.e=self.a+self.b+self.c+self.d
        print("total mark :",self.e)
    def percentage(self):
        self.x=self.e*100//400
        print("percentage :",self.x)
    def average(self):
        self.f=self.e//4
        print("average mark :",self.f)
x=student()
x.data(10,20,30,40)
x.total()
x.percentage()
x.average()
