class tooyoung(Exception):
    def __init__(self,msg):
        self.msg=msg

class tooold(Exception):
    def __init__(self,msg):
        self.msg=msg

x=int(input("Enter a number"))
if(x<18):
    raise tooyoung("you are under 18, not eligible")
elif(x>90):
    raise tooold("you are old, not eligible")
else:
    print("you are eligible")