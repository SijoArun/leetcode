from datetime import *

class Event:
    def __init__(self,startTime,endTime):
        self.startTime=startTime
        self.endTime=endTime
        self.venues=[]

    def addvenue(self,venue):
        self.venues.append(venue)

class venue:
    def __init__(self,name):
        self.name=name
        self.addressess=[]

    def addaddress(self,address):
        self.addressess.append(address)

class address:
    def __init__(self,street,city,state,country,zipcode):
        self.street=street
        self.city=city
        self.state = state
        self.country = country
        self.zipcode = zipcode

estartdate=date(2023,2,1)
estartime=time(6,10,12)
eventstarttime=datetime.combine(estartdate,estartime)

eenddate=date(2023,2,1)
eendtime=time(8,10,12)
eventendtime=datetime.combine(eenddate,eendtime)


event=Event(eventstarttime,eventendtime)
venue=venue("RR mahal")
address=address("2th street","chennai","TN","india","600001")
venue.addaddress(address)
event.addvenue(venue)

for eachvenue in event.venues:
    print(event.startTime)
    print(event.endTime)
    print(eachvenue.name)
    for eachaddress in eachvenue.addressess:
        print(eachaddress.street)
        print(eachaddress.city)
        print(eachaddress.state)
        print(eachaddress.country)
        print(eachaddress.zipcode)