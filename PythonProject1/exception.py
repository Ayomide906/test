class Accident(Exception):#since this is how we inherit a class
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print("User defined exception: ",self.msg)
x=int(input("Enter a number"))
try:
    y=int((input("Enter another number")))
except Exception as b:
    print("Exception is: ",type(b).__name__)
    y="INPUT IS NOT INTEGER"
try:
    z=x/y
except ZeroDivisionError as e:
    print("Exception occured: ",e)
    z="undefined"
except TypeError as a:
    print("Exception is: ",type(a).__name__)
    z=None
print("Division is: ",round(z,2))
#raise standard exception i.e add your own exception class instead of zeroD, tYPE ETC
try:
    raise Accident("Crash between two cars")
except Accident as e:#e acts like a class
    e.print_exception()
def process_file():
    try:
        f=open("c\\data\\country2.txt")
        print(f)
        y = 1 / 0
        print(y)
    except FileNotFoundError as e:
        print("Exception occurred")
    finally:# this helps to run a code even if an exception has been called upward line
        print("clean up file")
        #it will execute no matter what
        f.close()
process_file()