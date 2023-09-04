class flight:
    def __init__(self,engine):
        self.engine=engine
    def startengine(self):
        self.engine.start()

class airbusengine():
    def start(self):
        print("Airbus engine started")
class boeingengine():
    def start(self):
        print("Boeing engine started")

ae=airbusengine()
f=flight(ae)
f.startengine()

be=boeingengine()
f=flight(be)
f.startengine()