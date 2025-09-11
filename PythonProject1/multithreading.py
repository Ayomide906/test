#calculate cube and square at the same time
import time
import threading
no_functions=0
def calc_square(numbers):
    global no_functions
    no_functions+=1
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square: ",n*n)

def calc_cube(numbers):
    global no_functions
    no_functions += 1
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube: ",n*n*n)

arr=[1,3,4,5,6]
tt=time.time()
t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()
t1.join()
t2.join()
def worker():
    time.sleep(0.5)
threads=[]
for i in range(3):
    t=threading.Thread(target=worker)
    t.start()
    threads.append(t)
print("total threads before joining: ",threading.active_count())
for t in threads:
    t.join()
print("total threads after joining: ",threading.active_count())
print("done in :",time.time()-tt)
print("Hah... I am done with all my work now!")
print(no_functions)