from abc import abstractmethod,ABC

class TouchScreenLaptop(ABC):
    def __init__(self):
        self.click
        self.scroll

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):

    def scroll(self):
        print("Scorll the HP screen")

class HPNotebook(HP):

    def click(self):
        print("click the HPnotebook screen")


class Dell(TouchScreenLaptop):

    def scroll(self):
        print("Scorll the Dell screen")


class DellNotebook(Dell):

    def click(self):
        print("click the Dellnotebook screen")

HPNotebook=HPNotebook()
HPNotebook.scroll()
HPNotebook.click()

DellNotebook=DellNotebook()
DellNotebook.scroll()
DellNotebook.click()


