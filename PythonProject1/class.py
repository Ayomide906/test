class Human:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name, "acts")
    def speaks(self):
        print(self.name,"says how are you?")

tom=Human("tom","actor")
tom.do_work()
tom.speaks()
print(tom.name)
"""deleting occupation attribute"""
del tom.occupation
try:
    print(tom.occupation)
except AttributeError as e:
    print("tom.occupation is not defined")
'''delete a whole object'''
del tom
try:
    print(tom)
except NameError as a:
    print("tom is not defined")

