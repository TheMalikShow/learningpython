class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year = year
    def descriptio(self):
        print(f"the Make of car is {self.make}")
        print(f"the Make of car is {self.model}")
        print(f"the Make of car is {self.year}")
    def move(self):
        print(f"{self.make} is moving with speed")
    def Applyingbrake(self):
        print(f"{self.model} is now breaking ")
    def accelerate(self):
        print(f"{self.year} is Accelerating ")
car1 = Car("","","")
car2 = Car("","","")
car2.descriptio()
car1.descriptio()
car1.accelerate()
car2.Applyingbrake()
car2.move()
car1.make="NISSAN"
car2.make = "KIA"
car1.descriptio()