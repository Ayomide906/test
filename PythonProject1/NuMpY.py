import numpy as np
import time
import sys
size=1000000
l1= range(size)
l2= range(size)

a1=np.arange(size)
a2=np.arange(size) #size of an arr times bytesize of each element
start = time.time()
result= [(x+y) for x,y in zip(l1,l2)]
print("python list took",(time.time()-start)*1000)

start=time.time()
result=a1+a2
print("numpy took: ",(time.time()-start)*1000)