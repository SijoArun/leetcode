from abc import abstractmethod,ABC


class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass



class Threeseries(BMW):
    def __init__(self,cruisecontrol,make,model,year):
        super().__init__( make, model, year)
        self.cruisecontrol=cruisecontrol

    def display(self):
        print(self.cruisecontrol)

    def start(self):
            print("Button start")


    def stop(self):
            print("Button stop")

    def drive(self):
        print("3 series is driven")


class Fiveservice(BMW):
    def __init__(self,parkingcontrol,make,model,year):
        super().__init__( make, model, year)
        self.parkingcontrol=parkingcontrol

    def start(self):
        super().start()
        print("Voice control start")

    def stop(self):
        print("Voice control stop")

    def drive(self):
        print("5 series is driven")


threeservice=Threeseries(True,"BMW","312i","2009")
print(threeservice.cruisecontrol)
print(threeservice.make)
print(threeservice.model)
print(threeservice.year)
threeservice.start()
threeservice.drive()
threeservice.stop()
threeservice.display()

print("@@@@@@")


fiveservice=Fiveservice(True,"BMW","512i","2015")
print(fiveservice.parkingcontrol)
print(fiveservice.make)
print(fiveservice.model)
print(fiveservice.year)
fiveservice.start()
fiveservice.drive()
fiveservice.stop()
