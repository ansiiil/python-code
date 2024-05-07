class bank:
      def data(self,n,m,g,h,f,o,i):
           self.n=n
           self.m=m
           self.g=g
           self.h=h
           self.f=f
           self.o=o
           self.i=i
      def customer(self):
             self.n=input("enter customer name:")
             self.m=int(input("enter account num of customer:"))
             print("customer details completed")
      def banking(self):
             self.g=int(input("enter aloan ammount"))
             self.h=int(input("enter a interest amoun t"))        
             self.f=int(input("loan validity"))
             print("banking details")
      def interest(self):
            self.o=self.g*self.h*self.f//100
            print("interest amount",self.o)
      def emi(self):
            self.i=self.o+self.g//(self.f*12)
            print("emi amount",self.i)    
x=bank()
x.customer()
x.banking()
x.interest()
x.emi()