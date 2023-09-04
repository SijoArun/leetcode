from datetime import *

class project:
    def __init__(self,name,startdate,enddate):
        self.name=name
        self.startdate=startdate
        self.enddate=enddate
        self.tasks=[]

    def addtask(self,task):
        self.tasks.append(task)

class task:
    def __init__(self,name,duration):
        self.name=name
        self.duration=duration
        self.resources=[]

    def addresource(self,resource):
        self.resources.append(resource)

class resource:
    def __init__(self,name,skill):
        self.name=name
        self.skill=skill

project=project("AI",date(2023,3,15),date(2025,3,15))
task=task("semsester 1","6 months")
resource=resource("john","python")
task.addresource(resource)
project.addtask(task)

for eachtask in project.tasks:
    print(eachtask.name)
    for eachresource in eachtask.resources:
        print(eachresource.name)
        print(eachresource.skill)