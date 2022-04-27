''' 
%Types of variables:%


-1. Instance Varibles and -2. class/static variable

1.instance variable: separate copy is created in every instance or obj.

can be created in:
    ->a. inside a constructor
    ->b. in method using self
        both a and b are in class
    ->c. outside class using reference object
'''
'''
#a.inside a contructor
class Employee:
    #contructor
    def __init__(self):
        self.id=10          #instance variable 1
        self.name="Renu"    #instance variable 2

emp1=Employee()
print(emp1.__dict__)

'''
'''
#b.instance variable in Method using self:
class Employee:
    #contructor
    def __init__(self):
        self.id=10          #instance variable 1
        self.name="Renu"    #instance variable 2

    #method
    def sal(self):
        self.sal=600        #instance variable 3

emp1=Employee()
emp1.sal()        #HAVE TO CALL THE FUNCTION TO DISPLAY VARIABLES
print(emp1.__dict__)
'''
'''
#c.Outside class but using object reference variable
class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def meth1(self):
        self.c=30

#creating object t1
t1=Test()
t1.meth1()

t1.d=40      #outside class, with reference obj t1
print(t1.__dict__)
'''

#accessing the variables(in method usinf self and outside class using reference object)
class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def meth1(self):
        print("a==",self.a)
        print("b==",self.b)

    
#creating object t1
t1=Test()
t1.meth1()

print("-------This is Meth1--------")
print("a is",t1.a)
print("b is",t1.b)
print("-----------------------------")
