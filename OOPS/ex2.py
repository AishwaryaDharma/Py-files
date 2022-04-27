#1.Writing the class
class student:
    #instance method
    def __init__(self): #self is current class instance
    #defining attributes i.e. contructing or defining the indtances
    #thus, constructor method     
        self.name="Vishnu"   #name,age,marks are instance variables
        self.age=20
        self.marks=98.7

    #also, instance method
    #defining method called instance method that uses self as first parameter
    def talk(self):
        print("Hi, I am ",self.name)
        print("i am {} years old".format(self.age))
        print("i have got {} marks".format(self.marks))


#2.using the class
#create an instance using student class
#s1 is instance or an object
#object creation represents allocation of memory to store actual data of variables
s1=student()  


#calling the method talk using object or instance
s1.talk()


