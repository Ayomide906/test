import time
import math
class Negative(Exception):
    def __init__(self,msg):
        self.msg=msg
    def print_Exception(self):
        print("user defined exception ",self.msg)
def time_it(func):
    def wrapper(*args, **kwargs):
        #the args and kwargs is used when you wanna assume the function can have any argument
        #args means positional argument and kwargs is keyword argument
        start=time.time()
        result = func(*args, **kwargs)
        end= time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper
def check_arg(func):
    def wrapper(arg):
        #in this case arg represent the singular argument of any function decorated by this
        #this means the decorator wont work with functions with two arguments
        if type(arg) == int and arg>=0:
            return func(arg)
        else:
            raise Negative("number is less than 0")
    return wrapper
def check_arg2(func):
    def helper(x):
        if type(x)==int:
            return func(x)
        else:
            raise TypeError
    return helper

@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result
@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result
@check_arg2
def factorial(number):
    result=math.factorial(number)
    return result
array =range(1,100000)
out_square= calc_square(array)
out_cube= calc_cube(array)
print(factorial("ade"))