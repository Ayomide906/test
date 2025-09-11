class RemoteControl():
    def __init__(self):
        self.channels=["HBO", "CNN", "ABC", "ESPN"]
        self.index=-1 #initial channel i.e tv is off
    def __iter__(self):
        return self  #this will retuen the RemoteControl class object
    def __next__(self):
        self.index +=1
        if self.index ==len(self.channels):
            raise StopIteration
        return self.channels[self.index]
    def Get_index(self):
        index=self.index
        return "index is",index
class fib():
    def __init__(self,limit):
        self.limit=limit
        self.arr=[]
        self.index=-1
        self.a=0
        self.b=1
        self.stopIteration=False
        self.arr.append(self.a)
        while self.a<limit:
            if self.b> limit:
                break
            self.a,self.b=self.b,self.a+self.b
            self.arr.append(self.a)
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index==len(self.arr):
            self.stopIteration=True
            raise StopIteration
        return self.arr[self.index]

r=RemoteControl()
f=fib(150)
itre=iter(f)
try:
    while not f.stopIteration:
        print(next(itre))
except StopIteration:
    print("iteration stopped")
itr=iter(r)
print(next(itr))
next(itr)
print(r.Get_index())