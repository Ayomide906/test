#produce a fibonaaci sequence using generator
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for f in fib():   #when a generator function next is first called it runs until it encounter the first yield
    if f> 50: #when the next() is called again execution resumes immediately after the previous yield
        break
    print(f)
#benefits of using generators over class based iterators
#1. You wont need to define iter() and next() methods
#2. you dont need to raise StopIteration exception