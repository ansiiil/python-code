class calculation:
    def data(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        c=self.a+self.b
        print("sum :",c)
    def mul(self):
        e=self.a*self.b
        print("mul :",e)
    def div(self):
        f=self.a//self.b
        print("div :",f)
    def sub(self):
        g=self.a-self.b
        print("sub :",g)
x=calculation()
x.data(10,20)
x.sum()
x.mul()
x.div()
x.sub()
