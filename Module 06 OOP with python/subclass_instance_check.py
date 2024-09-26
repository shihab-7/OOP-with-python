class Book:
    def __init__(self,name) -> None:
        self.name = name

    def read(self):
        raise NotImplementedError

class Physics(Book):
    def __init__(self, name, lab) -> None:
        self.lab = lab
        super().__init__(name)

    def read(self):
        print("reading vector")

topon = Physics('topon',True)

print(issubclass(Physics,Book))
print(isinstance(topon,Physics))
print(isinstance(topon,Book))

topon.read() # function a pass deowa thakle pass kore choel jabe

# but abstruct call korle parent class theke child class a giye na pele error raise kore dile oita dekhabe r function complete kore dile r error ta dekhabe na