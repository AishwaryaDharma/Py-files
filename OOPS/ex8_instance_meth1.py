#1. Instance Method

class Emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    def show(self):
        print(self.name,"has",self.sal,"Rs. Salary")

    def calci(self):
        print("Yearly Package=",self.sal*12)
'''
e1=Emp("ABCD",10)

e1.show()
e1.calci()

'''
#user input

num_of_emp=int(input("No. of emp: "))
for i in range(num_of_emp):
    name=input("Enter Employee name: ")
    sal=int(input("Salary is: "))
    e=Emp(name,sal)
    print("------------------")
    e.show()
    e.calci()
    print("------------------")