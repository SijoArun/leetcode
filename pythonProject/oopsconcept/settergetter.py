class programmer:
    def setname(self,n):
        self.name=n

    def setsalary(self,sal):
        self.salary=sal

    def settech(self,techs):
        self.tech=techs

    def getname(self):
        return self.name

    def getsalary(self):
        return self.salary

    def gettech(self):
        return self.tech

p1=programmer()
p1.setname("sijo")
p1.setsalary(10000)
p1.settech(["java","python"])

print(p1.getname())
print(p1.getsalary())
print(p1.gettech())