from datetime import *

def validateccexpire(expdate):
    if expdate>datetime.now().date():
        return "valid"
    else:
        raise RuntimeError("Card is expired")

