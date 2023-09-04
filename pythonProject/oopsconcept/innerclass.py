class car:
    def __init__(self,name,model):
        self.name=name
        self.modelyear=model

    class engine:
        def __init__(self,engineno):
            self.engineno=engineno
        def start(self):
            print("Engine started")

c1=car("BMW",2018)
e1=c1.engine(212121)
e1.start()
