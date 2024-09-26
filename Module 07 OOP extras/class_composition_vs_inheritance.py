# inheritance provides you 'is a' relation
class Animal:
    pass
# dog is an animal
class Dog(Animal):
    pass
# tiger is an animal
class Tiger(Animal):
    pass


# composition

class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        return 'Engine started'
    
class Driver:
    def __init__(self) -> None:
        pass

# car "has a" relation
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()

# another example

class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity


class Computer:
    def __init__(self, cores, ram_size, hd_capasity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disk = HardDrive(hd_capasity)

mac = Computer(8, 12, 120)

# follow 'geeks for geeks' to see more for composition vs inheritance