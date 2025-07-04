import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__ ," took ", (end-start)*1000, "mil sec" )
        return result
    return wrapper
@time_it
def ogba(alele="dont go"):
    print(alele)

import multiprocessing
#create two processes , one to calc square and one to calc cube
square_result=[]
def calc_square(numbers):
    global square_result
    for n in numbers:
        print(f"square of {n} is : ", n*n)
        square_result.append(n*n)
    #This has to be printed within the process
    print("within the process result is : " + str(square_result))
def calc_cube(numbers):
    for n in numbers:
        print(f"cube of {n} is: " + str(n*n*n))
def combined_target(numbers,func):
    calc_cube(numbers)
    time_it(func)
if __name__=='__main__':
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=calc_square, args=(arr,))
    p2=multiprocessing.Process(target=combined_target,args=(arr,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    ogba()
    print("Done!")