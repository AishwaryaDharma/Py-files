'''
2. Static variable: value does not change from obj to obj.
    declared in 
    -> class directly but outside the method (e.g. a=10)
    -> in constructor (e.g. Test.a=10)
'''

class Test():
    a=10        #class/static variable
    #contructor method
    def __init__(self):
        self.x=22
        self.y=33
  
#creating ref obj
t1=Test()
t2=Test()

print("T1 object and A=",t1.a)
print("T2 object and A=",t2.a)
Test.a=211
print("T1 object and A=",t1.a)
print("T2 object and A=",t2.a) 