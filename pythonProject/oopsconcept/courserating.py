class course:
    def __init__(self,name,rating):
        self.name=name
        self.ratings=rating

    def average(self):
        noofiteams=len(self.ratings)
        average=sum(self.ratings)/noofiteams
        print(average)

c1=course("Java",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2=course("Javascript",[5,5,3,4,5])
print(c2.name)
print(c2.ratings)
c2.average()
