class patient:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.component=[]

    def adddata(self, component):
        self.component.append(component)


class component:
    def __init__(self,componentname,rating):
        self.componentname=componentname
        self.rating=rating
'''
p1=patient("john","34")
c1=component("BP","80")
p1.adddata(c1)


c2=component("Heartrate","120")
p1.adddata(c2)

for eachcomponent in p1.component:
    print(eachcomponent.componentname)
    print(eachcomponent.rating)
'''