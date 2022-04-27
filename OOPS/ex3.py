class student:
    #contructor method
    def __init__(self,n='.',m=0):
        self.name=n
        self.marks=m
    
    #instance method
    def display(self):
        print("Hi",self.name)
        print("your marks:",self.marks)

#constructor is called without arguments
s=student()
s.display()
print("------------")

#contructor is called with 2 arguments
s1=student("vishnu",690)
s1.display()
print("------------")



