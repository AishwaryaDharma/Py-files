class Emp:
    def setName(self,name):
        self.name=name

    def setEmpID(self,empid):
        self.empid=empid

    def setSal(self,sal):
        self.sal=sal

    def getName(self):
        return self.name

    def getEmpID(self):
        return self.empid

    def getSal(self):
        return self.sal

e=Emp()
e.setName("Renu")
e.setEmpID("16151123")
print(e.getName())
print(e.getEmpID())