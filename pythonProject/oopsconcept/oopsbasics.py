class Product:
    def __init__(self):
        self.name="Iphone"
        self.description="Its awesome"
        self.amount = 700

    def __del__(self):
        print("Inside the destructor")

    def display(self):
        print(self.name)
        print(self.description)
        print(self.amount)

p1=Product()
p1.display()
p1=None

p2=Product()
p2.display()
p2=None