'''
#deleting a instance variable

class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def meth1(self):
        print("b=",self.b)
        del self.b              #deleting variable

#create reference object
t1=Test()
t2=Test()

#assigning the values and calling it
t1.meth1()
print("this is T1: ", t1.__dict__)  #printing object values
print("--------------------------")
print("This is T2: ", t2.__dict__)

'''
#variable out of class could change everything!! 

class Test:
    def __init__(self):
        self.a=10
        self.b=20

#create reference object
t1=Test()
t2=Test()

t1.a=111

print("T1 is ",t1.__dict__)
print("T2 is ",t2.__dict__)
