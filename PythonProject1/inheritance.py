class Vehicle:
     def general_usage(self):
         print("general use : transportation")
class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels=4
        self.has_roof=True
    def specific_usage(self):
        print("specific use: commute to work, vacation with family")
class Motorcycle(Vehicle):
    def __init__(self):
        print("I am motorcycle")
        self.wheels = 2
        self.has_roof =False
    def specific_usage(self):
        print("specific use: road trip, racing")
class Animal:
    def supers(self):
        print("Animals generally live in the forest")
class Dog(Animal):
    def __init__(self):
        self.bark=True
        self.legs=4
        Animal.supers(self)
    def info(self):
        print(f"Dogs bark and they have {self.legs} legs")
class Duck(Animal):
    def __init__(self):
        self.bark=False
        self.legs=2
        Animal.supers(self)
    def info(self):
        print(f"Ducks don't bark and they have {self.legs} legs")
c= Car()
c.general_usage()   #general usage can be called even though its not directly an instance of class car
c.specific_usage()
d=Duck()
d.info()
if c.has_roof:
    print("Yeah it can protect you from rain")