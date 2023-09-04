class duck:
    def talk(self):
        print("quack quack")

class human:
    def talk(self):
        print("Hi Hello")

def talk(obj):
    obj.talk()

d=duck()
talk(d)

h=human()
talk(h)