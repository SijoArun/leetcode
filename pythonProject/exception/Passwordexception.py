class pwderror(Exception):
    def __init__(self,msg):
        self.msg=msg
try:
    pwd=input("Enter the password")
    assert len(pwd)>7,"Password character should be greater than or equal to 8"
except AssertionError as obj:
    print(obj)
    raise pwderror("Enter the valid number")
