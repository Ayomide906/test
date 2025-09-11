class isMajor(Exception):
    def __init__(self,msg):
        self.msg=msg
        print("An Exception occurred: ",self.msg)
class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def print_details(self):
        print(self.name," is ",self.age," years old, and is eligible")
if __name__=='__main__':
    kola=Person(17,"Bukola")
    dayo=Person(90,"Oluwadayo")
    List=[kola,dayo]
    for items in List:
        if items.age < 18:
            items.print_details()
        else:
            raise isMajor("not eligible")



