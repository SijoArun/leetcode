class patient:

    def setid(self,id):
        self.id=id

    def setname(self,name):
        self.name=name

    def setssn(self, ssn):
            self.ssn = ssn

    def getid(self):
        return self.id

    def getname(self):
        return self.name

    def getssn(self):
        return self.ssn

patient1=patient()
patient1.setid("123")
patient1.setname("John")
patient1.setssn("US2121212")
print(patient1.getid())
print(patient1.getname())
print(patient1.getssn())






