class overLimithrow(Exception):
    def __init__(self,msg):
        self.msg=msg

def withdrawal(amount):
    if(amount>500):
        raise overLimithrow("Please enter the valid number")
    else:
        print("Amount is correct")

withdrawal(400)