class student:
    major ="cse"
    def __init__(self,name,rollno):
        self.name=name
        self.roll=rollno

    def display(self):
        print(self.major)
        print(self.name)
        print(self.roll)

s1=student("john",1)
s2=student("mary",2)
s1.display()
s2.display()
print(student.major)
