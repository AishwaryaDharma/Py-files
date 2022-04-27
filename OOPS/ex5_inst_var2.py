#code for changing values of variables in method 

class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def meth1(self):
        print("a==",self.a)
        print("b==",self.b)

    def meth2(self):
        self.a+=3
        self.b+=5

    
#creating object t1 
t1=Test()
t2=Test()

t1.meth1()  #assigning values in methods to objects and calling it 
t2.meth2()  #assigning values and calling it 

#printing values

print("-------This is Meth 1--------")
print("a is",t1.a)
print("b is",t1.b)
print("-----------------------------")

print("-------This is Meth 2--------")
print("a is",t2.a)
print("b is",t2.b)
print("-----------------------------")
